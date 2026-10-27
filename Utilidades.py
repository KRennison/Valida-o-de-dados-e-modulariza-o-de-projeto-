def maior_iterativo(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior


def maior_recursivo(lista):
    if len(lista) == 1:
        return lista[0]

    if lista[0] > maior_recursivo(lista[1:]):
        return lista[0]

    return maior_recursivo(lista[1:])


def valida_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11 or not cpf.isdigit():
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0

    if resto != int(cpf[9]):
        return False

    soma = 0

    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0

    return resto == int(cpf[10])


if __name__ == "__main__":
    print(maior_iterativo([3, 9, 2, 7]))
    print(maior_recursivo([3, 9, 2, 7]))
    print(valida_cpf("529.982.247-25"))
