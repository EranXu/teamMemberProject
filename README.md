# Team Member Project
a mobile app by `Django`, `MySQL` and `HTML`, using python virtual environment.

## Estimated Time
15 hrs

5 hrs / day (Dec.11 - Dec.13) 

## About
Although there is no deadline for this project, I want to complete it as quickly as possible. It is a pity that my semester enters the final week, so I can only use the weekend time to do this totally new project for me.

I know the cost time may be very long, because I started from 0, and I recorded all the problems I encountered. Almost every problem allows me to deal with more than 1 hour. But I finally finished it:)

I really hope you can see my attitude and my sincerity. I can do my best to learn the unknown knowledge. This is my attitude. I hope you can give me a chance to prove myself.

## Bug Log

### Dec. 11 venv can't execute manage.py

problem code: 

```
python manage.py startapp xx
python3 manage.py startapp xx
```

solution: 

`python3.8 manage.py startapp xx`


---

### Dec.11 pip can't install phonenumberfiled

problem code:

`pip install django-phonenumber-filed[phonenumbers]`

solution:

`pip install 'django-phonenumber-filed[phonenumbers]`

---

### Dec.11 venv can't install restframework

problem code:

`python -m pip install djangorestframework`

solution:

```
python3 -m venv env
source ./env/bin/activate    // start again
python3.8 -m pip install djangorestframework
```

---

### Dec.12 ordering can't recognize the var

problem code:

```
canDelete = False
...
ordering = ['canDelete']
```

solution:

```
canDelete = models.BooleanField(..)
...
ordering = ['canDelete']
```

---

### Dec.12 Error: port 8000 are in use

solution:

`python3.8 manage.py runserver 8080    // can be various port, or kill`

---

### Dec.13 there's no module called: pymysql

problem:

Anaconda in base, although pip install, VSCode can't find the site-package

solution:

pip install in env and runserver in env

---

### Dec.13 canDelete can't be transit from POST response

problem code:

in view.py

`canDelete = request.POST['canDelete']`

solution:

`canDelete = request.POST.get('canDelete', False)   // because it's a boolean filed`

---

### Dec.13 Exception: MultiDictKey - Several buttons in edit page

problem code:

```
if request.POST.has_key('update'):

if request.POST.has_key('delete'):
```

solution:

Python3 delete the function: has_key!

```
if 'update' in request.POST:

if 'delete' in request.POST:
```


## Further Upgrade

design radio_customer

write unittest

add can't delete hint message

add more pages
