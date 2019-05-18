# KaiCTF2019

## Запуск всех сервисов

<code bash>
for r in $(find . -name "docker-compose.yaml"); do docker-compose -f $r build --no-cache; done
</code>


<code bash>
for r in $(find . -name "docker-compose.yaml"); do docker-compose -f $r stop; done
</code>


<code bash>
for r in $(find . -name "docker-compose.yaml"); do docker-compose -f $r start; done</code>

## Список текущих заданий

### Hard
- MINIMIZEME - 200
- sezaaam - 200
- Kitty_Ping - 150
- sql-leakage - 250
- Terminal-Hack-3


### Medium
- 50shadesofgreen - 120
- Broken-Terminal - 100
- LetterRep - 110
- blind-xss - 200
- login-traff - 200
- metaTONNA - 110
- safe RSA - 120



### Easy
- Basic authorization - 40
- EasyStego - 80
- Last-signal - 80
- Lost-Pass - 50
- SecretPerson - 80
- backdoor - 80
- crazymatreshka - 100
- traf-watch - 80


## По портам


### Hard
- MINIMIZEME - 10020
- sezaaam - 10030
- Kitty_Ping - 10060
- Terminal-Hack-3 - 2224


### Medium
- 50 Shades of green - N/A
- Broken-Terminal - N/A
- sql-leakage -  N/A
- blind-xss - 10050
- login-traff - N/A
- metaTONNA - N/A
- LetterRap - N.A



### Easy
- Last-signal - N/A
- CrazyMatreshka - N/A
- backdoor - 10010
- crazymatreshka - N/A
- SecretPerson - N/A
- Basic authorization - N/A
- history - 10070
