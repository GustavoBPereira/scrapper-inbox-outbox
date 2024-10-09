from app.infra.db import session
from app.infra.db.tables import Inbox, Outbox, State


def process_inbox(inbox_id: int):
    inbox = session.query(Inbox).filter(Inbox.id == inbox_id).one()
    inbox_payload = inbox.payload

    try:
        outbox_payload = {
            'films': [film for film in inbox_payload.get("films", [])],
            'name': inbox_payload.get("name", ""),
        }
        outbox_state = State.DONE
    except Exception as error:
        outbox_state = State.FAILED
        outbox_payload = {'reason': error}

    new_outbox_entry = Outbox(payload=outbox_payload, inbox_id=inbox_id, state=outbox_state)
    inbox.state = State.DONE
    session.add(inbox)
    session.add(new_outbox_entry)
    session.commit()
