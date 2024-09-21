import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from app.medico import Medico
from app.cita import Cita
def test_confirmar_cita_disponible():
    medico = Medico(1, 'Laura Gabriela Capera Montaño', 'pediatra')
    fecha_inicio = datetime(2023, 9, 25, 10, 0)
    fecha_fin = datetime(2023, 9, 25, 12, 0)
    medico.actualizar_disponibilidad(fecha_inicio, fecha_fin)

    # Crear una cita dentro del horario disponible
    cita = Cita(1, datetime(2023, 9, 25, 11, 0), '123456789', medico.id_medico, 'Chequeo general')
    assert medico.verificar_disponibilidad(cita.fecha)
    cita.confirmar_cita()
    assert cita.estado == 'Confirmada'

def test_confirmar_cita_no_disponible():
    medico = Medico(1, 'Laura Gabriela Capera Montaño', 'pediatra')
    fecha_inicio = datetime(2023, 9, 25, 10, 0)
    fecha_fin = datetime(2023, 9, 25, 12, 0)
    medico.actualizar_disponibilidad(fecha_inicio, fecha_fin)

    # Crear una cita fuera del horario disponible
    cita = Cita(2, datetime(2023, 9, 25, 13, 0), '987654321', medico.id_medico, 'Consulta de rutina')
    assert not medico.verificar_disponibilidad(cita.fecha)
    cita.confirmar_cita()
    assert cita.estado == 'Pendiente'



def test_consulta_citas():
    # Crear un médico
    medico = Medico(1, 'Laura Gabriela Capera Montaño', 'pediatra')

    # Información de la cita
    id_cita = 1
    fecha_cita = datetime(2023, 9, 25, 11, 0)
    cedula_paciente = '123456789'
    detalle_cita = 'Chequeo general'

    cita = Cita(id_cita, fecha_cita, cedula_paciente, medico.id_medico, detalle_cita)
    cita.confirmar_cita(medico)  

    
    consulta_resultado = {
        'fecha': cita.fecha,
        'detalle': cita.detalle
    }
    assert consulta_resultado['fecha'] == fecha_cita
    assert consulta_resultado['detalle'] == detalle_cita
