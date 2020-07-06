from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .apps import WebappConfig
from .forms import NameForm

def index(request):
    if request.method == "POST":
        review = request.POST.get("your_review")
        vec = WebappConfig.vectorizer.transform([review])
        film_class = WebappConfig.logreg.predict(vec)
        rating = float(WebappConfig.linreg.predict(vec))
        if rating > 8:
            rating = 10
        elif rating < 1:
            rating = 1
        elif rating < 4.5:
            rating = round(rating)
        else:
            rating = round(rating+2)
        if film_class == 1:
            film_type = 'positive'
        else:
            film_type = 'negative'

        return HttpResponse("<h2>Type of review: {0}. Rating: {1}</h2>".format(film_type, rating))
    else:
        userform = NameForm()
        return render(request, "index.html", {"form": userform})

