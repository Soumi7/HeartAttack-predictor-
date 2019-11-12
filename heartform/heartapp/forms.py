
from crispy_forms.layout import Layout,Submit
from crispy_forms.helper import FormHelper
from django import forms
#from .models import Snippet




class HeartForm(forms.Form):
    name= forms.CharField()
    age=forms.IntegerField(label='age')
    sex= forms.CharField()
    cp= forms.IntegerField()
    tres= forms.IntegerField()
    chol= forms.IntegerField()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.helper=FormHelper
        self.helper.form_method='POST'

        self.helper.layout=Layout(
            'name',
            'age',
            'sex',
            'cp',
            'tres',
            'chol',
            Submit('submit','Submit',css_class='btn-success')

        )

#class SnippetForm(forms.ModelForm):
    #class Meta:
     #   model= Snippet
      #  fields = ('name','age')