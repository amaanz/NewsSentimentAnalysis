# How to access local host:
```bash
# Clone the repository
git clone https://github.com/amaanz/NewsSentimentAnalysis.git
cd NewsSentimentAnalysis

# Set up django
pip install django
pip install djangorestframework

#Navigate to the directory containing news_sentiment, newsscore,manage.py,etc.

# Set up the database
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```
Use the local host link generated to access the site.

# How to check out the news?

You are advised to go through the whole sign up login process and also sign up at newsapi.org to generate your api key.
Enter that during the site sign up proccess, once you have don that, you are all set to use the NEWS SCORE site.
