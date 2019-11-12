
from django.shortcuts import render
from django.http import HttpResponse
from .forms import HeartForm #SnippetForm

import pickle
pickle_in=open('model (1).pickle','rb')
model= pickle.load(pickle_in)



def contact(request):
    if request.method=='POST':
        form=HeartForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            sex=form.cleaned_data['sex']
            tres = form.cleaned_data['tres']
            cp = form.cleaned_data['cp']
            chol = form.cleaned_data['chol']



            age_scaled = (age - 54.366337) / 9.082101
            tres_scaled = (tres - 131.623762) / 17.538143
            chol_scaled = (chol - 246.264026) / 51.830751
            sex_0 = 0
            sex_1 = 0
            chol_0 = 0
            chol_1 = 0
            chol_2 = 0
            chol_3 = 0
            if sex == 'male':
                sex_1 = 1
            else:
                sex_0 = 1

            if chol == 0:
                chol_0 = 1

            elif chol == 1:
                chol_1 = 1

            elif chol == 2:
                chol_2 = 1

            else:
                chol_3 = 1

            pred = model.predict([[age_scaled, tres_scaled, chol_scaled, sex_0, sex_1, chol_0, chol_1, chol_2, chol_3]])

            if pred[0]==0:
                return render(request,"yes.html",{'form': form})
            else:
                return render(request,"no.html",{'form': form})

    form= HeartForm()
    return render(request,"form.html",{'form': form})

def snippet_detail(request):

    if request.method=='POST':
        form=SnippetForm(request.POST)
        if form.is_valid():
            form.save()


    #form= SnippetForm()
    #return render(request,"form.html",{'form': form})