import datetime
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from models import Poll
from forms import ContactsForm
from django.template.loader import get_template
from django.template import Template, Context, RequestContext
from django.contrib.auth import logout

def HelloWorld(request):
  return HttpResponse('Hello There, and welcome to the my powerfull Django web app, here are some details i can know about you Browser: %s, Path: %s , IP Address: %s  and IF your site is secured: %s' % (request.META['HTTP_USER_AGENT'], request.path, request.get_host(), request.is_secure()))

def hello(request):
	return HttpResponse('Welcome to the Home Page of my First Django powered Web App')

def current_date(request):
    now = datetime.date.today()
    return render_to_response('current.html', {'date': now}, context_instance=RequestContext(request))

def datetime_offset(request, offset):
	try:
	  offset = int(offset)
	except ValueError:
	  raise Http404
	now = datetime.datetime.today()
	dt = datetime.datetime.today() + datetime.timedelta(hours=offset)
        html = "<html><body>Time now is %s and after %s hour time will be %s</body></html>" %(now, offset, dt)
	return HttpResponse(html)

def index(request):
	latest_poll = Poll.objects.all()
	# output = ', '.join([p.question for p in latest_poll])
	t = get_template('polls.html')
	c = Context	({'latest_poll': latest_poll})
	return HttpResponse(t.render(c))

def details(request, poll_id):
	return HttpResponse('You Are Looking at the details page of poll %s' %poll_id)

def results(request, poll_id):
	# Polls = Poll.objects.all()
	# poll_list = ([p.question for p in Polls])
	poll_id = int(poll_id)
	Polls = get_object_or_404(Poll, pk=poll_id)
	# question_asked = poll_list[poll_id]
	return HttpResponse('You Are Looking at the results page of poll %s and the question was asked in that poll is %s' %(poll_id,Polls))

def votes(request, poll_id):
	return HttpResponse('You Are Looking at the votes page of poll %s' %poll_id)

def logout_view(reauest):
	logout(request)

def user_agent(request):
	try:
	 UserAgent = request.META['HTTP_USER_AGENT']
	except KeyError:
	 UserAgent = 'UNKNOW'
	return HttpResponse(UserAgent)

def ip(request):
	IP = request.META.get('REMOTE_ADDR','UNKNOW')
	return HttpResponse(IP)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	errors = []
	if 'text_field' in request.GET:
	  query = request.GET['text_field']
	  if not query:
	    errors.append('Please type a search term, OR you will be banned')
	  elif len(query) > 20:
	    errors.append('please submit a query less than 20 character in long')
	  else:	
	   poll_search = Poll.objects.filter(question__icontains='query')
	   return render_to_response('search_results.html', {'poll_search': poll_search, 'query': query})
	return render_to_response('search_form.html',{'errors': errors})

def contact(request):
	
	ADDR = request.META['PATH_INFO']
	if request.method == 'POST':#means if the form is submitted
	 form = ContactsForm(request.POST) #will bound the form with data submitted in the request
	 if form.is_valid(): #validation takes place		
		data = form.cleaned_data #accessing the data submitted in the request, this step will return the data after its converted to 							 #python object
		send_mail ( data['subject'],
			    data['message'],
			    data['email'],
			    ['recipient@localhost.com'],
			   )
		return HttpResponseRedirect('/thanks/')
	else:
	 form = ContactsForm()
	return render_to_response('contact_form.html', {'form': form, 'ADDR':ADDR}, context_instance=RequestContext(request))
	



def home(request):
	ADDR = request.META['PATH_INFO']
	return render_to_response('index.html', {'ADDR':ADDR}, context_instance=RequestContext(request))


def resume(request):
	ADDR = request.META['PATH_INFO']
	return render_to_response('resume.html', {'ADDR':ADDR}, context_instance=RequestContext(request))
