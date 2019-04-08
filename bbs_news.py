import requests
import user_date
import datetime

token_bbs = user_date.bbs_token
URL_NEWS = 'http://newsapi.org/v2/top-headlines?sources=bbc-news&' + token_bbs

def get_news():
    url = URL_NEWS
    response = requests.get(url).json()
    top_news = response['articles']
    main_fields = []
    for i in top_news:
        source_name = i['source']['name']
        title_new = i['title']
        description_new = i['description']
        date_time = i['publishedAt']
        dt = datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%SZ")
        content_new = i['content']
        list_data = [source_name, title_new, description_new, dt, content_new]
        main_fields.append(list_data)
    return main_fields
