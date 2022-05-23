def listando_int_pos(lista):
    if type(lista) is str:
        lista_split = lista.split()  # Tire os espaços e separa os elementos em uma nova lista.
        lista_num = []  # Devolva a lista_split com elementos apenas com caracteres numéricos.

        for elemento in lista_split:
            if elemento.isnumeric() is True:
                lista_num.append(elemento())  # Adicione na lista elementos apenas caractéres numéricos.
            else:
                elemento_editado = []  # Ajuste os elementos que não são numéricos.
                for digito in elemento:
                    if digito.isnumeric() is False:
                        elemento_editado.append(" ")  # Substitua o dígito não numérico por " "
                    elif digito.isnumeric() is True:
                        elemento_editado.append(digito)  # Acrescente o dígito na lista_editado
                elemento_num = "".join(elemento_editado)  # Junte os dígitos em um string numérica.
                lista_num.append(elemento_num)  # Acrescente o elemento numérico (agora numérico) em lista_split
        # Até aqui temos uma lista de string's numérica, porém alguns elementos da lista podem conter mais de um item

        lista_num_split = []

        for item in lista_num:
            lista_num_split.append(
                item.split())  # Acrescente na lista_num_split os itens separados, agora cada item na lista original é uma lista com cada elemento sendo um item
        lista_num_split_item = []
        for sublista in lista_num_split:
            for nome in sublista:  # Pegue o nome na sublista
                lista_num_split_item.append(nome)  # Acrescente na lista_alpha_split_item os elementos nas sublistas
        lista_numerica = []
        for num in lista_num_split_item:
            numero = int(num)
            lista_numerica.append(numero)

        return lista_numerica

    else:
        print("A variável não é uma string")



lista = "8,72,,-123---b89e9"
merda = listando_int_pos(lista)
print(merda)

