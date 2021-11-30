# CSE412-Project
GitHub repository for CSE 412 group prject relating to video game collections stored in a database

To use install django
```bash
pip3 install django
```
then run the server
```bash
python3 manage.py runserver
```
open up a browser window, default loading page is localhost and port 8000
```bash
http:127.0.0.1:8000
```
# Creating the database

First, install psycopg2
```bash
pip3 install psycopg2
```

Open makefile and change the makefile path to point to your CSE412-Project local directory
then run as 
```bash
make setup_postgres
```
If something doesn't go according to plan, run
```bash
make nuke
``` 
After creating the database, go to videoGameDB/settings.py
Go to the DATABASES fields and change the username to your default username

Run the following to migrate the django project onto our DB
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Then run the server using the command given above

user manual https://docs.google.com/document/d/1bspXe0Lj1ViW5pJcDnar6c6gAFNbjh_r8tZSRdaKAs0/edit?usp=sharing
