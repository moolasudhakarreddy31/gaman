import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SudhakarJobsInfo.settings')
import django
django.setup()

from JobsInfo.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+ str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.email()
        ftitle=fake.random_element(elements=('Project manager','Team Lead','Software Enginner'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=fake.phonenumber()
        hydjobs_records=hydjobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,

        )
populate(25)

