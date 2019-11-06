Make sure you have Django and Python installed before trying to run our web application.
Once installed, clone this repository, open Terminal and navigate to the directory. To run the server locally, type the following command in the command line while inside the projectEnergy directory.
```
python3 manage.py runserver
```
Check out the website at the dedicated ```localhost``` address. For administrative use, add "/admin" to the URL and login with
username: projectEnergy
password: projectEnergy

You can play around with the data models we have, you can add some instances. Enjoy!

Note: after pulling current repository from git, run the following two commands to synchronize the database:
```python3 manage.py makemigrations```

```python3 manage.py migrate```
