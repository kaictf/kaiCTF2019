# Sezaaam

## Секция
- PPC
- Web

## Разбалловка
200

## Флаг
kaiCTF{6a4b909aee1a838bda249e1a3434e60e}

## Смысл задания
Участник получает точку входа ввида 

[open](http://10.116.1.151:10030)

Данный URL введет на веб-сервер, на котором включена автоиндексация (при входе в папку отображается ее содержимое), но каждый из подуровней находится под HTTP Basic Authentication.

Задача участника заключается в поиске той директории, в которой лежит флаг. Название директорий состоит из цифр, выбирается рандомно. Флаг располагается тоже в рандомной директории. Как только участник находит путь, по которому находится флаг, он может его запросить без аутентификации.
 
 
 Как можно добраться до каждого из уровней:
 
  <code bash>
hydra -L seclists_10_million_password_list_top_10000.txt -e s -f 192.168.93.226  http-head
 </code>

## Описание задания
Мы выяснили, что рейдеры шли и грабили корованы с крышками и хранили их в сундуке. Мы преследовали их до их убежища, но мы не можем открыть сундук. Нам нужны ментаты,rrrrrrrwawadarawradr

## Description
We found out that raiders went and robbed corovans with caps and stored them in a chest. We have chased them until their shelter, but we're unable to open the chest. We need mentats, arrwwawarawraraaar...

## Подсказки
- https://www.owasp.org/index.php/Basic_Authentication
- PASS = USER
- https://github.com/erforschr/bruteforce-http-auth
- https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
