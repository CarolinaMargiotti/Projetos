#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras para listas

# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
    # set transforma nums em dicionario e dicionarios não podem conter repetição
    # como o retorno é dicionario precisa ser convertido novamente pra lista
    return list(set(nums))

# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar


def cripto(frase):
    # guardar uma lista com cada palavra separada por espaço para não perdemrmos
    # suas localizações
    listLetras = frase.split()
    # varrer uma por uma mas precisamos saber suas localizações para trocarmos
    # com suas novas versões sem letras repetidas
    for p in range(0, len(listLetras)):
        # set devolve o elemento sem elementos repetidos, mas ao convertermos
        # sorted os organiza em ordem alfabetica
        # join remove o formato dicionario, e substitui as virgulas
        # que separa os items em "" nada, para ser uma palavra
        listLetras[p] = "".join(sorted(set(listLetras[p])))
    # transforma em uma string normal e separa os itens por espaço
    return ' '.join(listLetras)

# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2


def derivada(coef):
    for p in range(1, len(coef)):
        # derivada pega expoente da variavel e coloca na frente multiplicando
        coef[p] = p*coef[p]
    return coef[1:]  # o primeiro item não tem x, é ignorando na derivada

# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# Não vale converter a lista em número para somar diretamente


def soma(n1, n2):
    holder = 0  # variavel para carregar o excesso que sera somado no elemento seguinte
    for i in range(0, len(n1)):
        # soma os dois valores mais o holder que sobrou de outra soma
        soma = n1[i]+n2[i]+holder
        # print(str(soma)+"   :"+str(n1[i])+" | "+str(n2[i])+"    )"+str(holder))
        if(soma >= 10):  # terá holder
            # o valor que deve ser somado na próxima variavel é tudo menos a unidade
            holder = (soma-(soma % 10))/10
            n1[i] = soma % 10  # soma a unidade ja que todo o resto será holder
        else:
            holder = 0  # sem ter algo para sobrar na soma, seta o holder para 0, para não afetar outras somas
            n1[i] = soma
    if holder != 0:  # as vezes os ultimos numeros somados podem dar um valor maior que 9, então sobra um holder que não se pode jogar fora
        n1.append(holder)
    return n1

# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é são uma é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False


def anagrama(s1, s2):
    # precisamos saber se tem as mesmas letras
    if set(s1) == set(s2):
        # mas também a mesma quantidade de letras
        for c in s1:
            if s2.count(c) != s1.count(c):
                return False
    else:  # caso tenham letras diferentes
        return False
    return True


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('remove_iguais')
    test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
    test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
    test(remove_iguais([]), [])

    print()
    print('cripto')
    test(cripto('ana e mariana gostam de banana'),
         'an e aimnr agmost de abn')
    test(cripto('Batatinha quando nasce esparrama pelo chão'),
         'Bahint adnoqu acens aemprs elop choã')

    print()
    print('derivada de polinômio')
    test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
    test(derivada([4, 16, 1]), [16, 2])

    print()
    print('soma em listas invertidas')
    test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
    test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])

    print()
    print('anagrama')
    test(anagrama('aberto', 'rebato'), True)
    test(anagrama('amor', 'roma'), True)
    test(anagrama('ramo', 'amor'), True)
    test(anagrama('baba', 'aba'), False)
    test(anagrama('casa', 'cassa'), False)


if __name__ == '__main__':
    main()
