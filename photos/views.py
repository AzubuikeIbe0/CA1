from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# Create your views here.
#class PhotoCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
 #   model = Photo
 #   fields = ('title', 'category')
#    template_name = 'add.html'

#    def form_valid(self, form): 
 #       form.instance.author = self.request.user
 #       return super().form_valid(form)

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


def addPhoto(request):
    categories = Category.objects.all()


    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        elif data['new-location'] != '':
            category, created = Category.objects.get_or_create(name=data['new-location'])
        
        else: 
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image = image,
        )
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)


class editPhoto(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = ('title', 'category', 'image', 'description' )
    template_name = 'photo_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class deletePhoto(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photo_delete')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

