# main.py
from sistema_citas import SistemaCitas
from paciente import Paciente
from medico import Medico
from reporte import ReporteDemanda, ReporteCancelaciones
from datetime import datetime

def main():
    """Función principal para interactuar con el sistema de citas."""
    sistema = SistemaCitas.get_instance()

    while True:
        print("\n--- Sistema de Gestión de Citas Médicas ---")
        print("1. Registrar Paciente")
        print("2. Registrar Médico")
        print("3. Actualizar Disponibilidad del Médico")
        print("4. Programar Cita")
        print("5. Consultar Citas")
        print("6. Cancelar Cita")
        print("7. Generar Reporte de Demanda")
        print("8. Generar Reporte de Cancelaciones")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cedula = input("Cédula del paciente: ")
            nombre = input("Nombre del paciente: ")
            correo = input("Correo electrónico: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            paciente = Paciente(cedula, nombre, correo, telefono, direccion)
            sistema.agregar_paciente(paciente)
            print(f"Paciente {nombre} registrado con éxito.")

        elif opcion == "2":
            nombre = input("Nombre del médico: ")
            especialidad = input("Especialidad: ")
            id_medico = len(sistema.medicos) + 1
            medico = Medico(id_medico, nombre, especialidad)
            sistema.agregar_medico(medico)
            print(f"Médico {nombre} registrado con éxito. ID del médico: {id_medico}")

        elif opcion == "3":
            id_medico = int(input("ID del médico para actualizar disponibilidad: "))
            medico = next((m for m in sistema.medicos if m.id_medico == id_medico), None)
            if medico:
                fecha_inicio_str = input("Fecha de inicio (dd-mm-yyyy): ")
                fecha_fin_str = input("Fecha de fin (dd-mm-yyyy): ")
                fecha_inicio = datetime.strptime(fecha_inicio_str, "%d-%m-%Y")
                fecha_fin = datetime.strptime(fecha_fin_str, "%d-%m-%Y")
                # Establece una hora predeterminada si no se proporciona
                fecha_inicio = datetime.combine(fecha_inicio, datetime.min.time())
                fecha_fin = datetime.combine(fecha_fin, datetime.max.time())
                medico.actualizar_disponibilidad(fecha_inicio, fecha_fin)
                print(f"Disponibilidad actualizada para el médico {medico.nombre}.")
            else:
                print(f"Médico con ID {id_medico} no encontrado.")

        elif opcion == "4":
            cedula_paciente = input("Cédula del paciente: ")
            id_medico = int(input("ID del médico: "))
            fecha_str = input("Fecha de la cita (dd-mm-yyyy hh:mm): ")
            try:
                fecha = datetime.strptime(fecha_str, "%d-%m-%Y %H:%M")
            except ValueError:
                print("Formato de fecha incorrecto. Use el formato dd-mm-yyyy hh:mm.")
                continue
            detalle = input("Detalle de la cita: ")
            paciente = next((p for p in sistema.pacientes if p.cedula == cedula_paciente), None)
            medico = next((m for m in sistema.medicos if m.id_medico == id_medico), None)
            if paciente and medico:
                if medico.verificar_disponibilidad(fecha):
                    sistema.programar_cita(paciente, medico, fecha, detalle)
                    print(f"Cita programada para el paciente {paciente.nombre} con el médico {medico.nombre}.")
                else:
                    print(f"El médico {medico.nombre} no está disponible en la fecha {fecha}.")
            else:
                if not paciente:
                    print(f"Paciente con cédula {cedula_paciente} no encontrado.")
                if not medico:
                    print(f"Médico con ID {id_medico} no encontrado.")

        elif opcion == "5":
            cedula_paciente = input("Cédula del paciente: ")
            paciente = next((p for p in sistema.pacientes if p.cedula == cedula_paciente), None)
            if paciente:
                paciente.consultar_citas()
            else:
                print(f"Paciente con cédula {cedula_paciente} no encontrado.")

        elif opcion == "6":
            cedula_paciente = input("Cédula del paciente: ")
            id_cita = int(input("ID de la cita a cancelar: "))
            paciente = next((p for p in sistema.pacientes if p.cedula == cedula_paciente), None)
            if paciente:
                paciente.cancelar_cita(id_cita)
            else:
                print(f"Paciente con cédula {cedula_paciente} no encontrado.")

        elif opcion == "7":
            reporte_demanda = ReporteDemanda(1, "Demanda de Médicos", [])
            reporte_demanda.generar(sistema)
            nombre_archivo = input("Ingrese el nombre del archivo para el reporte de demanda: ")
            reporte_demanda.exportar_informe(nombre_archivo)

        elif opcion == "8":
            reporte_cancelaciones = ReporteCancelaciones(1, "Cancelaciones de Citas", [])
            reporte_cancelaciones.generar(sistema)
            nombre_archivo = input("Ingrese el nombre del archivo para el reporte de cancelaciones: ")
            reporte_cancelaciones.exportar_informe(nombre_archivo)

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
