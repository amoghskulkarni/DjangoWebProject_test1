"""
Definition of views.
"""

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from app.models import Document
from app.forms import DocumentForm

from app.forms import BootstrapAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Ayan: Added import analytics
from analytics import testAnalytics

def home(request):
    """Renders the home page."""
    #Test Comment 
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def mypage(request):
    """Renders the mypage page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/mypage.html',
        context_instance = RequestContext(request,
        {
            'title':'My Page',
            'year':datetime.now().year,
        })
    )


def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('app.views.upload'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'app/upload.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

#@csrf_exempt
def testPost(request):
    print "This is to test : "
    dataFromClient = dict(request.POST)['data'][0]
    print testAnalytics(dataFromClient)
    return HttpResponse("Success!")
    
def register(request):
    if request.method == 'POST':
	form = BootstrapAuthenticationForm(request.POST)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('register_success')

    args={}
    
    args['form'] = BootstrapAuthenticationForm()
    print args
    return render_to_response('app/register.html', args)
	
def register_success(request):
    return render_to_request('app/register_success.html')
