from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.forms import PhotoForm, EditForm
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from main.models import Photo

@login_required
def gallery(request):
    user = request.user
    image = user.photo_set.all()
    return render(request, "main/gallery.html", {'username': request.user.username, 'image': image})

@login_required
def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('gallery')
    else:
        form = PhotoForm()
    return render(request, 'main/upload.html', {'form': form})

# @login_required
# def edit(request):
#     image = EditForm(instance=request.user.photo_set.objects.get(title='i.title'))
#     print('i.title:', image)
#     form = EditForm(request.POST, request.FILES)
#     # if request.method == 'POST':
#
#
#     return render(request, 'main/photo_form.html', { 'i.title': image, 'form': form })

class Edit(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['title', 'location', 'captured_date', 'image']
    success_url = '/gallery/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ImageDelete(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/gallery/'