# main.py (continuación)

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
        print("3. Programar Cita")
        print("4. Consultar Citas")
        print("5. Cancelar Cita")
        print("6. Generar Reporte de Demanda")
        print("7. Generar Reporte de Cancelaciones")
        print("8. Salir")
        
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
            print(f"Médico {nombre} registrado con éxito.")

        elif opcion == "3":
            cedula_paciente = input("Cédula del paciente: ")
            id_medico = int(input("ID del médico: "))
            fecha_str = input("Fecha de la cita (dd-mm-yyyy hh:mm): ")
            fecha = datetime.strptime(fecha_str, "%d-%m-%Y %H:%M")
            detalle = input("Detalle de la cita: ")
            paciente = next((p for p in sistema.pacientes if p.cedula == cedula_paciente), None)
            medico = sistema.medicos[id_medico - 1]
            if paciente:
                sistema.programar_cita(paciente, medico, fecha, detalle)
            else:
                print(f"Paciente con cédula {cedula_paciente} no encontrado.")

        elif opcion == "4":
            cedula_paciente = input("Cédula del paciente: ")
            paciente = next((p for p in sistema.pacientes if p.cedula == cedula_paciente), None)
            if paciente:
                paciente.consultar_citas()
            else:
                print(f"Paciente con cédula {cedula_paciente} no encontrado.")

        elif opcion == "5":
            cedula_paciente = input("Cédula del paciente: ")
            id_cita = int(input("ID de la cita a cancelar: "))
            paciente = next((p for p in sistema.pacientes if p.cedula == cedula_paciente), None)
            if paciente:
                paciente.cancelar_cita(id_cita)
            else:
                print(f"Paciente con cédula {cedula_paciente} no encontrado.")

        elif opcion == "6":
            reporte_demanda = ReporteDemanda(1, "Demanda de Médicos", [])
            reporte_demanda.generar(sistema)
            nombre_archivo = input("Ingrese el nombre del archivo para el reporte de demanda: ")
            reporte_demanda.exportar_informe(nombre_archivo)

        elif opcion == "7":
            reporte_cancelaciones = ReporteCancelaciones(1, "Cancelaciones de Citas", [])
            reporte_cancelaciones.generar(sistema)
            nombre_archivo = input("Ingrese el nombre del archivo para el reporte de cancelaciones: ")
            reporte_cancelaciones.exportar_informe(nombre_archivo)

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
