from ..database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    x = []
    try:
        all_news = db.news.find({}, {
            '_id': 0,
            'url': 1,
            'title': 1
        })
        for new in all_news:
            if (title.lower() in new['title'].lower()):
                x.append((new['title'], new['url']))
        return x
    except FileNotFoundError:
        return []


# Requisito 8
def search_by_date(date):
    x = []
    try:
        fd = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
        all_news = db.news.find({"timestamp": fd}, {
            '_id': 0,
            'url': 1,
            'title': 1
        })

        if (all_news == []):
            return []
        for new in all_news:
            x.append((new['title'], new['url']))
        return x
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    x = []
    try:
        all_news = db.news.find({}, {
            '_id': 0,
            'url': 1,
            'title': 1,
            'category': 1
        })
        for new in all_news:
            if (category.lower() in new['category'].lower()):
                x.append((new['title'], new['url']))
        return x
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    x = search_by_title("Algoritmos")
    print(x)