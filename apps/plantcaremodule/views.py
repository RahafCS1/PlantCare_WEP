from django.shortcuts import render
from django.template.loader import get_template
def index(request):
    #study the request
    # render the appropriate template for this request
    return render(request, 'plantcaremodule/index.html')  #rendering a template