from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render,redirect
from . import forms,models
from django.shortcuts import get_object_or_404
from django.forms import formset_factory

# Create your views here.
@login_required
def home(request):

    photos = models.Photo.objects.all()
    blogs = models.Blog.objects.all()

    return render(request,'blog/home.html',{'photos':photos,'blogs':blogs})

@login_required
@permission_required('blog.add_photo')
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
@permission_required(['blog.add_photo', 'blog.add_blog'])
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

@login_required
@permission_required('blog.change_blog')
def edit_blog(request,blog_id):
    blog = get_object_or_404(models.Blog,id=blog_id)
    edit_form = forms.BlogForm(instance=blog)
    delete_form = forms.DeleteBlogForm()

    if request.method =='POST':

        if 'edit_blog' in request.POST:

            edit_form = forms.BlogForm(request.POST,instance=blog)

            if edit_form.is_valid():

                edit_form.save()
                
                return redirect('home')
            
        if 'delete_blog' in request.POST:

            delete_form = forms.DeleteBlogForm(request.POST)

            if delete_form.is_valid():

                blog.delete()

                return redirect('home')
            
    return render(request,'blog/edit_blog.html',{'edit_form':edit_form,'delete_form':delete_form})


@login_required
@permission_required('blog.add_photo')
def create_multiple_photos(request):

    PhotoFormSet = formset_factory(forms.PhotoForm, extra=5)
    formset = PhotoFormSet()
    if request.method == 'POST':
        formset = PhotoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
            return redirect('home')
    return render(request, 'blog/create_multiple_photos.html', {'formset': formset})