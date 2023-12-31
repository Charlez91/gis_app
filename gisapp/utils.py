import json
from pathlib import Path
from django.contrib.gis.geos import fromstr


DATA_FILENAME = 'data.json'
def load_data(apps, schema_editor):
    Shop = apps.get_model('gisapp', 'Shop')
    #jsonfile = Path(__file__).resolve().parents.parent / DATA_FILENAME
    jsonfile = DATA_FILENAME
    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name','no-name')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    Shop(name=name, location = location).save()
            except KeyError:
                pass 