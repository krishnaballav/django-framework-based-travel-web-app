from django.shortcuts import render
from .models import Destination
from .models import News
from .models import Review
# Create your views here.


def index(request):
    news = News.objects.all()
    dests = Destination.objects.all()
    reviews= Review.objects.all()
    #news= ['krishna', 1,2]
    my = {'news':news ,'dests': dests , 'reviews':reviews }
    





    

    return render(request, "index.html", context=my)



