from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.forms import PhotoForm
from django.contrib.auth.models import User

@login_required
def gallery(request):
    return render(request, "main/gallery.html", {'username': request.user.username})

@login_required
def upload(request):
    if request.method == 'POST':
        # user_id = request.POST[user]
        form = PhotoForm(request.POST, request.FILES)
        # initial = {'users': users}
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('gallery')
            # Get the current instance object to display in the template
            # img_obj = form.instance
            # return render(request, 'main/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = PhotoForm()
    return render(request, 'main/upload.html', {'form': form})