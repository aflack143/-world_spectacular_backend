# World Spectacular (Django-backend)

[Link for Frontend React Repository](https://github.com/aflack143/world_spectacular_frontend)<br>
[Link for Backend Django Repository](https://github.com/aflack143/world_spectacular_backend)

## Description:
An application that allows a user to search for countrys in multiple search methods, providing demographic pages for each country. Available photo galley, and user profile after logging in from an email authentication program (Auth0)

## Getting Started:
Project planning and deciding on creating my own models or using an API. I found a country information API and decided to use the API and create my own model for extra contry information.

![image](https://user-images.githubusercontent.com/80013194/125966953-7bcd553f-90d3-47e0-a193-50cd6cc0f986.png)


## Technologies Used (backend):
  Django, Postgres, Cors
  
### Sources:
[Setting up environment variables](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)<br><br>
[CSV Seeder into postgres from Django](https://stackoverflow.com/questions/55169081/python-django-import-data-to-postgres) 
<br>Below is the code to load the CSV files:
```js
# to start shell
> py manage.py shell

# to import and load csv files:
>>> from world_spectacular_app.data_import import load_csv_file
>>> load_csv_file("country.csv")

>>> from world_spectacular_app.data_import import load_country_picture_csv_file
>>> load_country_picture_csv_file("country_picture.csv")
````
