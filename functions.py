from class_project import *

import os.path
import os
import pickle


# ======================================================================================================
#                                       OPCION 1 FUNCIONES                                             #
# ======================================================================================================
def validar_repositorio_proyecto_op1(gProyecto, repository_to_comp):
    # Function to validate that repositories are not repeated.
    for i in gProyecto:
        if i.repository == repository_to_comp:
            return True
    return False


def add_in_order_op1(gProject, project_to_add):
    # Function Add In Order For Binary Search
    izq, der = 0, len(gProject) - 1
    pos = len(gProject)
    while izq <= der:
        c = (izq + der) // 2
        # Using .lower() to compare regardless of whether the beginning of the repositories is lowercase or uppercase
        if project_to_add.repository.lower() == gProject[c].repository.lower():
            pos = c
            break
        elif project_to_add.repository.lower() < gProject[c].repository.lower():
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq

    # I take advantage to create the counters to return 1 or 0 using the repository validation function. This will
    # create an accumulator in the previous 'for' loop that I can eventually use
    count_proj_valid = 0
    count_proj_invalid = 0

    repository_to_comp = project_to_add.repository
    if validar_repositorio_proyecto_op1(gProject, repository_to_comp) or len(project_to_add.lang) == 0:
        count_proj_invalid += 1
    else:
        gProject[pos:pos] = [project_to_add]
        count_proj_valid += 1

    return count_proj_valid, count_proj_invalid


def leer_csv_op1(fd, gProyecto):
    # Counters to be returned that the option 1 requests
    g_count_proj_valid = 0
    g_count_proj_invalid = 0
    # Bool to skip the first line of the file
    first_line = True

    if os.path.exists(fd):
        m = open(fd, mode="rt", encoding="utf8")
        for linea in m:
            if first_line:
                first_line = False
            else:
                ArregloProyect = csv_to_Proyecto(linea)
                # En esta funcion sumo los 0 ó 1 segun corresponda para los registros cargados.
                # Además de utilizar el add_in_order
                count_proj_valid, count_proj_invalid = add_in_order_op1(gProyecto, ArregloProyect)
                g_count_proj_valid += count_proj_valid
                g_count_proj_invalid += count_proj_invalid
        m.close()
    else:
        print('The file', fd, 'not exist.')

    return g_count_proj_valid, g_count_proj_invalid


# ======================================================================================================
#                                       OPCION 2 FUNCIONES                                             #
# ======================================================================================================
def count_qty_stars(likes):
    if 0 <= likes <= 10:
        Stars = 1
    elif 10.1 <= likes <= 20:
        Stars = 2
    elif 20.1 <= likes <= 30:
        Stars = 3
    elif 30.1 <= likes <= 40:
        Stars = 4
    else:
        Stars = 5
    return Stars


def filter_for_tag_op2(gProject, tag):
    # This list is created so that it can be reused and ask if you want to save the list in an external .txt file
    gLista_Op2 = list()

    print("\n")
    print(f'|\033[33m{"Repository":<35}\033[0m | \033[33m{"Date":<12}\033[0m |    \033[33m{"Qty. Stars":<17}\033[0m|')
    for i in range(len(gProject)):
        if tag in gProject[i].tags:
            # To create a list to return and be able to save it in a text file
            gLista_Op2.append(gProject[i])
            # To verify the amount of stars
            qty_stars = str(count_qty_stars(gProject[i].likes)) + "☆"
            date = str(gProject[i].year) + "-" + str(gProject[i].month) + "-" + str(gProject[i].day)
            print(f'|\033[36m{gProject[i].repository:<35}\033[0m | \033[36m{date:<12}\033[0m |          \033[36m{qty_stars:<11}\033[0m|')

    return gLista_Op2


def store_file_txt_op2(gLista_Op2):
    if len(gLista_Op2) > 0:
        # Menu and question validation.
        mensaje = "Do you want to save the created list in a text file?"
        op = confirmation_menu_op2(mensaje)
        # Esto sobreescribira cada vez que se acceda a la opcion.
        fd = "Lista_Op2.txt"
        if op == 1:
            m = open(fd, "w")
            m.write("nombre_usuario|repositorio|fecha_actualizacion|lenguaje|estrellas|tags|url\n")
            for i in gLista_Op2:
                cadena = to_lista(i)
                m.write(cadena)
            m.close()
            print("The list was successfully saved in the file:", fd)
        else:
            print("The list was not saved in a text file.")
    else:
        print("No records were found with that tag.")
    print("\033[0m")


def confirmation_menu_op2(mensaje):
    print("\n" + mensaje)
    print("1 - Yes.")
    print("2 - No.")
    op = int(input("\033[35mEnter your option: "))
    while op > 2 or op < 1:
        op = int(input("\033[31mERROR:\n Enter a valid option(1-2): "))
    return op


def to_lista(gLista_Op2):
    # To obtain a character string for saving the tags
    tags_chain = ", ".join(gLista_Op2.tags)
    cadena = gLista_Op2.name + "|" + gLista_Op2.repository + "|" + str(gLista_Op2.year) + "-" + str(gLista_Op2.month) + "-" + \
             str(gLista_Op2.day) + "|" + gLista_Op2.lang + "|" + str(gLista_Op2.likes) + "|" + tags_chain + "|" + gLista_Op2.url + "\n"
    return cadena


# ======================================================================================================
#                                       OPCION 3 FUNCIONES                                             #
# ======================================================================================================
def counters_op3(gProject):
    first_time = True
    language_list = list()
    language_counts = list()

    for i in range(len(gProject)):
        if first_time:
            language_list.append(gProject[i].lang)
            language_counts.append(1)
            first_time = False
        else:
            if not gProject[i].lang in language_list:
                language_list.append(gProject[i].lang)
                language_counts.append(1)
            else:
                for j in range(len(language_list)):
                    if gProject[i].lang == language_list[j]:
                        language_counts[j] += 1
    return language_list, language_counts


def sort_op3(language_list, language_counts):
    n = len(language_list)
    for i in range(n-1):
        for j in range(i+1, n):
            if language_counts[i] < language_counts[j]:
                language_list[i], language_list[j] = language_list[j], language_list[i]
                language_counts[i], language_counts[j] = language_counts[j], language_counts[i]


# ======================================================================================================
#                                       OPCION 4 FUNCIONES                                             #
# ======================================================================================================
# I create a generic array with 0 to eventually fill it with the values I am looking for.
# In addition, I add its aesthetic print in the form of a table with stars and months.
def create_array():
    matriz = [[0] * 6 for f in range(13)]
    estrellas = ("1 ★", "2 ★", "3 ★", "4 ★", "5 ★")

    for i in range(len(matriz)):
        if i == 0:
            matriz[i][0] = ""
            for j in range(1, len(matriz[i])):
                matriz[i][j] = estrellas[j-1]
        else:
            matriz[i][0] = valid_month(i-1)
    return matriz


def complete_array_op4(gProject, gMatriz_op4):
    for i in range(len(gProject)):
        stars = count_qty_stars(gProject[i].likes)
        gMatriz_op4[gProject[i].month][stars] += 1


def show_array_op4(gMatriz):
    for f in range(len(gMatriz)):
        if f == 0:
            txt = f'{gMatriz[f][0]:<21}\033[0m| \033[33m{gMatriz[f][1]:<5}\033[0m | \033[33m{gMatriz[f][2]:<4}\033[0m | \033[33m{gMatriz[f][3]:<5}\033[0m ' \
                  f'| \033[33m{gMatriz[f][4]:<5}\033[0m | \033[33m{gMatriz[f][5]:<4}\033[0m |'
        else:
            txt = f'\033[34m {gMatriz[f][0]:<20}\033[0m| {gMatriz[f][1]:<5} | {gMatriz[f][2]:<5} | {gMatriz[f][3]:<5} ' \
                  f'| {gMatriz[f][4]:<5} | {gMatriz[f][5]:<5} |'
        print(txt)
    print("\n")


def accumulators_op4(gMatriz_op4, m):
    accumulator = 0
    for j in range(1, 6):
        accumulator += gMatriz_op4[m][j]
    return accumulator


def valid_month(m):
    # This function involves some math with arrays when passing its parameters since it needs the correct month,
    # sometimes using +1 or -1. This will be easily solved.
    meses = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",  "Aug", "Sep", "Oct", "Nov", "Dec")
    for i in range(len(meses)):
        if i == m:
            return meses[i]


# ======================================================================================================
#                                       OPCION 5 FUNCIONES                                             #
# ======================================================================================================
# V represents the Object/Vector/Class(gProject) and X represents the value to compare (Rep=Repository)
# Generic Binary Search function
def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c].repository:
            return c
        if x < v[c].repository:
            der = c - 1
        else:
            izq = c + 1
    return -1


def change_url_op5(gProject):
    URL = input("Enter a new URL to change in the file: ")
    gProject.url = URL


def update_to_current_date_op5(gProject):
    from datetime import datetime
    now = datetime.now()
    gProject.day, gProject.month, gProject.year = now.day, now.month, now.year


# ======================================================================================================
#                                       OPCION 6 FUNCIONES                                             #
# ======================================================================================================
# At the end of the file class_project, the records of the array are located.
def create_binary_file(gMatriz, fd_op6):
    m = open(fd_op6, "wb")
    for i in range(len(gMatriz)):
        pickle.dump(gMatriz[i], m)
        m.flush()
    print("\n\033[36mThe file of the array from point 4 was saved correctly in:", fd_op6)
    m.close()


# ======================================================================================================
#                                       OPCION 7 FUNCIONES                                             #
# ======================================================================================================
def load_binary_file(fd_op6, gMatriz_op7):
    m = open(fd_op6, "rb")
    t = os.path.getsize(fd_op6)
    while m.tell() < t:
        gNewMatriz = pickle.load(m)
        # Function to convert the "Month" and "Stars" strings saved in point 6 to integers.
        gNewMatriz.mes = valid_file_str_to_num(gNewMatriz.mes)
        gNewMatriz.estrellas = valid_file_str_to_num(gNewMatriz.estrellas)
        gMatriz_op7[gNewMatriz.mes][gNewMatriz.estrellas] = gNewMatriz.cantidad
    m.close()


def valid_file_str_to_num(dato):
    meses = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",  "Aug", "Sep", "Oct", "Nov", "Dec")
    estrellas = ("1 ★", "2 ★", "3 ★", "4 ★", "5 ★")

    for i in range(len(estrellas)):
        if dato == estrellas[i]:
            return i+1

    for i in range(len(meses)):
        if dato == meses[i]:
            return i+1
