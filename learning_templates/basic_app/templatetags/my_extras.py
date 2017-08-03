from django import template;

register = template.Library()

@register.filter(name="cut") # this is the decorator version of doing the call below
def cut(value, arg):
    """
        this cuts out all values of arg from the string
    """
    return value.replace(arg, "")

# register.filter('cut', cut) # this is the regular version of doing the call above
