def listando_str(lista):
    if type(lista) is str:
        lista_split = lista.split()  # Tire os espaços e separa os elementos em uma nova lista.
        lista_alpha = []  # Devolva a lista_split com elementos apenas com caracteres alphabet.

        for elemento in lista_split:
            if elemento.isalpha() is True:
                lista_alpha.append(elemento.capitalize())  # Adicione na lista elementos apenas caractéres alfabéticos
            else:
                elemento_editado = []  # Ajuste os elementos que não são alfabéticos
                for digito in elemento:
                    if digito.isalpha() is False:
                        elemento_editado.append(" ")  # Substitua o dígito não alfabético por " "
                    elif digito.isalpha() is True:
                        elemento_editado.append(digito)  # Acrescente o dígito na lista_editado
                elemento_alpha = "".join(elemento_editado)  # Junte os dígitos em um string alfabética
                lista_alpha.append(
                    elemento_alpha)  # Acrescente o elemento não alfabéticos (agora alfabéticos) em lista_split
    # Até aqui temos uma lista de string's alfabéticas, porém alguns elementos da lista podem conter mais de um item

        lista_alpha_split = []

        for item in lista_alpha:
            lista_alpha_split.append(
                item.split())  # Acrescente na lista_alpha_split os itens separados, agora cada item na lista original é uma lista com cada elemento sendo um item
        lista_alpha_split_item = []
        for sublista in lista_alpha_split:
            for nome in sublista:  # Pegue o nome na sublista
                lista_alpha_split_item.append(nome)  # Acrescente na lista_alpha_split_item os elementos nas sublistas
        lista_cap = []  # Capitalize os itens da lista lista_alpha_split_item
        for item in lista_alpha_split_item:
            lista_cap.append(item.capitalize())

        lista_final = []
        for item_da_lista in lista_cap:  # Exclua itens de tamanho 1
            if len(item_da_lista) != 1:
                lista_final.append(item_da_lista)

        return lista_final
    else:
        print("A variável não é uma string")

lista = "calculo-ga-c1-ic-icd-e aedv"
merda = listando_str(lista)
print(merda)

