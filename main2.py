from functions import *


def menu():
    print("\033[35m═════ MENU ═════")
    print("1 - Load.")
    print("2 - Filter by tag.")
    print("3 - Languages.")
    print("4 - Popularity.")
    print("5 - Search for updated project.")
    print("6 - Save popular.")
    print("7 - Show file.")
    print("8 - Show Complete Project.")
    print("0 - Quit.")
    print("═" * 15)
    return int(input("\033[32m \t*Enter your option: "))


def main():
    gProject = list()
    # Main File Name to Read
    fd = 'proyectos.csv'

    # Bool Dependency of Point 1
    gHas_Op1 = False
    # Bool Dependency of Point 4
    gHas_Op4 = False
    # file_name_used in option 6 and 7
    fd_op6 = "Archivo_Binario_Op6.dat"
    gMatriz_op4 = None

    op = -1
    while op != 0:
        op = menu()

        if not gHas_Op1:
            if op == 1:
                gCount_Rec_Valid, gCount_Rec_Invalid = leer_csv_op1(fd, gProject)
                print("\n\033[36m♦ Amount of Records that were loaded:", gCount_Rec_Valid)
                print("♦ Quantity Records that were omitted:", gCount_Rec_Invalid)
                gHas_Op1 = True
            elif op != 0 and op != 7:
                print("\033[31mYou must first enter Option 1.\033[31m")

        else:
            # Although it may not be here, if you re-enter option 1, the same file will be loaded again.
            # This would not be a problem because all the files would be omitted.
            if op == 1:
                gCount_Rec_Valid, gCount_Rec_Invalid = leer_csv_op1(fd, gProject)
                print("\n\033[36m♦ Amount of Records that were loaded:", gCount_Rec_Valid)
                print("♦ Quantity Records that were omitted:", gCount_Rec_Invalid)

            elif op == 2:
                tag = input("\nEnter a tag to search for: ")
                gLista_Op2 = filter_for_tag_op2(gProject, tag)
                store_file_txt_op2(gLista_Op2)

            elif op == 3:
                language_list, language_counts = counters_op3(gProject)
                sort_op3(language_list, language_counts)
                print("\n")
                print(f'| \033[33m{"Language":<20}\033[0m |  \033[33m{"Qty Projects":<10}\033[0m |')
                for i in range(len(language_list)):
                    print(f'| \033[36m{language_list[i]:<20}\033[0m |        \033[36m{language_counts[i]:<8}\033[0m |')

            elif op == 4:
                gHas_Op4 = True

                gArray_op4 = create_array()
                # To fill the array with the accumulators
                complete_array_op4(gProject, gArray_op4)
                show_array_op4(gArray_op4)

                m = -1
                while not (0 < m < 13):
                    m = int(input("\033[36mEnter a month (between 1 and 12) to see the number of projects to update: "))

                accum = accumulators_op4(gArray_op4, m)
                if accum > 0:
                    print("The total number of projects to update in", valid_month(m-1), "es :", accum)
                else:
                    print("No projects to update in", valid_month(m-1))

            elif op == 5:
                rep = input("\n\033[33mEnter a repository to search for: ")

                pos = binary_search(gProject, rep)
                if pos >= 0:
                    # To view the data of the project prior to the change
                    print(gProject[pos])

                    # We recycle the function used in the Functions_Op2 module
                    mensaje = "Do you want to modify the URL of the file and the update date to the current date?"
                    op = confirmation_menu_op2(mensaje)

                    if op == 1:
                        change_url_op5(gProject[pos])
                        update_to_current_date_op5(gProject[pos])
                        # Mostrar los datos actualizados
                        print("\n\n\033[33mProject modified:")
                        print(gProject[pos])
                    else:
                        print("No data will be changed for the URL or the update date.")
                else:
                    print("The repository entered does not exist in the project.")

            # Dependency of Point 4
            elif op == 6:
                if gHas_Op4:
                    gMatriz = create_array_op6(gArray_op4)
                    create_binary_file(gMatriz, fd_op6)
                else:
                    print("You must first select option 4 to choose this option.")

            # To display the complete project
            elif op == 8:
                print('{:<20}'.format("User Name") + '{:<20}'.format("Repository") + '{:<20}'.format("Date") + '{:<20}'.format("Language") +
                        '{:<20}'.format("Likes") + '{:<20}'.format("Tags") + '{:<20}'.format("URL"))
                for i in gProject:
                    print(i)

        # Dependency of Point 6
        if op == 7:
            print("\n")
            gMatriz_op7 = create_array()
            if os.path.exists(fd_op6):
                load_binary_file(fd_op6, gMatriz_op7)
                show_array_op4(gMatriz_op7)
            else:
                print("\033[31mERROR:\n You must first use option 6 (create file).\033[31m")

        elif op == 0:
            print("Quit...")

        print("\033[31m\n\n")
        os.system("pause")
        print("\033[0m")


if __name__ == '__main__':
    main()
