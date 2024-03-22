from django.test import TestCase
from core.erp.models import Type

# Create your tests here.

query = Type.objects.all()
print(query)