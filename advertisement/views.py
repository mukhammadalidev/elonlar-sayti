from django.views import View
from .models import Job
from django.shortcuts import render,get_object_or_404,redirect
from .forms import AdsEmployer
class AdvertismentView(View):
    def get(self,request,pk):
        products = Job.objects.filter(category__pk=pk)
      
   
     

        return render(request,'category/category.html',{"products":products})
    
class Job_DetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Job, pk=pk)
        

        return render(request, 'category/job_detail.html', {"product": product})



class AdsEmployerView(View):
    def get(self, request):
        form = AdsEmployer()
        return render(request, 'ads/add.html', {"form": form})

    def post(self, request):
        form = AdsEmployer(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            # Employerni request.user orqali tayinlaymiz
            try:
                ad.employer = request.user.employer
                print(request.user.employer)
            except AttributeError:
                # Agar employer profile yo'q bo'lsa, xatolik yoki redirect
                return redirect('users:profile')  

            ad.save()
            return redirect('home')  # saqlangach, asosiy sahifaga yo'naltirish
        return render(request, 'ads/add.html', {"form": form})