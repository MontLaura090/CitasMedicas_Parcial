# horario.py
from datetime import time

class Horario:
    """
    Clase que representa un horario de disponibilidad para un médico.
    """

    def __init__(self, id_horario, dia, hora_inicio, hora_fin, id_medico):
        """
        Inicializa un nuevo horario.
        :param id_horario: ID del horario.
        :param dia: Día de la semana.
        :param hora_inicio: Hora de inicio.
        :param hora_fin: Hora de finalización.
        :param id_medico: ID del médico asociado.
        """
        self.id_horario = id_horario
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.id_medico = id_medico

    def disponible(self, fecha):
        """
        Verifica si el médico está disponible en la fecha dada.
        :param fecha: Fecha a verificar.
        :return: True si está disponible, False si no.
        """
        if fecha.weekday() == self.dia:
            if self.hora_inicio <= fecha.time() <= self.hora_fin:
                return True
        return False
