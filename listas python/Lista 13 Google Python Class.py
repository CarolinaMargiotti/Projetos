#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A. fim_igual
# Dada uma lista de strings, retorna o número de strings
# com tamanho >= 2 onde o primeiro e o último caracteres são iguais
# Exemplo: ['aba', 'xyz', 'aa', 'x', 'bbb'] retorna 3
def fim_igual(words):
    # verificar string por string dentro da lista
    cont = 0  # variavel para contar quantas strings batem com a condição
    for p in words:
        # verificar se a palavra p é do tamanho certo E o ultimo caractere [-1] é igual ao primeiro [0]
        if len(p) >= 2 and p[-1] == p[0]:
            cont += 1
    return cont

# B. x_antes
# Dada uma lista de strings retorna uma lista onde
# todos os elementos que começam com x ficam sorteados antes
# Ex.: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] retorna
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: monte duas listas separadas e junte-as no final


def x_antes(words):
    palavrasComX = []  # lista para palavras que começam com x
    palavrasResto = []
    # percorrer cada palavra para facilitar verificar isoladamente cada
    for p in words:
        if p[0] == 'x':  # a palavra começa com x?
            palavrasComX.append(p)
        else:  # não começa com x
            palavrasResto.append(p)
        palavrasComX.sort()
        palavrasResto.sort()
    return palavrasComX+palavrasResto


def last(a):  # esta def serve para a letra C
    return a[-1]

# C. sort_last
# Dada uma lista de tuplas não vazias retorna uma tupla ordenada
# por ordem crescente do último elemento
# Exemplo [(1, 7), (1, 3), (3, 4, 5), (2, 2)] retorna
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Dica: use key=função que você definiu e que retorna o último elemento


def sort_last(tuples):
    # tuplas são diferentes de listas!
    # colocar em ordem crescente do ultimo valor da tupla (1,2) 2 ultimo valor
    # da tupla não do elemento da lista
    # sorted — Return a new list containing
    # all items from the iterable in ascending order.
    # parametro 1, lista que quer varrer e por em ordem
    # parametro 2, condição genérica usada pela lista
    # variavel genérica tup contem o iterable da lista tuples (primeiro parametro)
    # que é passada de parametro para função que devolve o ultimo
    # elemento da tupla (estamos varrendo elemento por elemento da lista!
    # não da tupla!)
    # sorted então usa esse valor como key para organizar, vinculando a esse elemento
    tuples = sorted(tuples, key=lambda tup: last(tup))
    return tuples


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('fim_igual')
    test(fim_igual(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(fim_igual(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(fim_igual(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('x_antes')
    test(x_antes(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(x_antes(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(x_antes(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
