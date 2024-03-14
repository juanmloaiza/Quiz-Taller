#inico del codigo
class ImplanteMedico:
    def __init__(self, material, tipo_fijacion):
        self._material = material
        self._tipo_fijacion = tipo_fijacion
        self._paciente = None
        self._fecha_implantacion = None
        self._medico_responsable = None
        self._estado_implante = None
        self._fechas_revision = []
    
    def get_material(self):
        return self._material

    def set_material(self, material):
        self._material = material

    def get_tipo_fijacion(self):
        return self._tipo_fijacion

    def set_tipo_fijacion(self, tipo_fijacion):
        self._tipo_fijacion = tipo_fijacion

    def asignar_paciente(self, paciente, fecha_implantacion, medico_responsable, estado_implante):
        self._paciente = paciente
        self._fecha_implantacion = fecha_implantacion
        self._medico_responsable = medico_responsable
        self._estado_implante = estado_implante

    def obtener_seguimiento(self):
        return {
            'Paciente': self._paciente,
            'Fecha de Implantación': self._fecha_implantacion,
            'Médico Responsable': self._medico_responsable,
            'Estado del Implante': self._estado_implante,
            'Fechas de Revisión': self._fechas_revision if self._fechas_revision else "No hay fechas de revisión"
        }

    def agregar_revision(self, fecha_revision):
        self._fechas_revision.append(fecha_revision)

class ProtesisCadera(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamaño):
        super().__init__(material, tipo_fijacion)
        self._tamaño = tamaño
    
    def get_tamaño(self):
        return self._tamaño

    def set_tamaño(self, tamaño):
        self._tamaño = tamaño

class Marcapasos(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, num_electrodos, inalambrico, frecuencia_estimulacion):
        super().__init__(material, tipo_fijacion)
        self._num_electrodos = num_electrodos
        self._inalambrico = inalambrico
        self._frecuencia_estimulacion = frecuencia_estimulacion
    def get_num_electrodos(self):
        return self._num_electrodos

    def set_num_electrodos(self, num_electrodos):
        self._num_electrodos = num_electrodos

    def get_inalambrico(self):
        return self._inalambrico

    def set_inalambrico(self, inalambrico):
        self._inalambrico = inalambrico

    def get_frecuencia_estimulacion(self):
        return self._frecuencia_estimulacion

    def set_frecuencia_estimulacion(self, frecuencia_estimulacion):
        self._frecuencia_estimulacion = frecuencia_estimulacion

class StentCoronario(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, longitud, diametro):
        super().__init__(material, tipo_fijacion)
        self._longitud = longitud
        self._diametro = diametro
    def get_longitud(self):
        return self._longitud

    def set_longitud(self, longitud):
        self._longitud = longitud

    def get_diametro(self):
        return self._diametro

    def set_diametro(self, diametro):
        self._diametro = diametro

class ImplanteDental(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, forma):
        super().__init__(material, tipo_fijacion)
        self._forma = forma

    def get_forma(self):
        return self._forma

    def set_forma(self, forma):
        self._forma = forma