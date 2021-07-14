# World Spectacular (Django-backend)

[Link for Frontend React Repository](https://github.com/aflack143/world_spectacular_frontend)<br>
[Link for Backend Django Repository](https://github.com/aflack143/world_spectacular_backend)


Sources: 
[Setting up environment variables](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)
[CSV Seeder into postgres from Django](https://stackoverflow.com/questions/55169081/python-django-import-data-to-postgres) 

```js
## To begin seeding the CSV into Postgres from Django
# to start shell
> py manage.py shell

# to import and load csv file data
>>> from world_spectacular_app.data_import import load_csv_file
>>> load_csv_file("country.csv")

>>> from world_spectacular_app.data_import import load_country_picture_csv_file
>>> load_country_picture_csv_file("country_picture.csv")
````