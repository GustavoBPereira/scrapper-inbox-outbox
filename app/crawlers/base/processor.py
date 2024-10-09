from app.infra.db import session
from app.infra.db.tables import Inbox, Outbox, State
import importlib

def process_inbox(inbox_id: int, processor_handler: str):
    inbox = session.query(Inbox).filter(Inbox.id == inbox_id).one()

    handler = importlib.import_module(processor_handler)
    outbox_state, outbox_payload = handler.handle(inbox.payload)

    new_outbox_entry = Outbox(inbox_id=inbox_id, state=outbox_state, payload=outbox_payload)
    inbox.state = State.DONE
    session.add(inbox)
    session.add(new_outbox_entry)
    session.commit()
