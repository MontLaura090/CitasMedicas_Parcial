from sistema_citas import SistemaCitas
from paciente import Paciente
from medico import Medico
from reporte import ReporteDemanda, ReporteCancelaciones
from datetime import datetime
from notificacion import Notificacion  # Importar la clase Notificacion

def main():
    sistema = SistemaCitas.get_instance()

    while True:
        print("\n--- Sistema de Gestión de Citas Médicas ---")
        print("1. Registrar Paciente")
        print("2. Registrar Médico")
        print("3. Actualizar Disponibilidad del Médico")
        print("4. Programar Cita")
        print("5. Reprogramar Cita")
        print("6. Consultar Citas")
        print("7. Cancelar Cita")
        print("8. Generar Reporte de Demanda")
        print("9. Generar Reporte de Cancelaciones")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_paciente(sistema)
        elif opcion == "2":
            registrar_medico(sistema)
        elif opcion == "3":
            actualizar_disponibilidad(sistema)
        elif opcion == "4":
            programar_cita(sistema)
        elif opcion == "5":
            reprogramar_cita(sistema)
        elif opcion == "6":
            consultar_citas(sistema)
        elif opcion == "7":
            cancelar_cita(sistema)
        elif opcion == "8":
            generar_reporte_demanda(sistema)
        elif opcion == "9":
            generar_reporte_cancelaciones(sistema)
        elif opcion == "10":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def registrar_paciente(sistema):
    cedula = input("Cédula del paciente: ")
    nombre = input("Nombre del paciente: ")
    correo = input("Correo electrónico: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    paciente = Paciente(cedula, nombre, correo, telefono, direccion)
    sistema.agregar_paciente(paciente)
    print(f"Paciente {nombre} registrado con éxito.")


def registrar_medico(sistema):
    nombre = input("Nombre del médico: ")
    especialidad = input("Especialidad: ")
    id_medico = len(sistema.medicos) + 1
    medico = Medico(id_medico, nombre, especialidad)
    sistema.agregar_medico(medico)
    print(f"Médico {nombre} registrado con éxito. ID del médico: {id_medico}")


def actualizar_disponibilidad(sistema):
    id_medico = int(input("ID del médico para actualizar disponibilidad: "))
    medico = next((m for m in sistema.medicos if m.id_medico == id_medico), None)
    if medico:
        fecha_inicio_str = input("Fecha de inicio (dd-mm-yyyy hh:mm): ")
        fecha_fin_str = input("Fecha de fin (dd-mm-yyyy hh:mm): ")
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%d-%m-%Y %H:%M")
        fecha_fin = datetime.strptime(fecha_fin_str, "%d-%m-%Y %H:%M")
        medico.actualizar_disponibilidad(fecha_inicio, fecha_fin)
        print(f"Disponibilidad actualizada para el médico {medico.nombre}.")
    else:
        print(f"Médico con ID {id_medico} no encontrado.")


def programar_cita(sistema):
    """Programa una nueva cita."""
    cedula_paciente = input("Cédula del paciente: ")
    id_medico = int(input("ID del médico: "))
    fecha_str = input("Fecha de la cita (dd-mm-yyyy hh:mm): ")
    fecha = datetime.strptime(fecha_str, "%d-%m-%Y %H:%M")
    detalle = input("Detalle de la cita: ")
    paciente = next((p for p in sistema.pacientes if p.cedula == cedula_paciente), None)
    medico = next((m for m in sistema.medicos if m.id_medico == id_medico), None)

    if paciente and medico:
        if medico.verificar_disponibilidad(fecha):
            sistema.programar_cita(paciente, medico, fecha, detalle)
            # Mostrar el ID de la cita programada
            id_cita = len(sistema.citas)
            print(f"Cita programada con éxito. ID de la cita: {id_cita}")
            
            # Enviar notificación
            medio_notificacion = input("¿Cómo desea recibir la notificación? (correo/sms): ").lower()
            mensaje = f"Su cita con el Dr. {medico.nombre} ha sido programada para el {fecha}."
            notificacion = Notificacion(mensaje, medio_notificacion)
            if medio_notificacion == 'correo':
                notificacion.enviar(paciente.correo_electronico)
            elif medio_notificacion == 'sms':
                notificacion.enviar(paciente.telefono)
        else:
            print(f"El médico {medico.nombre} no está disponible en la fecha {fecha}.")
    else:
        if not paciente:
            print(f"Paciente con cédula {cedula_paciente} no encontrado.")
        if not medico:
            print(f"Médico con ID {id_medico} no encontrado.")


def reprogramar_cita(sistema):
    """Reprograma una cita existente."""
    id_cita = int(input("Ingrese el ID de la cita a reprogramar: "))
    cita = next((c for c in sistema.citas if c.id == id_cita), None)

    if cita:
        print(f"Cita actual: Fecha {cita.fecha}, Médico {cita.id_medico}, Detalle: {cita.detalle}")
        
        # Cambiar médico
        cambiar_medico = input("¿Desea cambiar el médico? (s/n): ")
        if cambiar_medico.lower() == 's':
            id_medico = int(input("Ingrese el nuevo ID del médico: "))
            medico = next((m for m in sistema.medicos if m.id_medico == id_medico), None)
            if medico:
                cita.id_medico = medico.id_medico
            else:
                print(f"Médico con ID {id_medico} no encontrado.")
                return

        # Cambiar fecha
        cambiar_fecha = input("¿Desea cambiar la fecha de la cita? (s/n): ")
        if cambiar_fecha.lower() == 's':
            fecha_str = input("Ingrese la nueva fecha (dd-mm-yyyy hh:mm): ")
            nueva_fecha = datetime.strptime(fecha_str, "%d-%m-%Y %H:%M")
            medico = next((m for m in sistema.medicos if m.id_medico == cita.id_medico), None)

            if medico and medico.verificar_disponibilidad(nueva_fecha):
                cita.fecha = nueva_fecha
            else:
                print(f"El médico no está disponible en la nueva fecha {nueva_fecha}.")
                return

        # Cambiar detalle
        cambiar_detalle = input("¿Desea cambiar el detalle de la cita? (s/n): ")
        if cambiar_detalle.lower() == 's':
            nuevo_detalle = input("Ingrese el nuevo detalle de la cita: ")
            cita.detalle = nuevo_detalle

        print(f"Cita reprogramada exitosamente: Fecha {cita.fecha}, Médico {cita.id_medico}, Detalle: {cita.detalle}")
        
        # Enviar notificación
        medio_notificacion = input("¿Cómo desea recibir la notificación? (correo/sms): ").lower()
        mensaje = f"Su cita ha sido reprogramada para el {cita.fecha} con el Dr. {cita.id_medico}."
        notificacion = Notificacion(mensaje, medio_notificacion)
        if medio_notificacion == 'correo':
            notificacion.enviar(cita.id_paciente)
        elif medio_notificacion == 'sms':
            notificacion.enviar(cita.id_paciente)
    else:
        print(f"Cita con ID {id_cita} no encontrada.")


def consultar_citas(sistema):
    cedula_paciente = input("Cédula del paciente: ")
    paciente = next((p for p in sistema.pacientes if p.cedula == cedula_paciente), None)
    if paciente:
        paciente.consultar_citas()
    else:
        print(f"Paciente con cédula {cedula_paciente} no encontrado.")


def cancelar_cita(sistema):
    cedula_paciente = input("Cédula del paciente: ")
    id_cita = int(input("ID de la cita a cancelar: "))
    paciente = next((p for p in sistema.pacientes if p.cedula == cedula_paciente), None)
    if paciente:
        paciente.cancelar_cita(id_cita)
        
        # Enviar notificación
        medio_notificacion = input("¿Cómo desea recibir la notificación? (correo/sms): ").lower()
        mensaje = f"Su cita con el ID {id_cita} ha sido cancelada."
        notificacion = Notificacion(mensaje, medio_notificacion)
        if medio_notificacion == 'correo':
            notificacion.enviar(paciente.correo_electronico)
        elif medio_notificacion == 'sms':
            notificacion.enviar(paciente.telefono)
    else:
        print(f"Paciente con cédula {cedula_paciente} no encontrado.")


def generar_reporte_demanda(sistema):
    reporte_demanda = ReporteDemanda(id_admin=1, tipo="Demanda de Citas", contenido=[])
    reporte_demanda.generar(sistema)
    nombre_archivo = input("Ingrese el nombre del archivo para el reporte de demanda: ")
    reporte_demanda.exportar_informe(nombre_archivo)


def generar_reporte_cancelaciones(sistema):
    reporte_cancelaciones = ReporteCancelaciones(id_admin=1, tipo="Cancelaciones de Citas", contenido=[])
    reporte_cancelaciones.generar(sistema)
    nombre_archivo = input("Ingrese el nombre del archivo para el reporte de cancelaciones: ")
    reporte_cancelaciones.exportar_informe(nombre_archivo)


if __name__ == "__main__":
    main()
