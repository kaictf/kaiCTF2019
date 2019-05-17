#

#описание
После ядерной войны, люди устанавливают это себе на старые телефоны. У нас их не осталось, нам сказали что ты можешь помочь. 

#flag
kaiCTF{214ec8aa0c94f81e6f943cd8176b088c}

#решение
apktool d app.apk
cd app/smali/com/example/warlock/easy
cat MainActivity.smali | grep kai
