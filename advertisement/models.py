from django.db import models
from users.models import CustomUser
# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=155)
    image = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title
    


class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='employer')
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='employers_logos/',null=True,blank=True)


    def __str__(self):
        return self.company_name

class Job(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name="jobs")
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=155)

    def __str__(self):
        return self.title
class AdvertisementModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=155)
    link = models.URLField()
    company = models.CharField(max_length=255,null=True,blank=True)
    job_time = models.CharField(max_length=255,default="9:00 dan 18:00")
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)



    def __str__(self):
        return self.title
    




class ApplyModel(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    advertisement = models.ForeignKey(AdvertisementModel,on_delete=models.CASCADE)
