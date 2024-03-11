Uso de Sphinx Linux
Para instalar Sphinx en Linux pycharm sirve con instalar la dependencia correcta en el proyecto. Sirve con buscar sphinx.

Antes de Usarlo
Desde una terminal aparte se debe de ir a la ruta del proyecto y usar:

source venv/bin/activate

Para activar la terminal usando el entorno virtual.

O abrir una terminal en pycharm, lo que hara que automaticamente haga lo anterior.

Su configuración
Desde la misma terminal anterior Usar los siguientes comandos.

sphinx-quickstart

En los pasos se debe de elegir si quieres separa la creacion de los archivos, y seguir de forma natural, cuando llegues a la parte de algo de modulos y no entiendes bien dale a enter y lo dejar vacio.

Luego de esto se debe de configurar el archivo conf.py de la carpeta source creada al separarlo en en paso previo, para que tenga la siguiente configuración:

añadir import os al inicio del archivo.

añadir import sys al inicio del archivo.

añadir sys.path.insert(0, os.path.abspath('.')) al inicio del archivo. Para poder obtener la posición del archivo.

añadir extensions = ['sphinx.ext.autodoc'] al inicio del archivo.

En la carpeta de source se configurara el archivo index.rst para que tenga la siguiente configuración:

entre los dos puntos de la primera linea añadir debajo los nombres de las clases que quieres hacer su documentación, en mi caso es funciones y conexionBD

Indexación
Para hacer una especie de indixacion se usa el siguiente comando

sphinx-apidoc -o source ./source

Tener en cuenta que siempre que se agregue algun archivo o alteracion en el index o config se debe de volver a hacer la indexacion.

Creación de Archivos
Para se que creen los archivos se usa el siguiente comando

sphinx-build source build
