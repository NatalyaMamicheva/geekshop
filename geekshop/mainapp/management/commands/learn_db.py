from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.db import connection
from django.db.models import Q
from adminapp.views import db_profile_by_type

class Command(BaseCommand):
   def handle(self, *args, **options):
       test_products = Product.objects.filter(
           Q(category__name='офис') |
           Q(category__name='модерн')
       )

       print(len(test_products))
       # print(test_products)

       db_profile_by_type('learn db', '', connection.queries)
