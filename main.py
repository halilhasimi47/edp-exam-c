class Event:
    def __init__(self, payload):
        self.payload = payload

class ApplicationSubmittedEvent(Event):
    name = "application_submitted"

class ApplicationRejectedEvent(Event):
    name = "application_rejected"

class ApplicationAcceptedEvent(Event):
    name = "application_accepted"

communication_queue = []