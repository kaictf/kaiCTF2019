## Login traffic

### Category
Forensics

### Points
medium/hard

### Task description
Подозреваемый использует одинаковый пароль на нескольких ресурсах. Мы перехватили трафик при попытке залогиниться на одном из них, но почему-то не удается воспользоваться им на другом сервисе. Помогите восстановить исходный пароль.
@baydarich

### Flag
kaiCTF{c063c864e3fa3d802271ed5198f88118}

### Hint
1. js + password
2. b64 = base64(password) and final = md5(b64[0]) || md5(b64[1]) ||..|| md5(b64[n])

### Info

`ready` folder contains pcap dump. ONLY this pcap should be given to participants.

`src` folder contains web app that was used during task creation, not used in ctf.

`test` folder contains solution.

### Solution
See `test` folder