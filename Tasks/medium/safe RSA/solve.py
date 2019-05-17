def extendedEuclid(a, n):
    U = [0, 1, n]
    V = [1, 0, a]

    while U[2] != 1 and U[2] != 0 and V[2] != 0:
        q = U[2] // V[2]
        for i in range(3):
            t = U[i] - V[i] * q
            U[i] = V[i]
            V[i] = t
    if (U[2] != 1):
        return 0

    if (U[0] < 0):
        U[0] += n

    return (U[0])


p = 737757897940993032182115482412659471
q = 1123604715059678054225100872480176241
e = 3
Cyphertext = 570383737295366064814032336840296435395089932193721921186253823571377215


n = p * q
N = (p - 1) * (q - 1)
d = extendedEuclid(e, N)

plaintext = str(pow(Cyphertext, d, n))
plaintext = ''.join([chr(int(plaintext[i:i + 3])) for i in range(0, len(plaintext), 3)])
print(plaintext)
