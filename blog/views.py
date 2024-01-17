from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from . import forms,models
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def home(request):

    photos = models.Photo.objects.all()
    blogs = models.Blog.objects.all()

    return render(request,'blog/home.html',{'photos':photos,'blogs':blogs})

@login_required
def photo_upload(request):

    form = forms.PhotoForm()

    if request.method =='POST':

        form = forms.PhotoForm(request.POST,request.FILES)
        
        if form.is_valid():

            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
        
    return render(request,'blog/photo_upload.html',{'form':form})

@login_required
def photo_profil_upload(request):

    form = forms.PhotoForm()

    if request.method =='POST':

        form = forms.PhotoForm(request.POST,request.FILES)
        
        if form.is_valid():

            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
        
    return render(request,'blog/photo_profil_upload.html',{'form':form})

@login_required
def blog_and_photo_upload(request):

    form_blog = forms.BlogForm()
    form_photo = forms.PhotoForm()

    if request.method =='POST':

        form_blog = forms.BlogForm(request.POST)
        form_photo = forms.PhotoForm(request.POST,request.FILES)
        
        if any([form_blog.is_valid(),form_photo.is_valid()]):

            photo = form_photo.save(commit=False)
            photo.uploader = request.user
            photo.save()

            blog = form_blog.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()

            return redirect('home')
        
   
    return render(request,'blog/create_blog_post.html',{'form_photo':form_photo,'form_blog':form_blog})

@login_required
def view_blog(request,blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'blog/view_blog.html', {'blog': blog})