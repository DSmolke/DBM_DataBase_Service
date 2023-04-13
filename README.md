# TESTS

#### 1. Make sure your docker is running and port 3306 is empty
2. Clone repository:
```angular2html
    git clone https://github.com/DSmolke/DBM_DataBase_Service.git
    cd DBM_DataBase_Service
```
3.Enter /tests package, create virtual env using poetry
```angular2html
    cd tests
    poetry update
```
*update protects from decoding errors

4. Enter shell and run pytest(takes around 15s because of database and .env files)
```angular2html
    poetry shell
    poetry run pytest -vv
```















# TEST RELEASE

https://pypi.org/project/dbm-database-service/

