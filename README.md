# How to access local host:
```bash
# Clone the repository
git clone https://github.com/username/repo-name.git
cd repo-name

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

# Use the local host link generated to access the site.
