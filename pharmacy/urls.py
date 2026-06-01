from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Medicines
    path('medicines/', views.medicines, name='medicines'),
    path('add-medicine/', views.add_medicine, name='add_medicine'),
    path('edit-medicine/<int:pk>/', views.edit_medicine, name='edit_medicine'),
    path('delete-medicine/<int:pk>/', views.delete_medicine, name='delete_medicine'),

    # Customers
    path('customers/', views.customers, name='customers'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('edit-customer/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('delete-customer/<int:pk>/', views.delete_customer, name='delete_customer'),

    # Suppliers
    path('suppliers/', views.suppliers, name='suppliers'),
    path('add-supplier/', views.add_supplier, name='add_supplier'),
    path('edit-supplier/<int:pk>/', views.edit_supplier, name='edit_supplier'),
    path('delete-supplier/<int:pk>/', views.delete_supplier, name='delete_supplier'),

    # Employees
    path('employees/', views.employees, name='employees'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('edit-employee/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:pk>/', views.delete_employee, name='delete_employee'),

    # Purchases
    path('purchases/', views.purchases, name='purchases'),
    path('add-purchase/', views.add_purchase, name='add_purchase'),
    path('edit-purchase/<int:pk>/', views.edit_purchase, name='edit_purchase'),
    path('delete-purchase/<int:pk>/', views.delete_purchase, name='delete_purchase'),

    # Sales
    path('sales/', views.sales, name='sales'),
    path('add-sale/', views.add_sale, name='add_sale'),
    path('edit-sale/<int:pk>/', views.edit_sale, name='edit_sale'),
    path('delete-sale/<int:pk>/', views.delete_sale, name='delete_sale'),

    # Reports
    path('reports/', views.reports, name='reports'),
]