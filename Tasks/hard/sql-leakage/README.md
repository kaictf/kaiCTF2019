# QUERY LEAKAGE

## Секция
- Network

## Разбалловка
250

## Флаг
kaiCTF2019{UsE_SECURED_Sessi0ns}

## Смысл задания
Участник получает дамп трафика. В этом дампе содержится большое количество сетевых взаимодействий (HTTP, HTTPS, ICMP, DNS). При этом в дампе содержится дамп сессии MSSQL сервера, в рамках который в незашифрованном виде был сделан запрос в БД по таблице secureFl@g в базе leave_me:

Используется База данных "hackers", таблица "secureFl@g". Схема отношений таблицы - 

<br>secureFl@g(id INT PRIMARY KEY, fl_ VARCHAR(100)); </br>


Шаблон используемых SQL команд, участник может получить исходных флаг по поиску параметров, вызываемых с удаленной процедурой:

<code sql>
INSERT TOP (200) INTO secureFl@g(id, fl_) VALUES (@id, @fl_)
</code>

Взаимодействие с СУБД MSSQL происходит с помощью Microsoft SQL Management Studio. Процесс обнаружения нетривиален - используемый способ (MSSMS) использует процедуры для вставки записей в таблице.
Вкратце, участнику рекомендуется использование GUI Wireshark. 

На данной картинке представлено, как можно обнаружить букву "i" в порядке вызова вставок в таблицу.

![](way_of_solving.png)




## Описание задания
Мы получили информацию, что злостные хакеры используют супер-секурный протокол© для передачи своих транзакций. Но мы же с вами настоящие хакеры, взломаем этот язык ?

## Description
We have received information that evil hackers use very super encrypted© protocol to send their transactions. But we are true hackers, can break this lang, aren't we?

## Подсказки
- WILL WE BREAK THIS 'CODE' OR 'NOT'='NOT'--
- MSSQL
- Microsoft SQL Management Studio 
