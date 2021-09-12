import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.http import request

from .models import Search


BASE_CRAIGSLIST_URL = "https://ahmedabad.craigslist.org/d/services/search/?query={}"
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def home(request):
    return render(request, template_name='base.html')


def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_listings = []
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        post_price = post.find(
            class_='result-price').text if post.find(class_='result-price') else 'N/A'
        post_date = post.find(class_='result-date').text
        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(':')[1].split(',')[0]
            post_image = BASE_IMAGE_URL.format(post_image_id)
        else:
            post_image = 'https://camerax.com/wp-content/uploads/2018/10/no_image.jpg'
        final_listings.append(
            (post_title, post_url, post_price, post_image, post_date)
        )

    stuff_for_frontend = {
        'search': search,
        'final_listings': final_listings,
    }

    return render(request, 'my_app/new_search.html', stuff_for_frontend)
