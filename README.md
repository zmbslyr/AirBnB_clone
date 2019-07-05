# 0x00. AirBnB clone - The console

## Project Overview

Description of the project

The goal of the project is to deploy on a server a simple copy of the AirBnB website.


What you should learn from this project:

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---

This Project Included the Following Tasks:

### [1. Be PEP8 compliant!](./tests/)
* Write beautiful code that passes the PEP8 checks.


### [2. Unittests](./models/base_model.py)
* All your files, classes, functions must be tested with unit tests


### [3. BaseModel](./models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes:


### [4. Create BaseModel from dictionary](./models/engine/file_storage.py)
* Previously we created a method to generate a dictionary representation of an instance (method to_dict()).


### [5. Store first object](./console.py)
* Now we can recreate a BaseModel from another one by using a dictionary representation:


### [6. Console 0.0.1](./console.py)
* Write a program called console.py that contains the entry point of the command interpreter:


### [7. Console 0.1](./models/user.py)
* Update your command interpreter (console.py) to have these commands:


### [8. First User](./models/state.py)
* Write a class User that inherits from BaseModel:


### [9. More classes!](./console.py)
* Write all those classes that inherit from BaseModel:


### [10. Console 1.0](./console.py)
* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review


### [11. All instances by class name](./console.py)
* Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().


### [12. Count instances](./console.py)
* Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().


### [13. Show](./console.py)
* Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).


### [14. Destroy](./console.py)
* Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).


### [15. Update](./console.py)
* Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).


### [16. Update from dictionary](./tests/test_console.py)
* Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).

---

## Command Interpreter Description, Usage and Examples:

* Description of the command interpreter:

The command interpreter manipulates data without a visual interface, which eases developmentand debugging.


* How to use it

The command interpreter can be used to create, manipulate, serialize/deserialize and destroy class objects (i.e. BaseModel, User, State, Amenity, City, Place, and Review - which allow for the management and maintenance of the objects that comprise the HBnB Database.


*Examples

### How to start console (launches the prompt)
```
./console.py
```
### How to create a User Object (prints the id of the new object)
```
(hbnb) create User
```
### How to display a specific object (displays a string represntation of\
the object)
```
(hbnb) show User [object id]
```
### How to display all objects or all object of a specific class (displays list)
```
(hbnb) all
```
or
```
(hbnb) all User
```
### How to destroy a User object (deletes object)
```
(hbnb) destroy User [object id]
```

---

## Authors
* **Ty Edge** - [tyedge](https://github.com/tyedge)
* **Mark Hedgeland** - [zmbslyr](https://github.com/zmbslyr)