# Vitual Environtments In Python
Imagine a scenario where you are working on two web-based Python projects one of them uses **Django 4.0** and the other uses **Django 4.1** (check for the latest Django versions and so on). In such situations, we need to create a virtual environment in Python that can be really useful to maintain the dependencies of both projects.


>A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. 
---

## To create a virtual environment in Python
You can use the `venv` module that comes with Python. Here's an example of how to create a virtual environment and activate it:

### Create a virtual environment
```Python
python -m venv EnvironmentName

```
 
## Start Working/Activate the virtual environment (Linux/macOS)
```Bash
source EnvironmentName/bin/activate
```
 
### Activate the virtual environment (Windows)
```Bash
#In CMD
EnvironmentName\Scripts\activate.bat

#In PS
EnvironmentName\Scripts\activate.ps1
```


Once the virtual environment is activated, any packages that you install using `pip` will be installed in the virtual environment, rather than in the global Python environment. This allows you to have a separate set of packages for each project, without affecting the packages installed in the global environment.

## Deactivate the virtual environment
To deactivate the virtual environment, you can use the `deactivate` command:
```Bash
deactivate
```
---
## The `requirements.txt` file

In addition to creating and activating a virtual environment, it can be useful to create a `requirements.txt` file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

### To create a requirements.txt file
You can use the `pip freeze` command, which outputs a list of installed packages and their versions. For example:


 Output the list of installed packages and their versions to a file
```Bash
pip freeze > requirements.txt
```

### To install the packages listed in the requirements.txt file, you can use the pip install command with the `-r` flag:

Install the packages listed in the requirements.txt file
```Bash
pip install -r requirements.txt
```

>Using a virtual environment and a `requirements.txt` file can help you manage the dependencies for your Python projects and ensure that your projects are portable and can be easily set up on a new machine.