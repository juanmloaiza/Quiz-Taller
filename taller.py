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