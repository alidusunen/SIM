from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from datetime import date

from .models import Asset
from history.models import History
from custodians.models import Custodian
from categories.models import SubCategory, Category
from allocations.models import Allocation

# from .forms import AssetForm, AssignForm
from pages.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer', 'logassistant'])
def list_view(request):

    queryset = reversed(Asset.objects.all())
    context = {
        "object_list": queryset
    }
    return render(request, "list_view.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer', 'logassistant'])
def detail_view(request,asset_id):
    #Show method if exists:
    obj = get_object_or_404(Asset, id=asset_id)
    queryset = reversed(Allocation.objects.filter(assets=asset_id))

    context = {
        "object": obj,
        "object_list": queryset
    }
    return render(request, "asset_details.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer'])
def create_view(request):
    if request.method == "GET":
        queryset = SubCategory.objects.all()
        context ={
            "object": queryset
        }
        return render(request, "asset_create.html", context)
    if request.method == "POST":
        #Asset info
        c_tag = request.POST.get('tag_number')
        c_brand = request.POST.get('brand')
        c_model = request.POST.get('model')
        c_serial = request.POST.get('serial')
        c_description = request.POST.get('description')
        data = request.POST.get('sub_cat')
        c_sub_cat = SubCategory.objects.get(id=data)
        #User info
        c_location = request.POST.get('location')
        c_physical_location = request.POST.get('physical_location')
        c_condition = request.POST.get('condition')
        c_accessories = request.POST.get('accessories')
        #Purchase Info
        c_purchaseReferece = request.POST.get('purchaseReference')
        c_purchaseDate = request.POST.get('purchaseDate')
        c_price = request.POST.get('price')
        c_donor = request.POST.get('donor')
        c_budgetCode = request.POST.get('budgetCode')
        c_supplierName = request.POST.get('supplierName')
        c_comments = request.POST.get('comments')

        # Create Code
        new = Asset.objects.create(tag_number=c_tag,
                                   brand = c_brand,
                                   model = c_model,
                                   serial = c_serial,
                                   sub_category = c_sub_cat,
                                   description = c_description,
                                   price = c_price,
                                   location = c_location,
                                   physical_location = c_physical_location,
                                   condition = c_condition,
                                   accessories = c_accessories,
                                   donor = c_donor,
                                   budgetCode = c_budgetCode,
                                   purchaseReference = c_purchaseReferece,
                                   purchaseDate = c_purchaseDate,
                                   supplierName = c_supplierName,
                                   comments = c_comments)
        return redirect("/assets/list_view/", {})

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer'])
def update_view(request, asset_id):

    if request.method == 'POST':
        obj = get_object_or_404(Asset, id=asset_id)
        # Asset info
        obj.tag = request.POST.get('tag_number')
        obj.brand = request.POST.get('brand')
        obj.model = request.POST.get('model')
        obj.serial = request.POST.get('serial')
        obj.description = request.POST.get('description')
        data = request.POST.get('sub_cat')
        obj.sub_category = SubCategory.objects.get(id=data)
        # User info
        obj.location = request.POST.get('location')
        obj.physical_location = request.POST.get('physical_location')
        obj.condition = request.POST.get('condition')
        obj.accessories = request.POST.get('accessories')
        # Purchase Info
        obj.purchaseReferece = request.POST.get('purchaseReference')
        obj.purchaseDate = request.POST.get('purchaseDate')
        obj.price = request.POST.get('price')
        obj.donor = request.POST.get('donor')
        obj.budgetCode = request.POST.get('budgetCode')
        obj.supplierName = request.POST.get('supplierName')
        obj.comments = request.POST.get('comments')

        data = request.POST.get('custodian')
        # gets "custodian_id" from post data
        obj.custodian = Custodian.objects.get(id=data)
        # gets "custodian"

        obj.save()


        return redirect('assets:asset-detail', asset_id=asset_id)

    asset = get_object_or_404(Asset, id=asset_id)
    obj2 = Custodian.objects.all()
    obj3 = SubCategory.objects.all()
    context = {
        "object": asset,
        "custodian": obj2,
        "subcategory": obj3
    }
    return render(request, "asset_update.html", context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer', 'logassistant'])
def assign_view(request, asset_id):

    # gets the values of the URL
    if request.method == "GET":
        obj = get_object_or_404(Asset, id=asset_id)
        obj2 = Custodian.objects.all()
        context = {
            "object": obj,
            "custodian": obj2
        }
        return render(request, "asset_assign.html", context)

    # for posting the values of the URL
    if request.method == "POST":
        a_id = get_object_or_404(Asset, id=asset_id)
        #gets "asset"
        data = request.POST.get('custodian')
        #gets "custodian_id" from post data
        c_id = Custodian.objects.get(id=data)
        #gets "custodian"

        a_id.custodian = c_id                           #assigns id field of custodian to the asset's field
        a_id.save()

        ret = History.objects.create(asset_id=a_id, custodian_id=c_id) #creates history of the assignment

        return redirect('assets:asset-detail', asset_id=asset_id)




@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer', 'logassistant'])
def delete_view(request,product_id):
    #Show method if exists:
    obj = Asset.objects.get(id=product_id)
    #delete method:
    obj.delete()
    context = {
    }
    return render(request, "delete_view.html", context)



# Create your views here.
