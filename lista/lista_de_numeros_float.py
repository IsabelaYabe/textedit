from str_float import str_float

def listando_float(lista):
    if type(lista) == str :
        lista_split = lista.split()  # Tire os espaços e separa os elementos em uma nova lista.
        lista_num = []  # Devolva a lista_split com elementos apenas com caracteres numéricos.
        print(lista_split)
        for elemento in lista_split:
            elemento_editado = []  # Ajuste os elementos que não são numéricos.
            if str_float(elemento) is True:
                lista_num.append(elemento)  # Adicione na lista elementos apenas caractéres numéricos.
            elif "." in elemento:
                print(elemento)
                contador = 0
                lista_pto = []
                while contador < len(elemento):
                    if elemento[contador] == ".":
                        lista_pto.append(contador)
                    contador+=1
                print(lista_pto)
                for pto in lista_pto:
                    print(elemento[(pto-1)])
                    print(elemento[(pto+1)])
                    if (elemento[(pto-1)].isnumeric() is True) and (elemento[(pto+1)].isnumeric() is True):
                        for digito in elemento:
                            if digito.isnumeric() is False and digito != "-" and digito != ".":
                                elemento_editado.append(" ")  # Substitua o dígito não numérico por " "
                            elif digito.isnumeric() is True or (digito == "-" == elemento[0]) or digito == ".":
                                elemento_editado.append(digito)  # Acrescente o dígito na lista_editado
                            elif digito.isnumeric() is True or (digito == "-" != elemento[0]):
                                elemento_editado.append(" -")
                    else:
                        elemento_editado.append(" ")


                print(elemento_editado)

                elemento_num = "".join(elemento_editado)  # Junte os dígitos em um string numérica.
                lista_num.append(elemento_num)  # Acrescente o elemento numérico (agora numérico) em lista_split
        # Até aqui temos uma lista de string's numérica, porém alguns elementos da lista podem conter mais de um item
        print(elemento_editado)
        lista_num_split = []

        for item in lista_num:
            lista_num_split.append(
                item.split())  # Acrescente na lista_num_split os itens separados, agora cada item na lista original é uma lista com cada elemento sendo um item
        lista_num_split_item = []
        for sublista in lista_num_split:
            for nome in sublista:  # Pegue o nome na sublista
                lista_num_split_item.append(nome)  # Acrescente na lista_alpha_split_item os elementos nas sublistas
        lista_corrigida = []
        for elemento in lista_num_split_item:
            if elemento.count("-") != 1 and elemento.count("-") != 0:
                elemento_substituido = elemento.replace("-", "")
                lista_corrigida.append("-" + elemento_substituido)
            else:
                lista_corrigida.append(elemento)

        lista_numerica = []
        for num in lista_corrigida:
            if num != "-":
                numero = float(num)
                lista_numerica.append(numero)

        return lista_numerica

    else:
        print("A variável não é uma string")




lista = "8,72, ,---112- -2.8.-..-.3.89e-9 -2.3"
merda = listando_float(lista)
print(merda)
