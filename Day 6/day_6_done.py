import datetime

default_names = ["justin", "john", "Emilee", "Jim", "Ron", "sandra",
                 "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 

Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!

Team CFE
"""


def make_message(names, amount):
    all_message = []
    date = '{today.month}/{today.day}/{today.year}'.format(
        today=datetime.date.today())
    if len(names) == len(amount):
        i = 0
        for name in names:
            all_message.append(
                unf_message.format(
                    name=name[0].upper() + name[1:].lower(),
                    date=date,
                    total="%.2f" % amount[i],

                )
            )
            i += 1
        return all_message


def print_message(messages):
    for message in messages:
        print message


print print_message(make_message(default_names, default_amounts))
