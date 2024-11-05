import random

class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    
    def __init__(self):
        lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet[::-1])}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet[::-1])}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])


# cipher = Atbash()
# line = input()
# while line != '.':
#     print(cipher.encode(line))
#     line = input()

class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = {}
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            decoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._decode.get(char, char) for char in line])


# key = int(input('Введите плюч:'))
# cipher = Caesar(key)
# line = input()
# while True:
#     print(cipher.encode(line))
#     line = input()



class Monoalphabet:
    alphabet = ""  # TODO

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        self._decode = {}  # TODO

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        pass  # TODO


# key = Monoalphabet.alphabet[:]
# random.shuffle(key)
# cipher = Monoalphabet(key)
# line = input()
# while line:
#     print(cipher.encode(line))
#     line = input()

class SimpleReplace():
    alphabet   = "егпжонщюэбэчмяхыцилдшарсйзвьёктф"
    alphabet_x = "шифрвженатакдльйоячёспгмзыхбцэую"
    
    def __init__(self):
        lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet_x)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet_x)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

cipher = SimpleReplace()
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()