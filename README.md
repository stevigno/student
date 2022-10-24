# student
 segeee projet

# Installations
Installation instructions are slightly different depending on whether you’re installing a distribution-specific package, downloading the latest official release, or fetching the latest development version.

## Installing an official release with pip
This is the recommended way to install Django.

1. Install [pip](https://pip.pypa.io/en/stable/). The easiest is to use the [standalone pip installer](https://pip.pypa.io/en/latest/installation/). If your distribution already has pip installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.

2. Take a look at [venv](https://docs.python.org/3/tutorial/venv.html). This tool provides isolated Python environments, which are more practical than installing packages systemwide. It also allows installing packages without administrator privileges.

3. After you’ve created and activated a virtual environment, enter the command:
``` py -m pip install Django ``` or  ```python -m pip install Django```

# StartProject
open the folder where you copied and enter the command:
```python manage.py runserver``` make sure you have activated the virtual environment.

You’ll see the following output on the command line:
```Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

October 24, 2022 - 15:50:53
Django version 4.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
