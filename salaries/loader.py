import os, sys, string, csv, datetime, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "salaries.settings") 

from people.models import Person

from django.template.defaultfilters import slugify, urlize
from django.core.exceptions import ObjectDoesNotExist

reader = csv.reader(open("salaries1314.csv", "rU"), dialect=csv.excel)
reader.next()
for row in reader:
    try:
        sort = row[0]
        nom = row[1]
        nom_slug = slugify(nom)
        ttl = row[4]
        fname = row[3]
        lname = row[2]
        pnum = row[6]
        jclass = row[7]
        trm = row[8]
        fte = float(row[9])
        money = int(row[10])
        per, percreated = Person.objects.get_or_create(sort_id=sort, name=nom, name_slug=nom_slug, first_name=fname, last_name=lname, title=ttl, position_number=pnum, job_class_number=jclass, term=trm, fte_status=fte, salary=money)
        print per
    except:
        print "BOOOOOOOORRRRRRK!"
