# Broken-Terminal

## Секция
Stego

## Разбалловка
100

## Смысл задания
Участнику выдается GIF файл -<br>
<img src="https://psv4.userapi.com/c848436/u232954835/docs/d13/8498441fff56/terminal.gif?extra=8Ir-zTQZfhi55KFiA04hae5p4oEM0cRYP3vmK4wOu2Q2dd7muJTqYKQDDsDU5y12iSzKhCFFruD13kVHrQymUd_rhyfxRF_az6YPrDdtf8rq6o7d-flfDC360EdX5Pk67TH8FlLXWuF3iCgJ1oODod_1"><br>

## Путь решения
Если открыть файл в HEX-редакторе, то в конце, после 00 байтиков виден явный base64.<br>
Участник пробует декодировать онлайн сервисом и получает кракозябры и сигнатуру 7z в начале.<br>
Путем ручного декодирвоания или через сервисы по декодированию base64 файлов, он получает zip архив в котором лежит флаг.<br>
