from django.http import HttpResponse
from django.shortcuts import render



def blog(request):
    para='''Ross Enamait’s website is dedicated to high performance conditioning, strength, and
            athletic development. The longtime trainer and boxing coach understands that a successful
            fitness regimen boils down to finding what works for you. His blog is a great resource for 
            information about different kinds of training — from fitness
            fundamentals to old-school workouts like jumping rope to philosophical riffs on mental endurance.'''
    
    
    c=0
    space=9
    content_blog=''

    for i in range(len(para)):
        if(c!=space):
            if(para[i]==' '):
                c+=1
            content_blog+=para[i]
        else:
            break
    content_blog=content_blog
    
    params={'blog':content_blog, 'author':'DB'}    
    
    
    return(render(request,'blog.html',params))



def about(request):
    return(render(request,'about.html'))
