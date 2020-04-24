from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Asset, Allocation
from pages.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['logco'])
def create_view(request):

    if request.method == "POST":
        print(request.POST)
        #Asset info
        c_documentNumber = request.POST.get('documentNumber')
        c_date = request.POST.get('date')
        c_previousDonor = request.POST.get('previousDonor')
        c_previousBudget = request.POST.get('previousBudget')
        c_newDonor = request.POST.get('newDonor')
        c_newBudget = request.POST.get('newBudget')
        c_comments = request.POST.get('comments')

        #Returns a query:
        c_assets = request.POST.getlist('assets')


        # Create Code
        new = Allocation.objects.create(documentNumber=c_documentNumber,
                                   date = c_date,
                                   previousDonor = c_previousDonor,
                                   previousBudget = c_previousBudget,
                                   newDonor = c_newDonor,
                                   newBudget = c_newBudget,
                                   comments = c_comments)

        #Passes the query of assets to new created Allocation
        new.assets.set(c_assets)

        #Change the donor information to the allocation information
        for instance in c_assets:
            asset = get_object_or_404(Asset, id=instance)
            asset.donor = c_newDonor
            asset.budgetCode = c_newBudget
            asset.save()



        return redirect("/assets/list_view/", {})

    queryset = Asset.objects.all()
    context = {
        "objects": queryset
    }
    return render(request, "alloc_create.html", context)