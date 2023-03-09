
## REST API application  
- Приложение на python, с использованием Flask, которое слушает на порту 8080 и принимает только методы GET, POST, PUT.

- Создаем значение ключ(равно)значение, изменяем ключ(равно)новое_значение, читаем значение ключа.
 
- Вновь созданные объекты должны создаваться, изменяться и читаться из NoSQL DB.
### Technology stack
- Python 3.10,  Redis DB, Flask.

## Install and Run the Project
[Project deployed here](http://78.27.236.114:8080/flask)

### - Case how to start from IDE (Pycharm)
Start Redis in redis-cli :
```shell
sudo apt-get update
sudo apt-get install redis
redis-cli ping  # check connection ->PONG
```
Clone Project and install dependencies:
```shell
git clone https://github.com/Vitalikys/test_DocuSt.git
cd test_DocuSt/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 wsgi.py
```

visit -  http://127.0.0.1:8080

### - Case how to start in Docker
```shell
git clone https://github.com/Vitalikys/test_DocuSt.git
docker compose up -d --build 
```

## Use the Project
you could send curl request from bash comadline to host:
* GET all key:values from Redis database 
```shell
curl --location --request GET 'http://78.27.236.114:8080//flask'
```
* GET one specific Key:Value
```shell
curl --location --request GET 'http://78.27.236.114:8080//flask//key_08'
```

* GET one specific Key:Value (key doesn't exist -> got Exception)
```shell
curl --location --request GET 'http://78.27.236.114:8080//flask//key_08-bla-'
```

* Create POST Key:Value  (key_09: value_09)
```shell
curl -X POST  - 'http://78.27.236.114:8080/flask/key_08' \
-H 'Content-Type: application/json' --data '{"value": "value 08"}'
```

* Update PUT - Key:Value  (key_09: value_09)
```shell
curl -X PUT 'http://78.27.236.114:8080/flask/key_09' \
-H 'Content-Type: application/json' --data '{"value": "new value 0999"}'
```

## Test Project
Test by using Unittest - IN Progress....

Best way to test application:
<a href="https://lively-escape-146551.postman.co/workspace/flask_Docu_Stech~1327aacd-5646-4d79-8df7-087fa63c2403/collection/23239505-05b3298c-edd2-46c5-a4e1-21c72a4a6cf0?ctx=documentation"> 
test with Postman </a>


![img.png](img.png)


## Script for monitoring memory usage
* script 1: memory_alarm.py 

how to run: 

```shell
python3 memory_alarm.py --url 'http://78.27.202.55:8080/flask' --time 60 --message 'short message'
```

```shell
python3 memory_alarm.py --help 
```


```shell
curl --location --request POST 'http://78.27.202.55:8080/flask/key_08' --header 'Content-Type: application/json' --data-raw '{"value": "value 08-"}'
```

Using the classic memory profiler
pip install -U memory_profiler

* Bash script version 1, 2 - details in readme_RAM.md
