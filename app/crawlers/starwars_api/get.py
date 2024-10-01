from app.crawlers.base.client import HttpClient


def crawl(client: HttpClient, page: int):
    return client.get(f'people/{page}')