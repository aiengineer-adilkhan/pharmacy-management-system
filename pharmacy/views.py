from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine, Customer, Supplier, Employee, Purchase, Sale
from .forms import (
    MedicineForm,
    CustomerForm,
    SupplierForm,
    EmployeeForm,
    PurchaseForm,
    SaleForm
)
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_pharmacist(user):
    return user.groups.filter(name='Pharmacist').exists()

def is_cashier(user):
    return user.groups.filter(name='Cashier').exists()

def can_manage_medicines(user):
    return (
        user.groups.filter(name='Admin').exists()
        or user.groups.filter(name='Pharmacist').exists()
    )
def can_manage_purchases(user):
    return (
        user.groups.filter(name='Admin').exists()
        or user.groups.filter(name='Pharmacist').exists()
    )
def can_manage_sales(user):
    return (
        user.groups.filter(name='Admin').exists()
        or user.groups.filter(name='Pharmacist').exists()
        or user.groups.filter(name='Cashier').exists()
    )
def can_view_reports(user):
    return (
        user.groups.filter(name='Admin').exists()
        or user.groups.filter(name='Pharmacist').exists()
    )

def login_view(request):
    error = ""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid username or password"

    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    context = {
        'medicine_count': Medicine.objects.count(),
        'customer_count': Customer.objects.count(),
        'supplier_count': Supplier.objects.count(),
        'employee_count': Employee.objects.count(),
        'purchase_count': Purchase.objects.count(),
        'sale_count': Sale.objects.count(),
    }

    return render(request, 'dashboard.html', context)

# =========================
# MEDICINES CRUD
# =========================

@login_required
@user_passes_test(can_manage_medicines)
def medicines(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicines.html', {'medicines': medicines})


@login_required
@user_passes_test(can_manage_medicines)
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('medicines')

    else:
        form = MedicineForm()

    return render(request, 'add_medicine.html', {'form': form})


@login_required
@user_passes_test(can_manage_medicines)
def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)

        if form.is_valid():
            form.save()
            return redirect('medicines')

    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'add_medicine.html', {'form': form})


@login_required
@user_passes_test(can_manage_medicines)
def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    medicine.delete()
    return redirect('medicines')


# =========================
# CUSTOMERS CRUD
# =========================
@login_required
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customers')

    else:
        form = CustomerForm()

    return render(request, 'add_customer.html', {'form': form})

@login_required
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('customers')

    else:
        form = CustomerForm(instance=customer)

    return render(request, 'add_customer.html', {'form': form})


@login_required
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customers')


# =========================
# SUPPLIERS CRUD
# =========================
@login_required
@user_passes_test(is_admin)
def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers.html', {'suppliers': suppliers})


@login_required
@user_passes_test(is_admin)
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('suppliers')

    else:
        form = SupplierForm()

    return render(request, 'add_supplier.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def edit_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)

        if form.is_valid():
            form.save()
            return redirect('suppliers')

    else:
        form = SupplierForm(instance=supplier)

    return render(request, 'add_supplier.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def delete_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('suppliers')


# =========================
# EMPLOYEES CRUD
# =========================
@login_required
@user_passes_test(is_admin)
def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


@login_required
@user_passes_test(is_admin)
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employees')

    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employees')

    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'add_employee.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employees')


# =========================
# PURCHASES CRUD
# =========================

@login_required
@user_passes_test(can_manage_purchases)
def purchases(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchases.html', {'purchases': purchases})


@login_required
@user_passes_test(can_manage_purchases)
def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)

        if form.is_valid():
            purchase = form.save()

            medicine = purchase.medicine
            medicine.quantity += purchase.quantity
            medicine.save()

            return redirect('purchases')

    else:
        form = PurchaseForm()

    return render(request, 'add_purchase.html', {'form': form})


@login_required
@user_passes_test(can_manage_purchases)
def edit_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)

        if form.is_valid():
            form.save()
            return redirect('purchases')

    else:
        form = PurchaseForm(instance=purchase)

    return render(request, 'add_purchase.html', {'form': form})


@login_required
@user_passes_test(can_manage_purchases)
def delete_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    purchase.delete()
    return redirect('purchases')


# =========================
# SALES CRUD
# =========================

@login_required
@user_passes_test(can_manage_sales)
def sales(request):
    sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': sales})


@login_required
@user_passes_test(can_manage_sales)
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)

        if form.is_valid():
            sale = form.save()

            medicine = sale.medicine
            medicine.quantity -= sale.quantity
            medicine.save()

            return redirect('sales')

    else:
        form = SaleForm()

    return render(request, 'add_sale.html', {'form': form})


@login_required
@user_passes_test(can_manage_sales)
def edit_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)

    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)

        if form.is_valid():
            form.save()
            return redirect('sales')

    else:
        form = SaleForm(instance=sale)

    return render(request, 'add_sale.html', {'form': form})


@login_required
@user_passes_test(can_manage_sales)
def delete_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    sale.delete()
    return redirect('sales')


# =========================
# REPORTS
# =========================
@login_required
@user_passes_test(can_view_reports)
def reports(request):
    context = {
        'medicine_count': Medicine.objects.count(),
        'customer_count': Customer.objects.count(),
        'supplier_count': Supplier.objects.count(),
        'employee_count': Employee.objects.count(),
        'purchase_count': Purchase.objects.count(),
        'sale_count': Sale.objects.count(),
    }

    return render(request, 'reports.html', context)