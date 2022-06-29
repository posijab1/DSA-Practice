def valid_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(valid_anagram('hello', 'holle'))

def valid_anagram2(str1, str2):

    if len(str1) == len(str2):

        aux1, aux2 = {}, {}

        for i in range(len(str1)):
            aux1[str1[i]] = 1 + aux1.get(str1[i], 0)
            aux2[str2[i]] = 1 + aux2.get(str2[i], 0)

        return aux1 == aux2
    return False

print(valid_anagram2('hola', 'halo'))