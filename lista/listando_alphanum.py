def listando_alnum(lista):
    if type(lista) is str:
        lista_split = lista.split()  # Tire os espaços e separa os elementos em uma nova lista.
        lista_alnum = []  # Devolva a lista_split com elementos apenas com caracteres alfanum.

        for elemento in lista_split:
            if elemento.isalnum() is True:
                lista_alnum.append(
                    elemento.capitalize())  # Adicione na lista elementos apenas caractéres alfabéticos e numéricos
            else:
                elemento_editado = []  # Ajuste os elementos que não são alfabéticos e numéricos
                for digito in elemento:
                    if digito.isalnum() is False:
                        elemento_editado.append(" ")  # Substitua o dígito não alfabético e numérico por " "
                    elif digito.isalnum() is True:
                        elemento_editado.append(digito)  # Acrescente o dígito na lista_editado
                elemento_alnum = "".join(elemento_editado)  # Junte os dígitos em um string alfabética e numérica
                lista_alnum.append(
                    elemento_alnum)  # Acrescente o elemento não alfabéticos e numéricos(agora alfabéticos e numéricos) em lista_split
        # Até aqui temos uma lista de string's alfabéticas e numéricas, porém alguns elementos da lista podem conter mais de um item

        lista_alnum_split = []

        for item in lista_alnum:
            lista_alnum_split.append(
                item.split())  # Acrescente na lista_alnum_split os itens separados, agora cada item na lista original é uma lista com cada elemento sendo um item
        lista_alnum_split_item = []
        for sublista in lista_alnum_split:
            for nome in sublista:  # Pegue o nome na sublista
                lista_alnum_split_item.append(nome)  # Acrescente na lista_alnum_split_item os elementos nas sublistas
        lista_cap = []  # Capitalize os itens da lista lista_alpha_split_item
        for item in lista_alnum_split_item:
            lista_cap.append(item.capitalize())

        lista_quase_final = []
        for item_da_lista in lista_cap:  # Exclua itens de tamanho 1
            if len(item_da_lista) != 1:
                lista_quase_final.append(item_da_lista)
        lista_final = []
        for listado in lista_quase_final:
            if listado.isalpha() is True:
                lista_final.append(listado)
            elif listado.isalnum() is True:
                lista_num = []
                lista_alphabet = []
                for item in listado:
                    for digito in item:
                        if digito.isalpha() is True:
                            lista_alphabet.append(digito)
                        elif digito.isnumeric() is True:
                            lista_num.append(digito)
                lista_num_join = "".join(lista_num)
                lista_alphabet_join = "".join(lista_alphabet)
                lista_alphabet_cap = lista_alphabet_join.capitalize()
                lista_alpha_num = lista_num_join + " " + lista_alphabet_cap
                lista_final.append(lista_alpha_num)

        return lista_final

    else:
        print("A variável não é uma string")

lista = "1pão 2salsichas 4 manteigas 90 chocolates 500ml de gasolina 2-pães"
merda = listando_alnum(lista)
print(merda)

