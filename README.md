# Test Task Python School

Test task is a creation of REST API for drivers and vehicles.

### Installation

To make sure your Python installation is functional, you can open a terminal window and type python3 or just python

`$ python3`

Python version should be >= 3.9.0

### Creating a directory where the project will live
```
$ git clone git@github.com:norka2233/test_task_python_school.git
$ cd test_task_yalantis
```
Create Python virtual environment

```
$ python3 -m venv venv
```

Activate the environment

```
source venv/bin/activate
```

Now you should see the name of your environment ('venv' in my case) in the beginning of every row in your Terminal

`(venv) $ _`

### Install python dependencies

```(venv) $ pip install -r requirements.txt```

### Set Flask variables

```commandline
$ export FLASK_APP=test_task.py
$ export FLASK_ENV=development
```

### Usage
Launch the application with the following command:
```commandline
(venv) $ flask run
```