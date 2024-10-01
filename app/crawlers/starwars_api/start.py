import argparse

from app.crawlers.base.client import HttpClient
from app.crawlers.starwars_api.get import crawl
from app.crawlers.starwars_api.process import process_inbox
from app.infra.db import session
from app.infra.db.tables import Inbox, State

parser = argparse.ArgumentParser()
parser.add_argument('--start', help='page to start the crawler', type=int, default=1)
parser.add_argument('--stop', help='page to stop the crawler', type=int)
args = parser.parse_args()



def main():
    client = HttpClient(base_url='https://swapi.dev/api')
    for page in range(args.start, args.stop + 1):
        try:
            raw_response = crawl(client, page)
            inbox_state = State.PROCESSING
        except Exception as Error:
            inbox_state = State.FAILED
            raw_response = {'reason': Error}

        new_inbox_entry = Inbox(payload=raw_response, state=inbox_state)
        session.add(new_inbox_entry)
        session.commit()
        process_inbox(new_inbox_entry.id)
