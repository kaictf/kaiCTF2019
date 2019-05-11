# Broken-Terminal

## Секция
Stego

## Разбалловка
100

## Смысл задания
Участнику выдается GIF файл -<br>
<img src="https://psv4.userapi.com/c848436/u232954835/docs/d13/2bbe1f786951/terminal.gif?extra=-55Xd2FGgmVrDlufmr9k-vAhEHCqdzfddRbyc6u9qqFtlPPpy6lt2mdPtDr7mlWlt_VdJ5UbF4YpfnHjlsOSE1aVDE4jCtC9KVQATrTzVmr3gN1zmm1E-xMPdFIcGtda3IgTabgsOXtzvY2VXlOJl_ur"><br>

## Путь решения
Если открыть файл в HEX-редакторе, то в конце, после 00 байтиков виден явный base64.<br>
Участник пробует декодировать онлайн сервисом и получает кракозябры и сигнатуру 7z в начале.<br>
Путем ручного декодирвоания или через сервисы по декодированию base64 файлов, он получает zip архив в котором лежит флаг.<br>
