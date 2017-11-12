import datetime


class MessageUser:
    user_detail = []
    messages = []
    base_message = """Hi {name}! 
    Thank you for the purchase on {date}. 
    We hope you are exicted about using it. Just as a
    reminder the purcase total was ${total}.
    Have a great one!
    Team CFE
    """

    def add_user_detail(self, name, amount, email=None):
        detail = {
            "name": name[0].upper() + name[1:].lower(),
            "amount": "%2.f" % amount,
            "date": '{today.month}/{today.day}/{today.year}'.format(
                today=datetime.date.today())
        }
        if email is not None:
            detail["email"] = email
        self.user_detail.append(detail)

    def get_user_detail(self):
        return self.user_detail

    def make_message(self):
        if len(self.user_detail) > 0:
            for detail in self.get_user_detail():
                message = self.base_message
                new_message = message.format(
                    name=detail["name"],
                    total=detail["amount"],
                    date=detail["date"], )
                self.messages.append(new_message)

    def print_messages(self):
        for message in self.messages:
            print message


obj = MessageUser()
obj.add_user_detail("JOHN", 12, "john@30dayspython.edu")
obj.add_user_detail("Doe", 340, "doe@30dayspython.edu")
obj.make_message()
print obj.print_messages()
