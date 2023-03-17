# Project-Python
# Project in python

[EN]
The Software Projects we worked with in the previous TP are now in a text file called "progetti.csv" (click on the file name to download the compressed file), 
where each piece of data is separated from the next by pipe characters (“|”). The first line of the file contains the headers and should be skipped when processing
the file. Each line in the file is separated from the next with a line break, and each one has the following format:

* username: String representing the username who uploaded the project.
* repository: String representing the name of the repository where it was uploaded.
* description: Description in string format.
* update_date: String representing the date of the last update. It has the format yyyy-mm-dd where there are 4 digits for the year, 2 for the month and 2 for the day separated by hyphens.
* language: String representing the programming language of the project.
* likes: String with a numerical value representing thousands of likes indicated on it.
* tags: A list of words separated by commas.
* url: String representing the URL where the project is stored.
* Develop a program with a menu for the following options:

1.) Load: Load the contents of the file into a vector of project records (define the Project class), where each record has the following fields:

* username: string.
* repository: string.
* update_date: can choose to store it as a string or as a Date record variable that has the day, month and year fields. Note that if you opt for a new record type, each time the date is displayed it must be displayed as a string with the format from the file.
* language: string.
* likes: It must be stored as a floating point value representing thousands of likes. For example, 69.7k should be stored as 69.7.
* tags: vector of strings. To obtain the tag vector, the string in the corresponding column of the text file must be separated by commas. Not all records have tags.
* url: string.

The following rules must be considered when generating the vector from the text file:

The first line of the file contains the field names and therefore should not be taken into account.
The vector must always be sorted by the repository field. Loading all records and sorting them at the end will be considered incorrect.
Repositories should not be repeated.
Lines with blank language should not be processed.
Once the vector is loaded, show the number of records that were loaded and the number of records that were skipped.

2.) Filter by tag: Load a tag (string) by keyboard and, from the projects vector, show all records that contain the tag in one of the vector elements stored
in the tag field. The projects should be displayed at a rate of one record per line showing only the name of the repository, the update date, and the number 
of stars.

Stars represent a range of thousands of likes from the file:

* 1: from 0 to 10k
* 2: from 10.1 to 20k
* 3: from 20.1 to 30k
* 4: from 30.1 to 40k
* 5: greater than 40k

The user must be given the option to store the list in a text file separated by pipes where an initial line with the column (or field) names is written and 
then a line is written for each project record with all its fields (not just the fields shown in the list).

3.) Languages: From the vector, determine the number of projects for each programming language. Show the programming languages and their quantity ordered from 
largest to smallest by quantity.

4.) Popularity: We want to know the months in which projects are updated, according to the number of stars. To do this, we request to generate a matrix from
the vector where each row represents a month of update (no matter what year it corresponds to) and each column represents a quantity of stars. Each cell must
contain the number of projects that have that month of update and that quantity of stars. The stars represent the ranges of likes indicated in point 2.

Show the resulting array as a table of rows and columns. Also indicate the total number of projects updated in month m, where m is a month entered by the user 
(integer value from 1 to 12).

5.) Search for updated project: From the vector, search for a repository with the name "rep", where "rep" is a value entered by the user. If it exists, show 
its data and allow to replace the URL of the project entered by the user and change the update date to the current date (the date is not loaded by the user, 
investigate the way to obtain the current date and format it in the same way as it is in the file). If it does not exist, indicate with an error message.

6.) Save popular: From the matrix generated in point 4, store its content (only elements greater than zero) in a binary file in which each element is represented 
by a record with the following fields:

* Month of the year.
* Stars (the range indicated in point 2).
* Quantity of projects.

7.) Show file: Read the content of the binary file and regenerate the matrix. Show it in table format.

8.) Exit: End program execution.






[ES]
Los Proyectos de Software con los que trabajamos en el TP anterior  ahora se encuentran en un archivo de texto proyectos.csv, (hacer click en el nombre del 
archivo para descargar el archivo comprimido que lo contiene), en el que cada dato se separa del siguientes por caracteres pipe (“|”).  La primera línea del 
archivo contiene los encabezados, y debe ser salteada al procesar el archivo. Cada línea del archivo se separa de la siguiente con un salto de línea, y cada 
una tiene el siguiente formato:


* nombre_usuario: Cadena de caracteres que representa el nombre de usuario que subió el proyecto.
* repositorio: Cadena de caracteres que representa el nombre del repositorio donde fue subido.
* descripcion: Descripción en formato cadena de caracteres
* fecha_actualizacion: Cadena de caracteres que representa la  fecha de última actualización. Tiene el formato aaaa-mm-dd en dónde hay 4 dígitos para el año, dos del mes y dos del día separados por guiones.
* lenguaje: Cadena de caracteres que representa el lenguaje de programación del proyecto.
* likes: Cadena de caracteres que tiene un valor numérico que representa miles de me gusta indicados sobre el mismo.
* tags: Es una lista de palabras separadas por comas.
* url: Cadena de caracteres que representa la URL en la que está almacenado el proyecto.

Se pide desarrollar un programa con menú para las siguientes opciones:

1.) Cargar: Cargar el contenido del archivo en un vector de registros de proyectos (defina la clase Proyecto), donde cada registro tenga los siguientes campos:

* nombre_usuario: cadena de caracteres.
* repositorio: cadena de caracteres.
* fecha_actualizacion: puede optar por almacenarla como una cadena de caracteres o como una variable de tipo registro Fecha que tenga los campos dia, mes y año. Tener en cuenta que si opta por un nuevo tipo de registro, cada vez que se muestre la fecha deberá mostrarse como una cadena de caracteres con el formato del archivo.
* lenguaje: cadena de caracteres.
* likes: Se debe almacenar como un valor numérico con punto flotante representando los miles de me gusta. Por ejemplo 69.7k debe almacenarse como 69.7.
* tags: vector de cadenas de caracteres. Para obtener el vector de tags se debe separar la cadena que se encuentra en la columna correspondiente del archivo de texto por comas. No todos los registros tienen tags.
* url: cadena de caracteres.

Deben considerarse las siguientes reglas al generar el vector a partir del archivo de texto:

La primera línea del archivo contiene el nombre de los campos y por lo tanto no debe ser tenida en cuenta.
El vector debe mantenerse siempre ordenado por el campo repositorio. Se considerará incorrecta la solución de cargar todos los registros y ordenarlos al final.
No deben repetirse los repositorios.
Las líneas que tengan el lenguaje en blanco no deben ser procesadas.
Una vez finalizada la carga del vector, mostrar la cantidad de registros que se cargaron y la cantidad de registros que se omitieron.

2.) Filtrar por tag: Cargar por teclado un tag (cadena de caracteres) y a partir del vector de proyectos, mostrar todos aquellos registros que contengan al tag 
en alguno de los elementos del vector alojado en el campo tag. Los proyectos deben mostrarse a razón de un registro por línea mostrando solamente el nombre del 
repositorio, la fecha de actualización y  cantidad de estrellas.

Las estrellas representan un rango de miles de likes del archivo:

* 1: de 0 a 10 k
* 2: de 10.1 a 20 k
* 3: de 20.1 a 30 k
* 4: de 30.1 a 40 k
* 5: mayor a 40 k

Se debe dar al usuario la opción de almacenar el listado en un archivo de texto separado por pipes donde se escriba una línea inicial con el nombre de las 
columnas (o campos) y luego una línea por cada registro de proyecto con todos sus campos (no solo los campos que se mostraron en el listado).

3.) Lenguajes: A partir del vector determinar la cantidad de proyectos por cada lenguaje de programación. Mostrar los lenguajes de programación y su cantidad 
ordenados de mayor a menor por cantidad.

4.) Popularidad: Se quiere conocer los meses en los que se actualizan los proyectos, de acuerdo a la cantidad de estrellas. Para ello se pide, a partir del 
vector, generar una matriz donde cada fila sea un mes de actualización (no importa de qué año corresponde)  y cada columna una cantidad de estrellas. Cada 
celda deberá contener la cantidad de proyectos que tengan ese mes de actualización y esa cantidad de estrellas. Las estrellas representan los rangos de likes 
indicados en el punto 2.

Mostrar la matriz resultante como una tabla de filas y columnas. Indique, además, cuál es el total de proyectos actualizados en el mes m, siendo m un mes que 
se ingresa por teclado (valor entero del 1 al 12).

5.) Buscar proyecto actualizado: A partir del vector, buscar un repositorio con el nombre rep, siendo rep  un valor ingresado por teclado. Si existe mostrar 
sus datos y permitir reemplazar la URL del proyecto que se ingrese por teclado  y cambiar la fecha de actualización por la fecha actual (la fecha no se carga 
por teclado, investigue la manera de obtener la fecha actual y formatearla de igual manera en la que se encuentra en el archivo. Si no existe indicar con un 
mensaje de error.

6.) Guardar populares: A partir de la matriz generada en el punto 4, almacenar su contenido (sólo los elementos mayores a cero) en un archivo binario en el 
que cada elemento sea un registro en el que se representen los campos:

* mes del año.
* estrellas (El rango indicado en el punto 2).
* cantidad de proyectos.

7.) Mostrar archivo: Leer el contenido del archivo binario y volver a generar la matriz. Mostrarla en formato de tabla.

8.) Salir: Finaliza la ejecución del programa.
