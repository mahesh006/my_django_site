from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(publised_date__lte=timezone.now()).order_by('publised_date')
	stuff_for_frontend = {'posts' :posts}
	return render (request, 'blog/post_list.html', stuff_for_frontend)
