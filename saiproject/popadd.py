import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','saiproject.settings')
import django
django.setup()

from faker import Faker
from random import randint,random
from testapp.models import School,College,Degree
fake=Faker()
#a=('jmhs','kakatiya','oxford','poiner','janapriya')
#a=('sri gayatri','narayana','royal','gayatri jc')
a=('siddartha','idle','dr ambedkar','mantra','osmania')
def populate(n):
    for i in range(n):
        sno=randint(1,500)
        sname=fake.name()
        sclass=randint(1,3)
        if sclass==1:
            sclass=str(sclass)+'st'
        elif sclass==2:
            sclass=str(sclass)+'nd'
        elif sclass==3:
            sclass=str(sclass)+'rd'
        else:
            sclass=str(sclass)+'th'
        sadr=fake.address()
        scl=fake.random_element(a)
        Degree.objects.get_or_create(sno=sno,sname=sname,sclass=sclass,sadr=sadr,degree=scl)
n=int(input('enter the num of students:'))
populate(n)
print(f'{n} records are entered')