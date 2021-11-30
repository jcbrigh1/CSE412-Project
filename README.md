# CSE412-Project
GitHub repository for CSE 412 group prject relating to video game collections stored in a database

To use, first make sure postgresql is installed on you computer

Then make sure django and psycopg2 are installed
```bash
pip3 install django psycopg2
```
Then create the database
```bash
make setup_postgres
```
If the above doesn't work, you may need to add the following environment variables
```
export PGPORT=8888
export PGPATH=/tmp
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
then run the server
```bash
python3 manage.py runserver
```
open up a browser window, default loading page is localhost and port 8000
```bash
http:127.0.0.1:8000
```
user manual https://docs.google.com/document/d/1bspXe0Lj1ViW5pJcDnar6c6gAFNbjh_r8tZSRdaKAs0/edit?usp=sharing
