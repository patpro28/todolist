from django import template

register = template.Library()

@register.inclusion_tag('user/link.html', name='link')
def user_link(user):
    print(user)
    return {'user': user.username }