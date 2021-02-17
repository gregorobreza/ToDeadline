from django import forms
from django.forms import ModelForm
from datetime import datetime
import pytz
from .models import Task, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'New category...', 'class':'form-control width100'}))


    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            match = Category.objects.get(name=name)

        except Category.DoesNotExist:
            return name

        raise forms.ValidationError("This category already exist!")

    class Meta:
        model = Category
        exclude = ['slug']


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...', 'class':'form-control'}))
    doto = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],widget=forms.DateTimeInput(attrs={'placeholder':'Select date and hour...', 'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Choose category")

    def clean_doto(self):
        doto = self.cleaned_data['doto']
        now = datetime.utcnow()
        now = pytz.utc.localize(now)
        if doto < now:
            raise forms.ValidationError("Deadline cannot be in the past!")
        return doto

    class Meta:
        model = Task
        exclude = ['finished']
        widgets = {'level': forms.RadioSelect(attrs={'class':'radio'})}