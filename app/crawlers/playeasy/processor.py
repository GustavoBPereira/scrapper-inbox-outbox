from typing import Dict, Tuple

from app.infra.db.tables import State


def handle(payload: Dict) -> Tuple[State, Dict]:
    print('playeasy')
    try:
        outbox_payload = {
            'films': [film for film in payload.get("films", [])],
            'name': payload.get("name", ""),
        }
        outbox_state = State.DONE
    except Exception as error:
        outbox_state = State.FAILED
        outbox_payload = {'reason': error}

    return outbox_state, outbox_payload
