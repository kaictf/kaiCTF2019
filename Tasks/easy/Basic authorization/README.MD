# Basic authorization




## Секция

WEB




## Разбалловка

50




## Смысл задания

Дан заголовок запроса,в котором присутствует строка, шифрованная base64.




## Flag

kaiCTF{b@se64_1s_C0ol}




## Описание

Мы перехватили запрос,но ничего не можем в нем разобрать,ты можешь нам помочь в этом?




GET /securefiles/ HTTP/1.1

Host: www.kaiCTF.com

Authorization: Basic ZmxhZzprYWlDVEZ7YkBzZTY0XzFzX0Mwb2x9




## Путь решения

Участник должен расшифровать строку, шифрованную base64

