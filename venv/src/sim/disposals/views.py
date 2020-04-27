from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Asset, Disposal
from pages.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['logco'])
def create_view(request):

    if request.method == "POST":
        #Allocation info
        c_documentNumber = request.POST.get('documentNumber')
        c_base = request.POST.get('base')
        c_date = request.POST.get('date')
        c_reason = request.POST.get('reason')
        c_comments = request.POST.get('comments')

        #Returns a query:
        c_assets = request.POST.getlist('assets')


        # Create Code
        new = Disposal.objects.create(documentNumber=c_documentNumber,
                                   date = c_date,
                                   base = c_base,
                                   reason = c_reason,
                                   comments = c_comments)

        #Passes the query of assets to new created Disposal
        new.assets.set(c_assets)

        return redirect("/disposals/", {})

    queryset = Asset.objects.all()
    context = {
        "objects": queryset
    }
    return render(request, "disposal_create.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer', 'logassistant'])
def list_view(request):

    queryset = reversed(Disposal.objects.all())

    context = {
        "object_list": queryset
    }
    return render(request, "disposal_listview.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer', 'logassistant'])
def detail_view(request,id):
    #Show method if exists:
    obj = get_object_or_404(Disposal, id=id)
    queryset = obj.assets.all()

    context = {
        "object": obj,
        "assets": queryset
    }
    return render(request, "disposal_detail.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco'])
def delete_view(request, id):
    obj = get_object_or_404(Disposal, id=id)
    obj.delete()
    return redirect('disposals:list-view')


