from functools import reduce

array = [1,2,3,6,89,9]

def calculaSomaArray(num1,num2):
    """
    Soma por função
    """
    return num1+num2

soma = reduce(calculaSomaArray,array)

"""
Soma por while
"""
cont=0
while(cont<len(array)):
    print(array[cont])
    cont=cont+1

"""
Soma se for maior que 5
"""
somamaiorquecinco = reduce(calculaSomaArray,filter(lambda x : x>5,array))
print(soma)
print(somamaiorquecinco)