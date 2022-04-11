### Introduction

![drf-icon.jpg](static/drf-icon.jpg)

In the next course I would like you learn how to get CRUD in Django with REST Framework,
the standard instrument for creating APIs with Django, and for the second, with Python.<br>

The minimal requirements are:
* Install the latest version for Python3.
* Text Editor. If you are just starting, recommend PyCharm Community Edition o VSCode with Python plugin.
* Access to a terminal (which exists in PyCharm).

The purposes which should be reached are fundamental for every API(examples):
* Endpoint for _list_ of books.
* Endpoint for _details_ of particular book.
* Endpoint for _creating_ a book.
* Endpoint for _updating_ existed book.
* Endpoint for _deleting_ existed book.
* Create tests for all Endpoints which provides the functionality for any circumstances.

If you are curious and want to check the results you may open the terminal.
Then you may investigate the copy of the code on the server side.

#### List of the books

```commandline
curl  https://example-of-crud-in-django-jrf.herokuapp.com/api/book/
```

> Output

```commandline
[{
   "id":1,
   "title":"Things Fall Apart",
   "country":"Nigeria",
   "year":1958,
   "author":"Chinua Achebe",
   "created_at":"2022-04-11T02:30:26.684123",
   "updated_at":"2022-04-11T02:30:26.684134"
},
{
   "id":2,
   "title":"Fairy tales",
   "country":"Denmark",
   "year":1836,
   "author":"Hans Christian Andersen",
   "created_at":"2022-04-11T02:30:26.688126",
   "updated_at":"2022-04-11T02:30:26.688134"
}
...]
```

#### Get the details of the book

```commandline
curl https://example-of-crud-in-django-jrf.herokuapp.com/api/book/1/
```
> Output
```commandline
{
   "id":1,
   "title":"Things Fall Apart",
   "country":"Nigeria",
   "year":1958,
   "author":"Chinua Achebe",
   "created_at":"2022-04-11T02:30:26.684123",
   "updated_at":"2022-04-11T02:30:26.684134"
}
```

#### Create the book

```commandline
curl -XPOST -H "Content-type: application/json" -d 
'{"title": "Don Clojure de la mancha, el ingenioso lenguaje del parentesis", 
"country": "Spain", "author": "Andros Fenollosa Hurtado", "year": "2021"}' 
https://example-of-crud-in-django-jrf.herokuapp.com/api/book/
```

> Output
```commandline
{
   "id":1505,
   "title":"Don Clojure de la mancha, el ingenioso lenguaje del parentesis",
   "country":"Spain",
   "year":2021,
   "author":"Andros Fenollosa Hurtado",
   "created_at":"2022-04-11T21:23:25.406661",
   "updated_at":"2022-04-11T21:23:25.406680"
}
```

#### Update the book

```commandline
curl -XPUT -H "Content-type: application/json" -d 
'{"title": "Don Clojure de la mancha, el ingenioso lenguaje del parentesis", 
"country": "Spain", "author": "Andros Fenollosa", "year": "2021"}' 
https://example-of-crud-in-django-jrf.herokuapp.com/api/book/1505/
```

> Output
```commandline
{
   "id":1505,
   "title":"Don Clojure de la mancha, el ingenioso lenguaje del parentesis",
   "country":"Spain",
   "year":2021,
   "author":"Andros Fenollosa",
   "created_at":"2022-04-11T21:23:25.406661",
   "updated_at":"2022-04-11T21:26:36.580930"
}
```

#### Delete the book

```commandline
curl -XDELETE https://example-of-crud-in-django-jrf.herokuapp.com/api/book/1/
```

> Output
```commandline
{
   "id":null,
   "title":"Things Fall Apart",
   "country":"Nigeria",
   "year":1958,
   "author":"Chinua Achebe",
   "created_at":"2022-04-11T02:30:26.684123",
   "updated_at":"2022-04-11T02:30:26.684134"
}
```

#### Check that the server is active

```commandline
curl https://example-of-crud-in-django-jrf.herokuapp.com/ping/
```

> Output
```commandline
{"ping": "pong!"}
```

If you get lost on any step, do not hesitate to consult or download the code which was placed in GtHub repository:
https://github.com/tanrax/example-of-crud-in-django-with-rest-framework

Are you ready? Let's begin!