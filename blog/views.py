from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,UserPassesTestMixin
from django.views.generic import ListView , DetailView , CreateView ,UpdateView, DeleteView




def blog(request):
   
    
    context=Post.objects.all()
    all_content=[]
    
    for i in context:
        content=i.content

        #Conent Shortner
        c=0
        space=9
        content_blog=''
        
        for j in range(len(content)):
            if(c!=space):
                if(content[j]==' '):
                    c+=1
                content_blog+=content[j]
            else:
                break
        content_blog=content_blog
        all_content.append(content_blog)
        
    
    
    
    
    n=len(context)
    
    for i in range(n):
        print(context[i].title)
        print(all_content[i])
    
    params={'blog':all_content ,'context':context,'n':range(n)}    
    
    
    return(render(request,'blog.html',params))




class PostListView(ListView):
    model=Post
    template_name='blog.html'
    context_object_name='context'
    
class PostDetailView(DetailView):
    model=Post
    
class PostCreateView(CreateView,LoginRequiredMixin):
    model=Post
    fields=['title','content','date']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
class PostUpdateView(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    model=Post
    fields=['title','content','date']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
    
class PostDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model=Post
    success_url='/blog'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
    


def about(request):
    return(render(request,'about.html'))
