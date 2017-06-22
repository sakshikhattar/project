from datetime import datetime


class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


spy = Spy("Sakshi", "Ms.", 20, 4.6)


friend1 = Spy("Raman", "Mr.", 21, 4.9)
friend2 = Spy("Ankit", "Mr.", 23, 5)
friend3 = Spy("Asha", "Ms.", 25, 5.2)

friends = [friend1, friend2, friend3]


class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
