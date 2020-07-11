from django.contrib import admin

from transactions.models import Transactions, Categories, BusinessGroups, Accounts


class TransactionsAdmin(admin.ModelAdmin):

    readonly_fields = ('created_by', 'created_timestamp',
                       'updated_by', 'updated_timestamp')

    def save_model(self, request, obj, form, change):

        if not obj.created_by_id:
            obj.updated_by = request.user
            obj.created_by = request.user
        obj.save()


class BusinessGroupsAdmin(admin.ModelAdmin):

    readonly_fields = ('created_by', 'created_timestamp',
                       'updated_by', 'updated_timestamp')

    def save_model(self, request, obj, form, change):

        if not obj.created_by_id:
            obj.updated_by = request.user
            obj.created_by = request.user
        obj.save()


class AccountsAdmin(admin.ModelAdmin):

    readonly_fields = ('created_by', 'created_timestamp',
                       'updated_by', 'updated_timestamp')

    def save_model(self, request, obj, form, change):

        if not obj.created_by_id:
            obj.created_by = request.user
            obj.updated_by = request.user
        obj.save()


class CategoriesAdmin(admin.ModelAdmin):

    readonly_fields = ('created_by', 'created_timestamp',
                       'updated_by', 'updated_timestamp')

    def save_model(self, request, obj, form, change):

        if not obj.created_by_id:
            obj.created_by = request.user
            obj.updated_by = request.user
        obj.save()


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(BusinessGroups, BusinessGroupsAdmin)
admin.site.register(Accounts, AccountsAdmin)
