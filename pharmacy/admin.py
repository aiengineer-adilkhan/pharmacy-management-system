from django.contrib import admin
from .models import (
    Medicine,
    Customer,
    Supplier,
    Employee,
    Purchase,
    Sale
)

admin.site.register(Medicine)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Employee)
admin.site.register(Purchase)
admin.site.register(Sale)