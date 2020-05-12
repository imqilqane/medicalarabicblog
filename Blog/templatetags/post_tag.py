from django import template
from Blog.models import Post , Comment

register = template.Library()
@register.inclusion_tag('Blog/latests_posts.html')
def latests_posts ():
    context = {
        'l_posts':Post.objects.all()[0:5],
    }
    return context

@register.inclusion_tag('Blog/latest_comments.html')
def latests_comments ():
    context = {
        'l_comments' : Comment.objects.filter(active=True)[0:5],
    }
    return context