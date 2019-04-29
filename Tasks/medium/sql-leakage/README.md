# QUERY LEAKAGE

## Секция
- Network

## Разбалловка
100

## Флаг
kaiCTF2019{UsE_SECURED_Sessi0ns}

## Смысл задания
Участник получает дамп трафика. В этом дампе содержится большое количество сетевых взаимодействий (HTTP, HTTPS, ICMP, DNS). При этом в дампе содержится дамп сессии MSSQL сервера, в рамках который в незашифрованном виде был сделан запрос в БД по таблице secureFl@g в базе leave_me:

<code sql>
select fl_ from secureFl@g limit by 1;
</code>

При этом запрос был сделан поэтапно, т.е. был запрошел 1 символ, спустя некоторое время второй символ, потом третьий и т.д. до конца.


## Описание задания
Мы получили информацию, что злостные хакеры используют супер-секурный протокол© для передачи своих транзакций. Но мы же с вами настоящие хакеры, взломаем этот язык ?

## Description
We have received information that evil hackers use very super encrypted© protocol to send their transactions. But we are true hackers, can break this lang, aren't we?

## Подсказки
- WILL WE BREAK THIS 'CODE' OR 'NOT'='NOT'--
- MSSQL
- TCP/1433
