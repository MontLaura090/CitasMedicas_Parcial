import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.paciente import Paciente

def test_create_paciente():
    paciente = Paciente(1110282881, 'Laura Gabriela Capera Montaño', 'montlaura090@gmail.com','3218679776','Cr 7 norte #72-33 Guaduales')
    assert paciente.cedula == 1110282881
    assert paciente.nombre == 'Laura Gabriela Capera Montaño'
    assert paciente.correo_electronico == 'montlaura090@gmail.com'
    assert paciente.telefono == '3218679776'
    assert paciente.direccion == 'Cr 7 norte #72-33 Guaduales'


