
# Описание
Мы обнаружили странный файл. Кажется в нем ничего нет.

# Разветывание
к таску приложить файл LSB.wav

# Flag
kaiCTF{f35c21306142867668986880cd2fb48b}

# решение
from scipy.io import wavfile
l = 8*40
fs, new_data = wavfile.read("LSB.wav")
binary_data = "".join((str(extract(new_data, i)) for i in range(l)))
t="".join([chr(int(binary_data[j:j+8], 2)) for j in range(0, l, 8)])
print(t)
