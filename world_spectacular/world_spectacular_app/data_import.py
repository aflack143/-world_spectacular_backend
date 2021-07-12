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
    with open(path, newline='') as file_obj:
        reader = csv.reader(file_obj)

        for row in reader:
            print(row[0])
            Country_Picture.objects.create(
                country_id = row[0],
                picture_url = row[1],
                picture_location = row[2],
                picture_photographer = row[3],
                picture_photographer_link = row[4],
                picture_source = row[5],
            ),