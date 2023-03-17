

class Project:
    def __init__(self, user_name, repository, day, month, year, language, likes, tags, url):
        self.name = user_name
        self.repository = repository
        self.day = day
        self.month = month
        self.year = year
        self.lang = language
        self.likes = likes
        self.tags = tags
        self.url = url


    def __str__(self):
        # To create a string with the date
        date = str(self.year) + "-" + str(self.month) + "-" + str(self.day)


        # print('{:<20}'.format("User Name") + '{:<20}'.format("Repository") + '{:<20}'.format("Date") + '{:<20}'.format("Language") +
        #        '{:<20}'.format("Likes") + '{:<20}'.format("Tags") + '{:<20}'.format("URL"))


        r = ""
        r += '{:<20}'.format(str(self.name)) + '{:<20}'.format(str(self.repository)) + '{:<20}'.format(date) + '{:<20}'.format(str(self.lang))
        r += '{:<20}'.format(str(self.likes)) + '{:<20}'.format(str(self.tags)) + '{:<20}'.format(str(self.url))
        return r


def csv_to_Proyecto(linea):
    # To avoid reading empty intermediate lines, :-1 is used
    linea = linea[:-1]
    # To separate each line of the .csv file into tokens
    token = linea.split('|')

    # token 3 is the update date
    year, month, day = str_to_date_token3(token[3])
    # A float is returned to token5, with its function
    token[5] = str_to_float_token5(token[5])
    # A vector is returned to token6, with its function
    token[6] = str_to_vector_tag_token6(token[6])

    return Project(token[0], token[1], year, month, day, token[4], token[5], token[6], token[7])


def str_to_date_token3(token):
    token_list = token.split("-")
    return int(token_list[0]), int(token_list[1]), int(token_list[2])


def str_to_float_token5(token):
    num = ""
    for i in token:
        if i.lower() != "k":
            num += i
    return float(num)


def str_to_vector_tag_token6(token):
    """
    # Maybe this function dont found in all cases
    if "," in token:
        token_list = token.split(",")
    else:
        token_list = v_tags.append(token)
    return token_list
    """
    v_tags = []
    Palabra = ""
    for i in token:
        if i != ",":
            Palabra += i
        else:
            v_tags.append(Palabra)
            Palabra = ""
    # To add the Tag, in case there's only 1.
    if len(Palabra) > 0:
        v_tags.append(Palabra)
    return v_tags


# ======================================================================================================
#                                       Class Option 6                                                 #
# ======================================================================================================
class Matriz:
    def __init__(self, mes, estrellas, cant_proy):
        self.mes = mes
        self.estrellas = estrellas
        self.cantidad = cant_proy


def create_array_op6(gMatriz_op4):
    gMatriz = list()
    for i in range(1, len(gMatriz_op4)):
        mes = gMatriz_op4[i][0]
        for j in range(1, len(gMatriz_op4[i])):
            estrellas = gMatriz_op4[0][j]
            cantidad = gMatriz_op4[i][j]
            if cantidad > 0:
                NewMatriz = Matriz(mes, estrellas, cantidad)
                gMatriz.append(NewMatriz)
    return gMatriz
