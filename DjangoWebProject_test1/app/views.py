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

from app.analytics import testAnalytics
from PIL import Image
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from datetime import timedelta
import random
import django
import base64

#Ayan: Added import analytics
#from analytics import testAnalytics
#Ayan: Added image import
#from PIL import Image

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

def uploadFile(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('app.views.uploadFile'))
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

def applyAnalysis(request):
    #fig=Figure()
    #ax=fig.add_subplot(111)
    #x=[]
    #y=[]
    #now=datetime.now()
    #delta=timedelta(days=1)
    #for i in range(10):
    #    x.append(now)
    #    now+=delta
    #    y.append(random.randint(0, 1000))
    #ax.plot_date(x, y, '-')
    #ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    #fig.autofmt_xdate()
    #canvas=FigureCanvas(fig)
    #response=django.http.HttpResponse(content_type='image/png')
    #canvas.print_png(response)
    #return response

    print "This is to test : "
    dataFromClient = dict(request.POST)['data'][0]
    print testAnalytics(dataFromClient)
    # return HttpResponse("Success!")
    img = Image.open('../DjangoWebProject_test1/media/documents/2015/04/22/test_result_a.png')
    with open("../DjangoWebProject_test1/media/documents/2015/04/22/test_result_a.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    #image_data = img.partition('base64,')[2]
    #binary = base64.b64decode(image_data)
    return HttpResponse(encoded_string)


    #return render(
    #    request,
    #    'app/upload.html',
    #    context = RequestContext(
    #        request,
    #        { 'img' : img }
    #        ),
    #    content_type = 'image/png')


def testPost(request):
    print "This is to test : "
    dataFromClient = dict(request.POST)['data'][0]
    print testAnalytics(dataFromClient)
    return HttpResponse("Success!")

def suggestions(request):   
    print "This is to test"
    dataFromClient = dict(request.POST)['data'][0]
    print testAnalytics(dataFromClient)
    return HttpResponse("Success!")

def register(request):
    if request.method == 'POST':
        form = BootstrapAuthenticationForm(request.POST)
    	if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username = username, password = password)
            user.save()
            form.save()
            return HttpResponseRedirect('register_success')
        else:
            form = BootstrapAuthenticationForm()
    args = {}    
    args['form'] = BootstrapAuthenticationForm()
    print args

    return render_to_response('app/register.html', args, context_instance = RequestContext(request))


def register_success(request):
    return render_to_request('app/register_success.html')

#@csrf_exempt    
def login(request):
    if request.method == 'POST':
        form = BootstrapAuthenticationForm(request.POST)
    	if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username = username, password = password)
            if user.check_password(password):
                return HttpResponse('logged in')
            else:
                return HttpResponse('could not log in')
        else:
            form = BootstrapAuthenticationForm()
            return HttpResponse('invalid form')
    else:
        args = {}    
        args['form'] = BootstrapAuthenticationForm()
        print args

        return render_to_response('app/register.html', args, context_instance = RequestContext(request))




def logout(request):
    return HttpResponse("dummy response")
