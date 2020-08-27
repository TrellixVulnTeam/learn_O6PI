from django.contrib import admin
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from .models import Choice, Question, Product, Category, Member, Book, Author
from .views import index

# Register your models here.
"""
class MyAdminSite(AdminSite):

     def get_urls(self):
         from django.urls import path
         urls = super().get_urls()
         urls += [
             path('my_view/', self.admin_view(index))
         ]
         return urls

     def my_view(self, request):
         return HttpResponse("Hello!")

admin_site = MyAdminSite()


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class UserInline(admin.StackedInline):
    model = User
    extra = 1


"""



admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Book)
admin.site.register(Author)
admin.site.site_header = "Hello World"