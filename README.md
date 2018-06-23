# Sistema de registro de personas

Al iniciar el programa se abrirá una ventana de login en el cual se deberá ingresar un usuario con formato de correo electronico (usuario@servidor.extension) y una contraseña de entre 5 y 15 caracteres, con al menos una mayúscula y un número. Los usuarios registrados se encuentran en ```users.txt```. Una vez ingresado el usuario deberá dar click en ingresar para hacer el respectivo login, o también puede presionar en limpiar para poner los campos en blanco.

Una vez haya ingresado se abrirá una ventana con las opciones de registrar nacimiento, mostrar árbol genealógico, certificado de nacimiento y salir; además de marcar la cantidad total de personas registradas (las cuales se guardan en el archivo ```poblacion```). A continuación se detallarán cada una de estas opciones

**1) Registrar Nacimiento:** Esta opción sirve para registrar una nueva persona. Aquí se preguntará el número de cédula, el nombre, los apellidos, el sexo, el distrito, el cantón, la fecha de nacimieto, el padre y la madre (previamente registrados) y sus respectivas nacionalidades. Se deberán llenar todos los campos. Una vez hecho esto se presiona en registrar, lo cuál desplegará un cuadro de dialogo con la confirmación de que se ha registrado la persona. También se encuentra el botón de volver para regresar al menú principal.

**2) Mostrar Árbol Genealógico:** Aquí se muestran los padres de una persona registrada. Para esto deberá seleccionar una persona en el menú desplegable y presionar mostrar lo cual hará que en las caja que están en la parte inferior aparezca la persona escogida junto con sus padres. La opción de limpiar hace que estas cajas vuelvan a su estado inicial y volver regresa al menú principal.

**3) Certificado de Nacimiento:** Se abrirá una ventana en la que puede buscar a una persona por su número de cédula o nombre completo para generar su certificado de nacimiento. Al presionar en alguno de los dos botones de buscar (se debe presionar el botón respectivo al tipo de búsqueda) se generará un archivo HTML en la carpeta actual llamado ```Analisis-dd-mm-aaaa-hh-mm-ss.html``` que contiene el asiento, el tomo, el número de cédula (cita), el nombre (dice que), el sexo, lugar de nacimiento, fecha de nacimento, padre y madre y la nacionalidad de estos últimos. Una vez generado el archivo se abrirá un cuadro de dialogo confirmando la creación del archivo. También se presenta el botón de regresar que vuelve al menú principal.

**4) Salir:** Este botón cierra el programa.
