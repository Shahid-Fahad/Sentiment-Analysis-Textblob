from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from textblob import TextBlob

# Create your views here.
def f2(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        return redirect('analyze', anatext=text)
    else:
        return render(request, 'home.html')

def res(request,anatext):
        blob = TextBlob(anatext)
        sentiment_tensor = blob.sentiment.polarity
        #labelling sentiment_tensor for meaningfull outcomes
        if sentiment_tensor>0:
            sentiment="Positive 😁"
        elif sentiment_tensor<0:
            sentiment="Negative 😟"
        else:
            sentiment="Neutral 🙂"
        # Render the results in a template
        return render(request, 'results.html', {'sentiment': sentiment})


