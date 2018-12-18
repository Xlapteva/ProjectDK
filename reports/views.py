from django.shortcuts import render

# Create your views here.
def hello_world(request):
    name = 'Xlapteva'
    return render(
        template_name='reports/hello_world.html',
        context={'name': name},
        request=request
    )
