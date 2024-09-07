# notificacion.py

class Notificacion:
    """
    Clase para gestionar las notificaciones enviadas a los pacientes.
    """

    def __init__(self, mensaje, medio_notificacion):
        """
        Inicializa una nueva notificación.
        :param mensaje: El mensaje de la notificación.
        :param medio_notificacion: El medio de notificación (correo, SMS, etc.).
        """
        self.mensaje = mensaje
        self.medio_notificacion = medio_notificacion

    def enviar(self):
        """Envía la notificación al paciente."""
        print(f"Enviando notificación por {self.medio_notificacion}: {self.mensaje}")
