# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras

# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
def verbing(s):
    if len(s) >= 3:
        if "ing" in s:
            return s+"ly"
        return s+"ing"
    return s

# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'


def not_bad(s):
    bad = s.find("bad")
    notV = s.find("not")
    if notV < bad:
        return s[0:notV]+"good"+s[bad+3:]
    return s

# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
#  a-inicio + b-inicio + a-final + b-final


def inicio_final(a, b):
    a_1 = ""
    a_2 = ""
    b_1 = ""
    b_2 = ""
    if(len(a) % 2 == 0):
        a_1 = a[:int(len(a)/2)]
        a_2 = a[int(len(a)/2):]
    else:
        a_1 = a[:int(len(a)/2)+1]
        a_2 = a[int(len(a)/2)+1:]

    if(len(b) % 2 == 0):
        b_1 = b[:int(len(b)/2)]
        b_2 = b[int(len(b)/2):]
    else:
        b_1 = b[:int(len(b)/2)+1]
        b_2 = b[int(len(b)/2)+1:]
    return a_1+b_1+a_2+b_2

# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três


def zf(n):
    n = str(n)[::-1]
    count = 0
    for p in n:
        if(p == "0"):
            count += 1
        else:
            break
    return count

# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19


def conta2(n):
    count = 0
    for i in range(0, n-1):
        if "2" in str(i):
            count += str(i).count("2")
    return count

# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536


def inip2(n):
    naoAchou = True
    i = 0
    while naoAchou:
        if str(2**i)[0:len(str(n))] == str(n):
            naoAchou = False
            break
        i += 1
    return i


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('inicio_final')
    test(inicio_final('abcd', 'xy'), 'abxcdy')
    test(inicio_final('abcde', 'xyz'), 'abcxydez')
    test(inicio_final('Kitten', 'Donut'), 'KitDontenut')

    print()
    print('zeros finais')
    test(zf(10100100010000), 4)
    test(zf(90000000000000000010), 1)

    print()
    print('conta 2')
    test(conta2(20), 2)
    test(conta2(999), 300)
    test(conta2(555), 216)

    print()
    print('inicio p2')
    test(inip2(7), 46)
    test(inip2(133), 316)
    test(inip2(1024), 10)


if __name__ == '__main__':
    main()
