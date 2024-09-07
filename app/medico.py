# medico.py

from horario import Horario

class Medico:
    """
    Clase que representa a un médico en el sistema de gestión de citas.
    """

    def __init__(self, id_medico, nombre, especialidad):
        """
        Inicializa un nuevo objeto Medico.
        :param id_medico: ID único del médico.
        :param nombre: Nombre completo del médico.
        :param especialidad: Especialidad médica.
        """
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad
        self.horarios = []

    def actualizar_disponibilidad(self, dia, hora_inicio, hora_fin):
        """
        Actualiza el horario de disponibilidad del médico.
        :param dia: Día de la semana que el médico está disponible (e.g., "Lunes").
        :param hora_inicio: Hora de inicio de la disponibilidad.
        :param hora_fin: Hora de fin de la disponibilidad.
        """
        horario = Horario(self.id_medico, dia, hora_inicio, hora_fin)
        self.horarios.append(horario)
        print(f"Disponibilidad actualizada: {self.nombre} disponible el {dia} de {hora_inicio} a {hora_fin}.")

    def cancelar_cita(self, id_cita):
        """
        Cancela una cita del médico si corresponde a una cita programada.
        :param id_cita: ID de la cita que se quiere cancelar.
        """
        cita_cancelada = next((cita for cita in self.horarios if cita.id_cita == id_cita), None)
        if cita_cancelada:
            cita_cancelada.estado = "Cancelada"
            print(f"Cita con ID {id_cita} ha sido cancelada por el médico {self.nombre}.")
        else:
            print(f"Cita con ID {id_cita} no encontrada para el médico {self.nombre}.")
