from django.shortcuts import render_to_response
from django.template import RequestContext
from gensim.summarization import summarize

def home(request):
	text = request.GET.get('text', '').strip()
	summary = summarize(text)
	return render_to_response('home.html', {'text': text, 'summary': summary}, context_instance=RequestContext(request))
