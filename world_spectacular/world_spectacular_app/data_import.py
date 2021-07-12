import csv
from .models import Country, Country_Picture

def load_csv_file(path):
    with open(path) as file_obj:
        reader = csv.reader(file_obj)

        for row in reader:
            Country.objects.create(
                country_name=row[0],
                country_code=row[1],
                wiki_link=row[2],
                anthem=row[3],
                globe_map=row[4],
            )

def load_country_picture_csv_file(path):
    with open(path) as file_obj:
        reader = csv.reader(file_obj)

        for row in reader:
            Country_Picture.objects.create(
                country = row['country'],
                picture_url = row['picture_url'],
                picture_location = row['picture_location'],
                picture_photographer = row['picture_photographer'],
                picture_photographer_link = row['picture_photographer_link'],
                picture_source = row['picture_source'],
            )