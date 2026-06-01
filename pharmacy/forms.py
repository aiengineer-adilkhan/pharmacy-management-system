from django import forms
from .models import (
    Medicine,
    Customer,
    Supplier,
    Employee,
    Purchase,
    Sale
)


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'