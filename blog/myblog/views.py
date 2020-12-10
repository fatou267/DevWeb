from django.shortcuts import render, redirect, get_object_or_404
from .models import Publication
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import PublicationForms, LoginForm, SignUpForm, UserUpdateForm, ProfileUpdateForm

#from django.http import HttpResponse


# Create your views here.
#cette vue correspond à la page d'accueil de Myblog
def home(request):
	posts = Publication.objects.filter(archive=False, date_publication__lte=timezone.now()).order_by('date_publication')	
	return render(request, 'myblog/index.html', {'posts': posts})
#@login_required
def articles(request):
	posts = Publication.objects.filter(acteur=request.user,archive=False, date_publication__lte=timezone.now()).order_by('date_publication')
	return render(request, 'myblog/index.html', {'posts':posts})

def detail(request, pk):
	post = get_object_or_404(Publication, pk=pk)

	return render(request, 'myblog/detail.html', {'post': post})
@login_required
def new_pub(request):
	if request.method == "POST":
		form = PublicationForms(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.acteur = request.user
			post.date_publication = timezone.now()
			post.save()
			return redirect('detail', pk=post.pk)
	else:
		form = PublicationForms()

	return render(request, 'myblog/new.html', {'form':form})
@login_required
def edit_pub(request, pk):
	post = get_object_or_404(Publication, pk=pk)
	if request.method == "POST":
		form = PublicationForms(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.acteur = request.user
			post.date_publication = timezone.now()
			post.save()
			return redirect('detail', pk=post.pk)
	else:
		form = PublicationForms(instance=post)

	return render(request, 'myblog/new.html', {'form':form})
def delete_pub(request, pk):
	post = get_object_or_404(Publication, pk=pk)
	if request.method == 'POST':
		post_to_delete = Publication.objects.filter(pk=post.pk)
		post_to_delete.update(
				archive = True
			)
		#post.delete()
		return redirect('home')
	return render(request, 'myblog/delete.html', {'post':post} )

def login_view(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')

	return render(request, 'myblog/login.html', {'form':form})
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			raw_password = form.cleaned_data.get("password1")
			user = authenticate(username=username, password=raw_password)
			return redirect('home')
	else:
		form = SignUpForm()

	return render(request, 'myblog/register.html', {'form':form})

@login_required
def profile_user(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
									request.FILES,
									instance=request.user.profile)
		if u_form.is_valid() and  p_form.is_valid():
			u_form.save()
			p_form.save()
			return redirect('profile_user')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	

	context = {
		'u_form':u_form,
		'p_form':p_form
	}
	#user = User.objects.filter(username='username').first()
	return render(request, 'myblog/profile.html',  context)
	