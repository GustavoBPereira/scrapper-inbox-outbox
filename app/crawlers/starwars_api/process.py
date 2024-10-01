from app.infra.db import session
from app.infra.db.tables import Inbox, Outbox


def process_inbox(inbox_id: int):
    inbox = session.query(Inbox).filter(Inbox.id == inbox_id).one()
    inbox_payload = inbox.payload

    outbox_payload = {
        'films': [film for film in inbox_payload.get("films", [])],
        'name': inbox_payload.get("name", ""),
    }
    new_outbox_entry = Outbox(payload=outbox_payload, inbox_id=inbox_id)
    session.add(new_outbox_entry)
    session.commit()
    print(new_outbox_entry.id)
