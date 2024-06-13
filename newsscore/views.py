from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.templatetags.static import static
import requests
from textblob import TextBlob
from .serializers import ArticleSerializer
from django.contrib.auth import authenticate,login,logout,get_user_model
from newsscore.models import CustomUser
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')


class Analysis:
    def __init__(self, term, api_key):
        self.term = term
        self.api_key = api_key
        self.url = f'https://newsapi.org/v2/everything?q={self.term}&language=en&apiKey={self.api_key}'

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            scraped_data = []

            for article in articles:
                title = article.get('title')
                content = article.get('content')
                image_url = article.get('urlToImage')
                article_url = article.get('url')
                if title and content and image_url:
                    content_blob = TextBlob(content)
                    analysis = content_blob.sentiment
                    sentiment = analysis.polarity
                    sentiment_grade = round((sentiment + 1) * 5, 2)

                    if sentiment_grade >= 0 and sentiment_grade < 2:
                        senti_image = static('0-2.png')
                    elif sentiment_grade >= 2 and sentiment_grade < 4:
                        senti_image = static('2-4.png')
                    elif sentiment_grade >= 4 and sentiment_grade < 6:
                        senti_image = static('4-6.png')
                    elif sentiment_grade >= 6 and sentiment_grade < 8:
                        senti_image = static('6-8.png')
                    elif sentiment_grade >= 8 and sentiment_grade <= 10:
                        senti_image = static('8-10.png')

                    scraped_data.append({
                        'title': title,
                        'content': content,
                        'image_url': image_url,
                        'article_url': article_url,
                        'sentiment': sentiment_grade,
                        'senti_image': senti_image
                    })

            return scraped_data
        else:
            return []

@api_view(['GET'])
@login_required
def get_articles(request):
    topic = request.GET.get('topic')
    user = request.user
    CustomUser = get_user_model()
    api_key = user.apikey
    analysis = Analysis(topic, api_key)
    data = analysis.run()
    serializer = ArticleSerializer(data, many=True)
    return Response(serializer.data)

def home(request):
    return render(request, 'index.html')
# Create your views here.

def news(request):
    return render(request,'main.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return render(request, 'signup.html', {'error': "Passwords don't match"})
        
        apikey=request.POST.get('apikey')
        my_user=CustomUser.objects.create_user(username=uname, email=email, password=pass1,apikey=apikey )
        my_user.save()
        return redirect('login')
    return render(request,'signup.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('news')
        else:
            return render(request, 'login.html', {'error': "Username or Password is incorrect"})
    return render (request,'login.html')


def Logout(request):
    logout(request)
    return redirect('home')
