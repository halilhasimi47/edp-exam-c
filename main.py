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

class Company:
    def __init__(self, name):
        self.name = name

    def process_event(self, event):
        if isinstance(event, ApplicationSubmittedEvent):
            self.submitted(event)
        elif isinstance(event, ApplicationAcceptedEvent):
            self.accepted(event)
        elif isinstance(event, ApplicationRejectedEvent):
            self.rejected(event)

    def submitted(self, event):
        print(f"Company {self.name} received an application from {event.payload['name']} for the job {event.payload['job']}.")
        if event.payload['name'] == "Ahmet Muro":
            self.accepted(event)
        else:
            self.rejected(event)

    def accepted(self, event):
        print(f"Application from {event.payload['name']} has been accepted for the {event.payload['job']} position.")

    def rejected(self, event):
        print(f"Application from {event.payload['name']} has been rejected for the {event.payload['job']} position.")

if __name__ == "__main__":
    applicant1 = Applicant("ahmet muro", 53, "USA", "ahmetmuro@gmail.com")
    applicant2 = Applicant("Will Smith", 25, "PL", "Willsmith@gmail.com")
    applicant3 = Applicant("Ruhi Cenet", 24, "DE", "RuhiCenet@gmail.com")

    company = Company("halil company")

    applicant1.apply("sociology")
    applicant2.apply("actor")
    applicant3.apply("farmer")

    for event in communication_queue:
        company.process_event(event)