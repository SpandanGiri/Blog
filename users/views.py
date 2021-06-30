from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm



def register(request):
    form=UserRegisterForm()
    

    if(request.method=='POST'):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Account created for {username}')
            return redirect('http://127.0.0.1:8000/blog/')
            
    else:
        form=UserRegisterForm()
        
        
    return render(request, 'users/register.html',{'form':form})
