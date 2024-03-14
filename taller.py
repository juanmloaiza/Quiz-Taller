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
        
class ProtesisRodilla(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamaño):
        super().__init__(material, tipo_fijacion)
        self._tamaño = tamaño

    def get_tamaño(self):
        return self._tamaño

    def set_tamaño(self, tamaño):
        self._tamaño = tamaño
        
class SistemaGestionImplantes:
    def __init__(self):
        self.implantes = []

    def agregar_implante(self, implante):
        self.implantes.append(implante)

    def eliminar_implante(self, indice):
        del self.implantes[indice]

    def editar_implante(self, indice, nuevo_implante):
        self.implantes[indice] = nuevo_implante

    def mostrar_inventario(self):
        for i, implante in enumerate(self.implantes):
            print("Implante", i + 1)
            print("Material:", implante.get_material())
            print("Tipo de Fijación:", implante.get_tipo_fijacion())
            seguimiento = implante.obtener_seguimiento()
            print("Paciente:", seguimiento['Paciente'])
            print("Fecha de Implante:", seguimiento['Fecha de Implantación'])
            print("Médico Responsable:", seguimiento['Médico Responsable'])
            print("Estado del Implante:", seguimiento['Estado del Implante'])
            print("Fechas de Revisión:", seguimiento['Fechas de Revisión'])
            print("")
def agregar_implante_menu():
    print("""Agregar Nuevo Implante:
    1. Prótesis de Cadera
    2. Marcapasos
    3. Stent Coronario
    4. Implante Dental
    5. Prótesis de Rodilla
    >>""")
    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        material = input("Ingrese el material: ")
        tipo_fijacion = input("Ingrese el tipo de fijación: ")
        tamaño = input("Ingrese el tamaño: ")
        return ProtesisCadera(material, tipo_fijacion, tamaño)

    elif opcion == "2":
        material = input("Ingrese el material: ")
        tipo_fijacion = input("Ingrese el tipo de fijación: ")
        num_electrodos = input("Ingrese el número de electrodos: ")
        inalambrico = input("¿Es inalámbrico? (Sí/No): ")
        frecuencia_estimulacion = input("Ingrese la frecuencia de estimulación: ")
        return Marcapasos(material, tipo_fijacion, num_electrodos, inalambrico, frecuencia_estimulacion)

    elif opcion == "3":
        material = input("Ingrese el material: ")
        tipo_fijacion = input("Ingrese el tipo de fijación: ")
        longitud = input("Ingrese la longitud: ")
        diametro = input("Ingrese el diámetro: ")
        return StentCoronario(material, tipo_fijacion, longitud, diametro)

    elif opcion == "4":
        material = input("Ingrese el material: ")
        tipo_fijacion = input("Ingrese el tipo de fijación: ")
        forma = input("Ingrese la forma: ")
        return ImplanteDental(material, tipo_fijacion, forma)

    elif opcion == "5":
        material = input("Ingrese el material: ")
        tipo_fijacion = input("Ingrese el tipo de fijación: ")
        tamaño = input("Ingrese el tamaño: ")
        return ProtesisRodilla(material, tipo_fijacion, tamaño)

    else:
        print("Opción inválida")
        
def main():
    sistema = SistemaGestionImplantes()

    while True:
        print("""Menú Principal:
        1. Agregar Implante
        2. Eliminar Implante
        3. Editar Implante
        4. Mostrar Inventario
        5. Salir
        >>""")
        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            nuevo_implante = agregar_implante_menu()
            sistema.agregar_implante(nuevo_implante)

            paciente = input("Ingrese el nombre del paciente: ")
            fecha_implantacion = input("Ingrese la fecha de implantación (YYYY-MM-DD): ")
            medico_responsable = input("Ingrese el nombre del médico responsable: ")
            estado_implante = input("Ingrese el estado del implante: ")
            nuevo_implante.asignar_paciente(paciente, fecha_implantacion, medico_responsable, estado_implante)

            while True:
                opcion_revision = input("¿Desea agregar una fecha de revisión? (Sí/No): ")
                if opcion_revision.lower() == "si":
                    fecha_revision = input("Ingrese la fecha de revisión (YYYY-MM-DD): ")
                    nuevo_implante.agregar_revision(fecha_revision)
                    break
                elif opcion_revision.lower() == "no":
                    break
                else:
                    print("Opción inválida. Por favor, ingrese 'Sí' o 'No'.")
                    
        elif opcion == "2":
            indice = int(input("Ingrese el índice del implante a eliminar: ")) - 1
            sistema.eliminar_implante(indice)

        elif opcion == "3":
            indice = int(input("Ingrese el índice del implante a editar: ")) - 1
            implante_editar = sistema.implantes[indice]
            nuevo_implante = agregar_implante_menu()
            nuevo_implante.asignar_paciente(implante_editar._paciente, implante_editar._fecha_implantacion, implante_editar._medico_responsable, implante_editar._estado_implante)
            sistema.editar_implante(indice, nuevo_implante)