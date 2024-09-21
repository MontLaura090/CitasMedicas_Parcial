import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.medico import Medico

def test_create_medico():
    medico = Medico(1, 'Laura Gabriela Capera Montaño', 'pediatra')
    assert medico.id_medico == 1
    assert medico.nombre == 'Laura Gabriela Capera Montaño'
    assert medico.especialidad == 'pediatra'
   





from datetime import datetime

def test_actualizar_disponibilidad():
    medico = Medico(1, 'Laura Gabriela Capera Montaño', 'pediatra')
    fecha_inicio = datetime(2023, 9, 25, 10, 0)
    fecha_fin = datetime(2023, 9, 25, 12, 0)

    medico.actualizar_disponibilidad(fecha_inicio, fecha_fin)

    assert len(medico.horarios_disponibles) == 1
    assert medico.horarios_disponibles[0] == (fecha_inicio, fecha_fin)

def test_verificar_disponibilidad_disponible():
    medico = Medico(1, 'Laura Gabriela Capera Montaño', 'pediatra')
    fecha_inicio = datetime(2023, 9, 25, 10, 0)
    fecha_fin = datetime(2023, 9, 25, 12, 0)
    medico.actualizar_disponibilidad(fecha_inicio, fecha_fin)

    assert medico.verificar_disponibilidad(datetime(2023, 9, 25, 11, 0)) is True

def test_verificar_disponibilidad_no_disponible():
    medico = Medico(1, 'Laura Gabriela Capera Montaño', 'pediatra')
    fecha_inicio = datetime(2023, 9, 25, 10, 0)
    fecha_fin = datetime(2023, 9, 25, 12, 0)
    medico.actualizar_disponibilidad(fecha_inicio, fecha_fin)

    assert medico.verificar_disponibilidad(datetime(2023, 9, 25, 9, 0)) is False

def test_mostrar_disponibilidad():
    medico = Medico(1, 'Laura Gabriela Capera Montaño', 'pediatra')
    
    # Inicialmente no debe tener horarios
    assert len(medico.horarios_disponibles) == 0

    # Agregar disponibilidad
    medico.actualizar_disponibilidad(datetime(2023, 9, 25, 10, 0), datetime(2023, 9, 25, 12, 0))
    
    # Debe tener un horario ahora
    assert len(medico.horarios_disponibles) == 1
