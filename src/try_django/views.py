from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
# Model View Template (MVT)


def home_page(request):
    my_title = "Hello there...."
    context = {"title": "my title"}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    '''
    # template_name = "title.txt"
    # template_obj = get_template(template_name)
    # rendered_string = template_obj.render(context)
    '''
    # print(rendered_string)
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_render_doc = "<h1>{{title}}</h1>".format(title=my_title)
    '''
    return render(request, "hello_world.html", {"title": rendered_string})
    '''
    return render(request, "home.html", context)
def about_page(request):

    return render(request, "about.html", {"title": "About Us"})

def contact_page(request):
    return render(request, "hello_world.html", {"title": "Contact Us"})

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)

    return HttpResponse(template_obj.render(context))