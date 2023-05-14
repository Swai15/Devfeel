from django import template

register = template.Library()

@register.filter
def is_post_liked(post, user):
    return post.likes.filter(id=user.id).exists()