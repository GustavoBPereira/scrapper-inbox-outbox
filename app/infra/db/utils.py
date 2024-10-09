from app.infra.db import session
from app.infra.db.tables import Inbox, Outbox


def main():
    inbox_result = session.query(Inbox).all()
    print('#############')
    print(f'--- Inbox ---')
    print()
    for i in inbox_result:
        print(i)

    outbox_result = session.query(Outbox).all()
    print('##############')
    print(f'--- Outbox ---')
    print()
    for o in outbox_result:
        print(o)
