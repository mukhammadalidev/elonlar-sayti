from django import forms
from .models import Job

class AdsEmployer(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('category', 'title', 'description', 'salary', 'location', 'phone_number',)



# class EmloyerProfileForm(forms.ModelForm):
#     class Meta:
#         model = EmployerProfile
#         fields = ('company_name',)