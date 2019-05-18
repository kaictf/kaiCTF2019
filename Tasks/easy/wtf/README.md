
51 слой base64
# flag
kaiCTF{77870FFC8EF03E7A27C9D3B5510F9F3D}

#решение
>>> from base64 import b64decode
>>> data = open("file").read().encode()
>>> while True:
...	data=b64decode(data)
...
>>> print(data.deoced())

