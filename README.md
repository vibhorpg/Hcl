# Hcl Assignment - Employee Management

Employee Management highlights the task that the rest api can perform with employee endpoints. This project is developed on python to enable support of different inbuild library and provide space for any future scope of development.

# Functionality supported!

  - Create a employee
  - Update a employee
  - Delete a employee
  - Get a single employee
  - Get all the employees
  - Get employees with pagination and sorting on custom field
  - Test all api's

### Tech

Employee Management uses a number of open source technologies to work properly:

* [Python] - Interpreted, high-level, general-purpose programming language
* [Docker] - Ultralite Virtual layer on OS
* [Sqllite] - Ultralite filesystem database
* [Git] - Code versioning system
* [Django] - python supported MVT architecture framework


And of course Employee Management itself is # Hcl
open source on GitHub.

### Installation

```sh
$ sudo git clone https://github.com/vibhorpg/Hcl.git
$ cd Hcl/
$ sudo docker-compose build
$ sudo docker-compose up -d
```

### Testing


From the root directory of project following commands need to be triggered for testing:

```sh
$ sudo docker exec -it django_server python manage.py test
```

### Api's

Following are the api's supported in this project. There is a postman collection also placed in the root directory of the project 

- Create a employee
```sh
Request Method :
    POST
Api :
    http://127.0.0.1:82/employee/
Param :
    first_name:fname10
    last_name:lname10
    email:fname.lname10@gmail.com
```

  - Update a employee
```sh
Request Method :
    PUT
Api :
    http://127.0.0.1:82/employee/<int:id>
Param :
    first_name:fname10
    last_name:lname10
    email:fname.lname10@gmail.com
```
  

  - Delete a employee
```sh
Request Method :
    DELETE
Api :
    http://127.0.0.1:82/employee/<int:id>
``` 
  
  - Get a single employee
```sh
Request Method :
    GET
Api :
    http://127.0.0.1:82/employee/<int:id>
``` 
  
  - Get all the employees
```sh
Request Method :
    GET
Api :
    http://127.0.0.1:82/employee
``` 
  
  - Get employees with pagination and sorting on custom field
```sh
Request Method :
    GET
Api :
    http://127.0.0.1:82/employee?page_size=2&page=1&ordering=id
Description :
    page_size - no of records to get in a single request
    page - which page of records need to be acquired 
    ordering - Key for ordering need to be specified with (-) symbol if needed
        e.g : Asc = -id
              Desc = id
              Here id is the key name to be sorted
```


Alternatively you can import postman collection also placed in the root directory of the project 

