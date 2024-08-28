from django.contrib import admin
from credit.models import Contract, CreditRequest, Producer, Product

# Register your models here.
class ContractAdmin(admin.ModelAdmin):
    pass

class CreditRequestAdmin(admin.ModelAdmin):
    pass

class ProducerAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contract, ContractAdmin)
admin.site.register(CreditRequest, CreditRequestAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Product, ProductAdmin)

