from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import History
from assets.models import Asset
from custodians.models import Custodian


# Generates Asset reports based on seleceted dropdown
@login_required(login_url='login')
def reports_main(request):
        return render(request, "reports_main.html", {})

@login_required(login_url='login')
def generate_asset(request):
    if request.method == "GET":
        query_asset = Asset.objects.all()
        context = {
            "asset_list": query_asset,
        }
        return render(request, "generate_asset.html", context)

    if request.method == "POST":
        data = request.POST['asset']
        a_id = Asset.objects.get(id=data)
        print(request.POST)

        return HttpResponseRedirect(reverse('reports:report-asset', args=[a_id.pk] ) )

# Generates Custodian reports based on seleceted dropdown
@login_required(login_url='login')
def generate_custodian(request):
    if request.method == "GET":
        query_custodian = Custodian.objects.all()
        context = {
            "custodian_list": query_custodian
        }
        return render(request, "generate_custodian.html", context)

    if request.method == "POST":
        data = request.POST['custodian']
        a_id = Custodian.objects.get(id=data)
        print(request.POST)

        return HttpResponseRedirect(reverse('reports:report-custodian', args=[a_id.pk] ) )


# # for posting the values of the URL
#     if request.method == "POST":
#         a_step = request.POST.get('asset')
#         # gets "asset_id" from post data
#         a_id = Custodian.objects.get(id=a_step)
#         # gets "asset"
#
#         c_step = request.POST.get('custodian')
#         #gets "custodian_id" from post data
#         c_id = Custodian.objects.get(id=c_step)
#         #gets "custodian"
#         print(request.POST)
#         return render(request, "home.html", {})

@login_required(login_url='login')
def report_custodian(request, custodian_id):
    queryset = reversed(History.objects.filter(custodian_id=custodian_id))
    #Get the first item in the queryset for page title purposes
    cust_name = get_object_or_404(Custodian, id=custodian_id)
    context = {
        "object_list": queryset,
        "cust_name": cust_name
    }
    return render(request, "report_custodian.html", context)

@login_required(login_url='login')
def report_asset(request, asset_id):
    queryset = reversed(History.objects.filter(asset_id=asset_id))
    ast_name = get_object_or_404(Asset, id=asset_id)
    context = {
        "object_list": queryset,
        "ast_name": ast_name
    }
    return render(request, "report_asset.html", context)

