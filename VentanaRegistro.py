#Creado por: Gerardo, Triveth, Abraham
#Fecha de creación: 14/6/2018
#Última modificaciónÑ 14/6/2018
#Versión 3.4.6

""" Añadir estas dos a la GUI, ahí le ponen pegamento con todo lo demás xD
    def crearListaDesplegable(self, objeto, lista, coordenadas = (0,0)):
        '''
        Entradas: objeto tipo objeto, una lista de strings y coordenadas
        Salidas: Crea y retorna una lista desplegable
        Funcionamiento: Crea una lista desplegable donde cada opcion son los
        elementos de la lista
        '''
        combo = QComboBox(self)
        for elem in lista:
            combo.addItem(str(elem))
        combo.resize(200,30)
        combo.move(coordenadas[0], coordenadas[1])
        return combo

    def crearRadioBoton(self, objeto, texto = '', coordenadas = (0,0)):
        btn = QRadioButton(objeto, text = texto)
        btn.move(coordenadas[0],coordenadas[1])
        return btn
        """

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GUI import Widgets
from Clases import *

import sys
import time

class VentanaNuevaPersona(QMainWindow, Widgets):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de nacimiento")
        self.setGeometry(650,150,500,800)

        titulo = self.crearLabel(self, nombre="Datos Nueva Persona", coordenadas = (160,10), tamano = (210,15) )
        titulo.setStyleSheet("font-weight: bold")
        self.crearLabel(self, nombre = "Cita:", coordenadas = (30,50), tamano = (125,15))
        self.crearLabel(self, nombre = "-", coordenadas = (180,50), tamano = (125,15))
        self.crearLabel(self, nombre = "-", coordenadas = (245,50), tamano = (125,15))
        self.crearLabel(self, nombre = "Nombre:", coordenadas = (30,100), tamano = (125,15))
        self.crearLabel(self, nombre = "Apellido:", coordenadas = (30,150), tamano = (125,20))
        self.crearLabel(self, nombre = "Sexo:", coordenadas = (30,200), tamano = (125,15))
        self.crearLabel(self, nombre = "Distrito:", coordenadas = (30,250), tamano = (125,15))
        self.crearLabel(self, nombre = "Cantón:", coordenadas = (30,300), tamano = (125,15))
        self.crearLabel(self, nombre = "Provincia:", coordenadas = (30,350), tamano = (125,15))
        self.crearLabel(self, nombre = "Día:", coordenadas = (30,400), tamano = (125,15))
        self.crearLabel(self, nombre = "Mes:", coordenadas = (30,450), tamano = (125,15))
        self.crearLabel(self, nombre = "Año:", coordenadas = (30,500), tamano = (125,15))
        self.crearLabel(self, nombre = "Padre:", coordenadas = (30,550), tamano = (125,15))
        self.crearLabel(self, nombre = "Nacionalidad:", coordenadas = (30,600), tamano = (125,15))
        self.crearLabel(self, nombre = "Madre:", coordenadas = (30,650), tamano = (125,15))
        self.crearLabel(self, nombre = "Nacionalidad:", coordenadas = (30,700), tamano = (125,15))
        
        self.errorLabel = self.crearLabel(self, nombre = "", coordenadas = (30,740), tamano = (2000, 30), fuente = (None,5))
        self.errorLabel.setStyleSheet('color: red')
        
        self.cita1 = self.crearEntrada(self, coordenadas = (150,50), tamano = (20,20))
        self.cita2 = self.crearEntrada(self, coordenadas = (200,50), tamano = (35,20))
        self.cita3 = self.crearEntrada(self, coordenadas = (265,50), tamano = (40,20))
        self.entradaNombre = self.crearEntrada(self, coordenadas = (150,100), tamano = (310,20))
        self.entradaApellido = self.crearEntrada(self, coordenadas = (150,150), tamano = (310,20))
        self.entradaDistrito = self.crearEntrada(self, coordenadas = (150,250), tamano = (310,20))
        self.entradaCanton = self.crearEntrada(self, coordenadas = (150,300), tamano = (310,20))
        self.entradaProvincia = self.crearEntrada(self, coordenadas = (150, 350), tamano = (310,20))
        self.entradaPadre = self.crearEntrada(self, coordenadas = (150,550), tamano = (310,20))
        self.entradaMadre = self.crearEntrada(self, coordenadas = (150,650), tamano = (310,20))
        self.cita1.textChanged.connect(self.actualizarProvincia)
        self.entradaProvincia.setReadOnly(True)
        
        self.sexoM = self.crearRadioBoton(self, texto = 'Hombre', coordenadas = (150,190))
        self.sexoF = self.crearRadioBoton(self, texto = 'Mujer', coordenadas = (300, 190))
        
        nacionalidades = ['-','Afgano','Alemán/a','Árabe','Argentino/a','Australiano/a','Belga','Boliviano/a','Brasileño/a','Camboyano/a','Canadiense','Chileno/a','Chino/a','Colombiano/a','Coreano/a','Costarricense','Cubano/a','Danés/a','Ecuatoriano/a','Egipcio/a','Salvadoreño/a','Escocés/a','Español/a','Estadounidense','Estonio/a','Etiope','Filipino','Finlandés/a','Francés/a','Galés/a','Griego/a','Guatemanteco/a','Haitiano/a','Holandés/a','Hondureño/a','Indonés/a','Inglés/a','Iraquí','Iraní','Irlandés/a','Israelí','Italiano/a','Japonés/a','Jordano/a','Laosiano/a','Letón/a','Malayo/a','Marroquí','Mexicano/a','Nicaragüense','Noruego/a','Neozelandés/a','Panameño/a','Paraguayo/a','Peruano/a','Polaco/a','Portugués/a','Puertorriqueño/a','Dominicano/a','Rumano/a','Ruso/a','Sueco/a','Suizo/a','Tailandés/a','Taiwanés/a','Turco/a','Ucraniano/a','Uruguayo/a','Venezolano/a','Vietnamita']
        calendario = [['-','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],['-','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],[]]
        for i in range(1899,int(time.strftime("%Y"))):
            calendario[2].append(str(i+1))
        calendario[2].append('-')
        calendario[2] = calendario[2][::-1]
        self.dias = self.crearListaDesplegable(self, calendario[0], coordenadas = (200,395))
        self.meses = self.crearListaDesplegable(self, calendario[1], coordenadas = (200,445))
        self.annos = self.crearListaDesplegable(self, calendario[2], coordenadas = (200,495))
        self.nacionalidadPadre = self.crearListaDesplegable(self,nacionalidades, coordenadas = (200,595))
        self.nacionalidadMadre = self.crearListaDesplegable(self,nacionalidades, coordenadas = (200,695))
        
        self.botonRegistrar = self.crearBoton(self, 'registrar', nombre = 'Volver', coordenadas = (200,750),tamano = (100,30))
        self.botonRegresar = self.crearBoton(self, 'volver', nombre = 'Registrar', coordenadas = (320,750),tamano = (100,30))

        self.show()

    def actualizarProvincia(self):
        self.entradaProvincia.setText(self.obtenerProvincia())
        
    def validaciones(self, lista):
        if lista[0] == 'n':
            self.errorLabel.setText("--- Error: Debe ingresar solo\n valores numéricos en la cédula ---")
            return False
        if lista[0] == 'l':
            self.errorLabel.setText("--- Error: Revise la cédula ---")
            return False
        if not (lista[1] and lista[2] and lista[3] and lista[4] and lista[5] and lista[10] and lista[12]):
            self.errorLabel.setText("--- Error: Debe rellenar todos\n los campos ---")
            return False
        if not (palabras(lista[1]) and palabras(lista[2]) and palabras(lista[4]) and palabras(lista[5]) and palabras(lista[10]) and palabras(lista[12])):
            self.errorLabel.setText("--- Error: Use solo letras para\n nombres y apellidos ---")
            return False
        for elem in lista[7:10]+[lista[11]]+[lista[13]]:
            if elem == '-':
                self.errorLabel.setText("--- Error: Debe rellenar todos\n los campos ---")
                return False
        if not existeFecha(lista[7:10]):
            self.errorLabel.setText("--- Error: La fecha que ingresó\nno existe ---")
            return False
        return True

    def obtenerCedula(self):
        c1 = self.cita1.text()
        c2 = self.cita2.text()
        c3 = self.cita3.text()
        if not (c1.isnumeric() and c2.isnumeric() and c3.isnumeric()):
            return 'n'
        if len(c1)!=1:
            return 'l'
        if len(c2) != 3 and len(c2) != 4:
            return 'l'
        if len(c3) != 3 and len(c3) != 4:
            return 'l'
        if len(c2) == 3:
            c2 = '0'+c2
        if len(c3) == 3:
            c3 = '0'+c3
        return c1+'-'+c2+'-'+c3

    def obtenerProvincia(self):
        t = self.cita1.text()
        if t == '1':
            return "San José"
        if t == '2':
            return "Alajuela"
        if t == '3':
            return "Cartago"
        if t == '4':
            return "Heredia"
        if t == '5':
            return "Guanacaste"
        if t == '6':
            return "Puntarenas"
        if t == '7':
            return "Limón"
        if t == '8':
            return "PEN"
        if t == '9':
            return "Nacionalizado"
        return ''
        
    def registrar(self):
        cedula = self.obtenerCedula()
        nombre = self.entradaNombre.text()
        apellido = self.entradaApellido.text()
        sexo = 'M' if self.sexoM.isChecked() else ('F' if self.sexoF.isChecked() else '')
        distrito = self.entradaDistrito.text()
        canton = self.entradaCanton.text()
        provincia = self.obtenerProvincia()
        dia = self.dias.currentText()
        mes = self.meses.currentText()
        anno = self.annos.currentText()
        nacPadre = self.nacionalidadPadre.currentText()
        pa = self.entradaPadre.text()
        ma = self.entradaMadre.text()
        nacMadre = self.nacionalidadMadre.currentText()
        info = [cedula, nombre, apellido, sexo, distrito, canton, provincia, dia, mes, anno, pa, nacPadre, ma, nacMadre]
        print(info)
        if not self.validaciones(info):
            return
        nuevoCiudadano = Persona()
        nuevoCiudadano.setCedula(cedula)
        nuevoCiudadano.setNombre(nombre)
        nuevoCiudadano.setSexo(sexo)
        nuevoCiudadano.setUbicacion(provincia+', '+canton+', '+distrito)
        nuevoCiudadano.setFechanacimiento(dia+'/'+mes+'/'+anno)
        nuevoCiudadano.setPadre(pa)
        nuevoCiudadano.setNacionalidadpadre(nacPadre)
        nuevoCiudadano.setMadre(ma)
        nuevoCiudadano.setNacionalidadmadre(nacMadre)
        
        
    def volver(self):
        pass


def palabras(p):
    for elem in p.split():
        if not elem.isalpha():
            return False
    return True     
    
def divisible(n1, n2):
    """
    Entradas: Dos intigers
    Salidas: Un booleano.
    Funcionalidad: Indica s n1 es divisible por n2
    """
    if n1%n2 == 0:
        return True
    return False

def annoBisiesto(a):
    """
    Entradas: Un año como int
    Salidas: Un booleano
    Funcionalidad: Detecta si un año es bisiesto o no
    """
    if divisible(a,4) and ((not divisible(a,100)) or divisible(a,400)):
        return True
    return False

def existeFecha(lista):
    """
    Entradas: Una fecha como lista en formato [d, m, a]
    Salidas: Un booleano
    Funcionalidad: Detecta si una fecha existe o no
    """
    dia = lista[0]
    mes = lista[1]
    anno = lista[2] 
    if mes == '2':
        if int(dia)>29 or (dia == '29' and not annoBisiesto(int(anno))):
            return False
    if (mes == '4' or mes == '6' or mes == '9' or mes == '11') and dia == '31':
        return False
    return True

pedro = QApplication(sys.argv)
hola = VentanaNuevaPersona()
sys.exit(pedro.exec_())
