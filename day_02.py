"""
HARD

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the 
product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our 
input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

---------------------
Português (Brasil)

DIFICIL

Dada uma matriz de inteiros, retorne uma nova matriz de modo que cada elemento no índice i da nova matriz seja o
produto de todos os números na matriz original, exceto aquele em i.

Por exemplo, se nossa entrada fosse [1, 2, 3, 4, 5], a saída esperada seria [120, 60, 40, 30, 24]. se nosso
entrada foi [3, 2, 1], a saída esperada seria [2, 3, 6].

Acompanhamento: e se você não puder usar a divisão?

"""

numbers = [5, 6, 2, 3, 8]

def productAllNumbers(list):
    new_list = []
    
    for i, value in enumerate(list):
        first_list = list
        original_int = first_list[i]
        first_list[i] = 1

        product = 1

        for a in first_list:
            product = product * a

        new_list.append(product)

        first_list[i] = original_int
    
    return new_list

num = productAllNumbers(numbers)
print(num)


