def str_float(string): #recebe uma string, queremos verificar se essa string pode ser float
    if type(string) is str:
        string_split = string.split()
        if len(string_split) == 1:
            if string[0] == "-":
                if string[1].isnumeric() is True:
                    if string.find(".") != -1:
                        pto = string.find(".")
                        if string[pto+1:].isnumeric() is True and string[1:pto].isnumeric() is True:
                            return True
                        else:
                            return False
                    elif string.count(".") != 1 and string.count(".") != 0:
                        return False
                    else:
                        if string[1:].isnumeric() is True:
                            return True
                        else:
                            return False
                elif string[1:].isnumeric() is True:
                    return True
                else:
                    return False
            else:
                if string[0].isnumeric() is True:
                    if string.find(".") != -1:
                        pto = string.find(".")
                        if string[pto + 1:].isnumeric() is True and string[0:pto].isnumeric() is True:
                            return True
                        else:
                            return False
                    elif string.count(".") != 1 and string.count(".") != 0:
                        return False
                    else:
                        if string[0:].isnumeric() is True:
                            return True
                        else:
                            return False
                elif string[0:].isnumeric() is True:
                    return True
                else:
                    return False
        else:
            return False
    else:
        print("A variável não é uma string")
print(str_float("-12.23"))