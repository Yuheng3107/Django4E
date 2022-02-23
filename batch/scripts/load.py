import csv

from unesco.models import Category, State, Iso, Region, Site

def run():
    with open("unesco/load.csv") as file:
        reader = csv.reader(file)
        next(reader)

        Category.objects.all().delete()
        print("test")
        State.objects.all().delete()
        Iso.objects.all().delete()
        Region.objects.all().delete()
        Site.objects.all().delete()

        for row in reader:
            print(row)

            c, created = Category.objects.get_or_create(name=row[7])
            s, created = State.objects.get_or_create(name=row[8])
            i, created = Iso.objects.get_or_create(name=row[10])
            r, created = Region.objects.get_or_create(name=row[9])
            name = row[0]
            try:
                year = int(row[3])
            except:
                year = None
            try:
                latitude = float(row[5])
            except:
                latitude = None
            try: 
                longitude = float(row[4])
            except:
                longitude = None
            if row[1] == "":
                description = None
            else:
                description = row[1]
            if row[2] == "":
                justification = None
            else:
                justification = row[2]
            try:
                area_hectares = float(row[6])
            except:
                area_hectares = None
            site = Site(name=name, year=year, latitude=latitude, longitude=longitude, description=description, justification=justification, area_hectares=area_hectares, category=c, region=r, iso=i, state=s)
            site.save()



