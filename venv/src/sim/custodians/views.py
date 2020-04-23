from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Custodian
from pages.decorators import allowed_users

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer', 'logassistant'])
def view_custodians(request):
    queryset = Custodian.objects.all();
    context = {
        "object_list": queryset
    }
    return render(request, "view_custodians.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer', 'logassistant'])
def custodian_details(request, custodian_id):
    obj = get_object_or_404(Custodian, id=custodian_id)
    context = {
        "object": obj
    }
    return render(request, "custodian_details.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer'])
def custodian_create(request):
    if request.method == "GET":
        return render(request, "create.html", {})
    if request.method == "POST":
        c_name = request.POST.get('name')
        c_position = request.POST.get('position')
        c_base = request.POST.get('base')

        new = Custodian.objects.create(name=c_name, position=c_position, base=c_base)

        return redirect("/custodians/", {})

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer'])
def custodian_update(request, custodian_id):
    if request.method == "GET":
        obj = get_object_or_404(Custodian, id=custodian_id)
        context = {
            "object": obj
        }
        return render(request, "update_cust.html", context)

    if request.method == "POST":
        obj2 = get_object_or_404(Custodian, id=custodian_id)
        
        obj2.name = request.POST.get('name')
        obj2.position = request.POST.get('position')
        obj2.base = request.POST.get('base')
        obj2.save()
        return redirect("/custodians/", {})

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager'])
def custodian_delete(request,custodian_id):
    obj = get_object_or_404(Custodian, id=custodian_id)
    obj.delete()

    return redirect("/custodians/", {})