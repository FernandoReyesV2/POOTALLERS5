listaUsuario = []
listaCargo = []
listaDepartamentos = []
listaSistema = []
listaOperaciones = []
class Empresa:
    def __init__(self, idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones):
        # USUARIO INFO
        self.idusuario = idusuario
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.idcargo = idcargo #CARGO - USUARIO
        # CARGO
        self.descCargo = descCargo
        self.idDepto = idDepto #DEPTO - CARGO
        # DEPTO
        self.descDepto = descDepto
        self.pisoDepto = pisoDepto
        # SISTEMA
        self.idSistema = idSistema # OPERACIONES - SISTEMA
        self.descSistema = descSistema
        self.acronimoS = acronimoS
        # OPERACIONES
        self.idOperaciones = idOperaciones
        self.descOperaciones = descOperaciones
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Usuario(Empresa):
    def __init__(self, idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones):
        super().__init__(idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones)
    

    def AgregarUsuario(self):
        listaUsuario.append(self.idusuario)
        listaUsuario.append(self.nombre)
        listaUsuario.append(self.apellido)
        listaUsuario.append(self.telefono)
        listaUsuario.append(self.idcargo)
        listaUsuario.append(self.descCargo)
        return listaUsuario
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Cargo(Empresa):
    def __init__(self, idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones):
        super().__init__(idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones)

    def AgregarCargo(self):
        listaCargo.append(self.idcargo)
        listaCargo.append(self.descCargo)
        listaCargo.append(self.idDepto)
        listaCargo.append(self.descDepto)
        return listaCargo
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Depto(Empresa):
    def __init__(self, idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones):
        super().__init__(idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones)

    def AgregarDepto(self):
        listaDepartamentos.append(self.idDepto)
        listaDepartamentos.append(self.descDepto)
        listaDepartamentos.append(self.pisoDepto)
        return listaDepartamentos
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Sistema(Empresa):
    def __init__(self, idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones):
        super().__init__(idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones)

    def AgregarSistema(self):
        listaSistema.append(self.idSistema)
        listaSistema.append(self.descSistema)
        listaSistema.append(self.acronimoS)
        return listaSistema
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Operaciones(Empresa):
    def __init__(self, idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones):
        super().__init__(idusuario, nombre, apellido, telefono, idcargo, descCargo, idDepto, descDepto, pisoDepto, idSistema, descSistema, acronimoS, idOperaciones, descOperaciones)

    def AgregarOperaciones(self):
        listaOperaciones.append(self.idOperaciones)
        listaOperaciones.append(self.descOperaciones)
        listaOperaciones.append(self.idSistema)
        listaOperaciones.append(self.descSistema)
        return listaOperaciones
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
usu = Usuario(1,"Fernando","Reyes", 9845882, 1,"Programador",1,"TICS",3,1,"Contable","CTBLE",1,"Proveedores")
print("Usuario: ", usu.AgregarUsuario())
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
car = Cargo(1,"Fernando","Reyes", 9845882, 1,"Programador",1,"TICS",3,1,"Contable","CTBLE",1,"Proveedores")
print("Cargo: ", car.AgregarCargo())
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
dep = Depto(1,"Fernando","Reyes", 9845882, 1,"Programador",1,"TICS",3,1,"Contable","CTBLE",1,"Proveedores")
print("Depto: ",dep.AgregarDepto())
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sis = Sistema(1,"Fernando","Reyes", 9845882, 1,"Programador",1,"TICS",3,1,"Contable","CTBLE",1,"Proveedores")
print("Sistema :",sis.AgregarSistema())
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ope = Operaciones(1,"Fernando","Reyes", 9845882, 1,"Programador",1,"TICS",3,1,"Contable","CTBLE",1,"Proveedores")
print("Operaciones: ",ope.AgregarOperaciones())