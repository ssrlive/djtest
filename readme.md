# begin

```
django-admin startproject djtest
```

# run
```
python3 manage.py runserver 0.0.0.0:8002
```

# mysql
create mysql database
```
pip3 install pymysql

mysql -u root -p

create database runoob default charset=utf8;
```

# create table
create a mysql database table
```
python3 manage.py migrate   # 创建表结构
python3 manage.py makemigrations test_model  # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate test_model   # 创建表结构
```
# create admin account
```
python manage.py createsuperuser
```

