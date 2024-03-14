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