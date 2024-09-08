# Sistema de Gestión de Citas Médicas

Este proyecto es un sistema de gestión de citas médicas que permite registrar pacientes y médicos, programar citas, actualizar la disponibilidad de los médicos y generar reportes. El sistema está diseñado en Python y utiliza la biblioteca `pandas` para la exportación de reportes en formato Excel.

## Requisitos

Para ejecutar el sistema, necesitas tener Python instalado. Además, debes instalar las siguientes dependencias:

- `pandas`, openpyxl

Puedes instalar las dependencias necesarias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt


Estructura del proyecto:

CitasMedicas/
│
├── app/
│   ├── main.py
│   ├── sistema_citas.py
│   ├── paciente.py
│   ├── medico.py
│   ├── cita.py
│   ├── reporte.py
│   └── horario.py
│
└── requirements.txt

Descripción de Archivos
main.py: Archivo principal que contiene el menú interactivo para gestionar el sistema de citas médicas.
sistema_citas.py: Contiene la clase SistemaCitas, que gestiona los pacientes, médicos y citas.
paciente.py: Define la clase Paciente, que representa a un paciente en el sistema.
medico.py: Define la clase Medico, que representa a un médico en el sistema.
cita.py: Define la clase Cita, que representa una cita médica programada.
reporte.py: Define las clases Reporte, ReporteDemanda y ReporteCancelaciones para generar y exportar reportes en formato Excel.
horario.py: Define la clase Horario, que gestiona la disponibilidad de los médicos.
Uso
Registrar Paciente: Permite ingresar la cédula, nombre, correo, teléfono y dirección de un paciente.
Registrar Médico: Permite ingresar el nombre y especialidad de un médico.
Actualizar Disponibilidad del Médico: Permite registrar las fechas y horas de disponibilidad de un médico.
Programar Cita: Permite programar una cita médica especificando la cédula del paciente, ID del médico, fecha y detalle.
Consultar Citas: Permite consultar las citas programadas para un paciente específico.
Cancelar Cita: Permite cancelar una cita programada.
Generar Reporte de Demanda: Genera un reporte de demanda de médicos y citas.
Generar Reporte de Cancelaciones: Genera un reporte de cancelaciones de citas.
Ejecución
Para ejecutar el sistema, navega al directorio del proyecto y ejecuta el archivo main.py:

bash python app/main.py
Contribuciones: Si deseas contribuir al proyecto, por favor sigue estos pasos:

Clona el repositorio:

bash git clone <(https://github.com/SqmuelAzz/CitasMedicas_Parcial.git)>

Haz un fork del repositorio.
Crea una rama nueva para tus cambios.
Realiza tus modificaciones y asegúrate de que el código esté funcionando correctamente.
Envía un pull request describiendo los cambios que has realizado.
