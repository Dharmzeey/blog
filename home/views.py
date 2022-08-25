from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

class HomeView(View):
  template_name = "home/index.html"
  def get(self, request):
    posts = Blog.objects.all()
    context = {
      "posts" : posts
    }
    return render(request, self.template_name, context )
home = HomeView.as_view()
  
class CreatePost(LoginRequiredMixin, CreateView):
  model = Blog
  fields = ["title", "body"]
  template_name = "home/new_post.html"
  success_url = reverse_lazy("home")
  
  def form_valid(self, form):
    form.instance.owner = self.request.user
    form.save()
    return super().form_valid(form)
create_post = CreatePost.as_view()

class ReadPost(DetailView):
  model = Blog
  template_name = "home/view_post.html"
read_post = ReadPost.as_view()
  
class UpdatePost(LoginRequiredMixin, UpdateView):
  model = Blog
  success_url = reverse_lazy("home")
  fields = ["title", "body"]
  template_name = "home/new_post.html"
update_post = UpdatePost.as_view()
