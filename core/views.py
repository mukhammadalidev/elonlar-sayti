from django.shortcuts import render
from django.views import View
from advertisement.models import CategoryModel
# Create your views here.


class IndexView(View):
    def get(self,request):
        category = CategoryModel.objects.all()
        return render(request,'index.html',context={"categories":category})