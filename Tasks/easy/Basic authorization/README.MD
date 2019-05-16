# Basic authorization




## Секция
WEB




## Разбалловка
10




## Смысл задания
Дан заголовок запроса,в котором присутствует строка, шифрованная base64.




## Флаг
kaiCTF{44a75eed4dfa750953b610f2a17c617d}




## Описание
Мы перехватили запрос,но ничего не можем в нем разобрать,ты можешь нам помочь в этом?



```
GET /securefiles/ HTTP/1.1
Host: www.kai.ctf
Authorization: Basic ZmxhZzprYWlDVEZ7NDRhNzVlZWQ0ZGZhNzUwOTUzYjYxMGYyYTE3YzYxN2R9Cg
```



## Путь решения

Участник должен расшифровать строку, шифрованную base64

