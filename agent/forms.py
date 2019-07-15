from django import forms
from .models import User, Building, House
# from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()
class CreateUserForm(forms.ModelForm):

    class Meta:
        model = User
        # fields = ['first_name','last_name','email']
        exclude=[]

class UploadPicForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('image',)
        # exclude=[]


class CreateBuildingForm(forms.ModelForm):

    class Meta:
        model = Building
        fields = ('building_name','building_location','street','plot_number',)

class CreateHouseForm(forms.ModelForm):

    class Meta:
        model = House
        fields = ('house_type','house_floor','name','vacant','building')       



   
