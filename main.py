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

class Applicant:
    def __init__(self, name, age, country, email):
        self.name = name
        self.age = age
        self.country = country
        self.email = email

        def apply(self, job_title):
        event = ApplicationSubmittedEvent({"name": self.name, "job": job_title})
        communication_queue.append(event) 
        print(f"{self.name}, {job_title}, applied for this job. (Event: {event.name})")