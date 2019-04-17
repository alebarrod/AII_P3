# P3 para AII por alebarrod

Enunciado de la práctica del Departamento de Lenguajes y Sistemas (LSI) de la Universidad de Sevilla (http://www.lsi.us.es/docencia/pagina_asignatura.php?id=119&cur=2018):

"Se desea hacer un buscador sobre los distintos estrenos de cine en España. Mediante Beautifulsoup
extraeremos la información de la página:
https://www.elseptimoarte.net/estrenos/
SÓLO ALMACENAR LAS PELÍCULAS DE ESTRENOS DE LA PRIMERA PÁGINA.
Buscamos construir un programa en Tkinter con un MENÚ con tres opciones:
a) “Datos”, con dos opciones:
a. “Cargar”, que sea capaz de extraer y almacenar en una base de datos SQLite los
siguientes datos de cada estreno: título, título original, país, fecha de estreno en España,
director y género/s. Una vez cargados, que muestre una ventana de mensajes informando
del número de estrenos almacenadas en la BD.
b. “Salir”, que cierre la ventana principal.
b) “Buscar”, con dos opciones:
a. “Título”, que muestre una ventana con un entry que permita al usuario introducir
una palabra y muestre en otra ventana (con una listbox con scrollbar) todas las
películas (título, país y director) que hay en la BD que contengan dicha palabra en su
título.
b. “Fecha”, que muestre una ventana con un entry que permita al usuario introducir
una fecha (en formato dd-mm-aaaa) y muestre en otra ventana (con una listbox con
scrollbar) todas las películas (título y fecha de estreno) que hay en la BD posteriores a
dicha fecha.
c) “Películas por género”, que muestre una ventana con una spinbox que permita al usuario
seleccionar un género de los que hay en la BD, y muestre en otra ventana (con una listbox con
scrollbar) todas las películas (título y fecha de estreno) que hay en la BD de ese género. 
"

## Requisitos

Tener instalado Python 3 (el desarrollo se realizó bajo Python 3.6) Tener instalado BeautifulSoup4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## Ejecución

Para ejecutar la aplicación unicamente debemos abrir una consola e ir al directorio en el que se encuentre scrapApp.py y ejecutar este archivo con Python. La funcionalidad de la aplicación está explicada en el enunciado de la práctica.

## !Importante!

El web scraping se basa en aprovechar la estructura de la web para extraer la información publicada en esta de forma automática. Por ello si la web actualiza su estructura el programa no funcionará y tendrá que readaptarse.