from django.views import View
from .models import Job
from django.shortcuts import render,get_object_or_404

class AdvertismentView(View):
    def get(self,request,pk):
        products = Job.objects.filter(category__pk=pk)
      
   
     

        return render(request,'category/category.html',{"products":products})
    
class Job_DetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Job, pk=pk)
        

        return render(request, 'category/job_detail.html', {"product": product})
