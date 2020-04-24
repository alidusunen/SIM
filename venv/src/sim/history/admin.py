from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .models import Custodian, History, Asset
from categories.models import Category, SubCategory
from allocations.models import Allocation
from disposals.models import Disposal
# Register your models here.

# CUSTODIAN

#Define the resource to be exported
class CustodianResource(resources.ModelResource):
    class Meta:
        model = Custodian


class CustodianAdmin(ImportExportModelAdmin):
    resources_class = CustodianResource

admin.site.register(Custodian, CustodianAdmin)

#CATEGORY
class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
class CategoryAdmin(ImportExportModelAdmin):
    resources_class = CategoryResource

admin.site.register(Category, CategoryAdmin)

#SUBCATEGORY
class SubCategoryResource(resources.ModelResource):
    class Meta:
        model = SubCategory
class SubCategoryAdmin(ImportExportModelAdmin):
    resources_class = SubCategoryResource

admin.site.register(SubCategory, SubCategoryAdmin)


# ASSET  There is an issue here probably a cashing issue
class AssetResource(resources.ModelResource):
    custodian = fields.Field(column_name = 'custodian', attribute = 'custodian',
        widget = ForeignKeyWidget(Custodian, 'name'))
    class Meta:
        model = Asset
        fields =['tag_number', 'description', 'custodian',]



class AssetAdmin(ImportExportModelAdmin, ExportMixin):
    resources_class = AssetResource


admin.site.register(Asset, AssetAdmin)
class VievAdmin(ImportExportModelAdmin):
    pass



admin.site.register(History)
admin.site.register(Disposal)
admin.site.register(Allocation)
