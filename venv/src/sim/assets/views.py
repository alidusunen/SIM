from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import UpdateView

from .models import Asset
from history.models import History
from custodians.models import Custodian

from .forms import AssetForm, AssignForm


def list_view(request):

    queryset = Asset.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, "list_view.html", context)

def detail_view(request,asset_id):
    #Show method if exists:
    obj = get_object_or_404(Asset, id=asset_id)

    context = {
        "object": obj
    }
    return render(request, "asset_details.html", context)

# Create View with Django Forms
def create_view(request):
    form = AssetForm(request.POST or None)
    if form.is_valid():
        form.save()
        
       #Resets the form to blank
        form = AssetForm()

    context = {
       'form': form
    }
    return render(request, "asset_create.html", context)

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
        print(request.POST)
        #Trying to redirect to listview here but its not the best way to do it.
        queryset = Asset.objects.all()
        context = {
            "object_list": queryset
        }
        return redirect("/assets/list_view/", context)



# class AssetAssignView(UpdateView):
#     template_name = 'asset_assign.html'
#     form_class = AssignForm
#     queryset = Asset.objects.all()
#
#     def get_object(self):
#         id_ = self.kwargs.get("asset_id")
#         return get_object_or_404(Asset, id=id_)
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
#
    # def create_history(self):
    #     if request.method == "POST":
    #         asset = self.kwargs.get("asset_id")
    #         data = request.POST
    #         ret = History.objects.create(asset_id=asset, custodian_id=data.custodian )
    #         return render(request, "list_view.html", context)








# def assign_view(request, asset_id):
#     obj = get_object_or_404(Asset, id=asset_id)
#     form = AssignForm(request.POST, instance=asset_id)
#     if form.is_valid():
#         form.save()
#         # Resets the form to blank
#         form = AssignForm()
#
#     context = {
#         'form': form,
#         'object': obj
#     }
#     return render(request, "asset_assign.html", context)




# #Delete view
# def delete_view(request,product_id):
#     #Show method if exists:
#     obj = Product.objects.get(id=product_id)
#     #delete method:
#     obj.delete()
#     context = {
#     }
#     return render(request, "delete_view.html", context)



# Create your views here.
