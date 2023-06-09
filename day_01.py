"""

EASY

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Português (Brasil)

FACIL

Dada uma lista de números e um número k, retorne se quaisquer dois números da lista somam k.

Por exemplo, dados [10, 15, 3, 7] e k de 17, retorne verdadeiro, pois 10 + 7 é 17.

Bônus: você pode fazer isso de uma só vez?
"""

def sumItems(numbers, k):
    for i in range(len(numbers)):
        for a in range(i+1, len(numbers)):
            if numbers[i] + numbers[a] == k:
                return True
    return False

print(sumItems([10, 5, 6, 8, 9, 7, 3], 15))
print(sumItems([10, 5, 6, 8, 9, 7, 3], 25))
print(sumItems([10, 5, 6, 8, 9, 7, 3], 19))
print(sumItems([10, 5, 6, 8, 9, 7, 3], 48))
