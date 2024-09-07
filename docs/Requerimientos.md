# Requerimientos del Sistema - Sistema de Gestión de Citas Médicas

Este documento detalla los requerimientos funcionales y no funcionales para el sistema de gestión de citas médicas.

## Requerimientos Funcionales

1. **Registro de Pacientes**
   - El sistema debe permitir el registro de nuevos pacientes con la siguiente información:
     - Cédula
     - Nombre
     - Correo electrónico
     - Teléfono
     - Dirección

2. **Registro de Médicos**
   - El sistema debe permitir el registro de nuevos médicos con la siguiente información:
     - ID (asignado automáticamente)
     - Nombre
     - Especialidad

3. **Actualización de Disponibilidad de Médicos**
   - El sistema debe permitir actualizar la disponibilidad de los médicos, especificando:
     - Fecha y hora de inicio
     - Fecha y hora de fin
   - La disponibilidad debe ser actualizada en el sistema para la correcta programación de citas.

4. **Programación de Citas**
   - El sistema debe permitir programar citas médicas con la siguiente información:
     - Cédula del paciente
     - ID del médico
     - Fecha y hora de la cita
     - Detalle de la cita
   - El sistema debe verificar que el médico esté disponible en la fecha y hora solicitada antes de confirmar la cita.

5. **Consulta de Citas**
   - El sistema debe permitir a los pacientes consultar sus citas programadas, mostrando:
     - Fecha y hora
     - Detalle de la cita

6. **Cancelación de Citas**
   - El sistema debe permitir a los pacientes cancelar citas programadas, especificando:
     - ID de la cita a cancelar

7. **Generación de Reportes**
   - El sistema debe generar los siguientes reportes:
     - **Reporte de Demanda**: Información sobre la demanda de médicos y citas.
     - **Reporte de Cancelaciones**: Información sobre las citas canceladas.
   - Los reportes deben poder exportarse en formato Excel.

## Requerimientos No Funcionales

1. **Interfaz de Usuario**
   - La interfaz de usuario debe ser de línea de comandos (CLI) e interactiva.
   - Debe proporcionar mensajes claros y opciones de menú para la navegación.

2. **Rendimiento**
   - El sistema debe ser capaz de manejar múltiples pacientes y médicos sin afectar significativamente el rendimiento.
   - La generación de reportes debe realizarse de manera eficiente, incluso con un número grande de datos.

3. **Seguridad**
   - Los datos sensibles, como la cédula de los pacientes, deben ser manejados con cuidado.
   - Se deben implementar validaciones para asegurar que los datos ingresados sean correctos y coherentes.

4. **Escalabilidad**
   - El sistema debe estar diseñado de manera que se pueda ampliar fácilmente para incluir más funcionalidades en el futuro.

5. **Mantenimiento**
   - El código debe estar bien documentado para facilitar su mantenimiento y futuras modificaciones.
   - Se deben seguir buenas prácticas de codificación y organización del código.

## Contacto

Para preguntas o soporte adicional, puedes abrir un issue en el repositorio del proyecto o ponerte en contacto con el mantenedor.
