from spy_details import spy, Spy, friends, ChatMessage
from steganography.steganography import Steganography
from termcolor import colored

STATUS_MESSAGES = ["Available", "busy"]

print "hello"
print "what\'s up?"
input_string = "my name is sakshi"

question = "Continue as " + spy.salutation + " " + spy.name + "(Y/N)? "
existing = raw_input(question)


def count_words(word):
    word.split()
    length = len(word.split())
    return length


def remove_friend(friend_position):
    print "Removing " + friends[friend_position].name + "."
    del friends[friend_position]
    print "Spy removed."
    print len(friends)


def read_chat_history():
    read_for = select_friend()

    for chats in friends[read_for].chats:
        if chats.sent_by_me:
            print ("[%s] %s %s" % (colored(chats.time.strftime("%d %B %Y"), "blue"), colored("Me:", "red"), chats.message))
        else:
            print ("[%s] %s said: %s" % (colored(chats.time.strftime("%d %B %Y"), "blue"), colored(friends[read_for].name, "red"), chats.message))


def send_message():
    choose_friend = select_friend()
    print choose_friend
    original_image = raw_input("What is the name of the image?")
    output_path = "secret.jpg"
    text = raw_input("What do you want to say?")

    Steganography.encode(original_image, output_path, text)
    new_chat = ChatMessage(text, True)
    friends[choose_friend].chats.append(new_chat)
    print "Your secret message is ready!"


def read_message():
    sender = select_friend()

    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    number = count_words(secret_text)
    if (number) > 10:
        remove_friend(sender)
    else:
        print secret_text
        new_chat = ChatMessage(secret_text, False)
        friends[sender].chats.append(new_chat)

        print "Your secret message has been saved!"


def select_friend():
    item_number = 1

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number, friend.name,
                                                             friend.age,
                                                             friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def add_friend():
    new_friend = Spy(" "," ", 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name:")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)

        print "Friend added!"

    else:
        print "Sorry! Invalid entry. We can\'t add spy with the details you provided"

    return len(friends)


def add_status(current_status_message):
    updated_status_message = None
    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print "You don\'t have any status message currently \n"

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == "Y":
        item_position = 1

        for message in STATUS_MESSAGES:
            print "%d. %s" % (item_position , message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print "The option you choose is not valid! Press either y or n."

    if updated_status_message:
        print "Your updated status message is: %s" % updated_status_message
    else:
        print "You did not update your status message"

    return updated_status_message


def start_chat(spy):

    current_status_message = None

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(
            spy.rating) + " Proud to have you onboard"

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user  \n 6. Remove friend \n 7. Close Application"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
                if(menu_choice == 1):
                    current_status_message = add_status(current_status_message)
                elif(menu_choice == 2):
                    number_of_friends = add_friend()
                    print "You have %d friends" % (number_of_friends)
                elif(menu_choice == 3):
                    send_message()
                elif(menu_choice == 4):
                    read_message()
                elif(menu_choice == 5):
                    read_chat_history()
                elif(menu_choice == 6):
                    delete_friend = select_friend()
                    remove_friend(delete_friend)

                else:
                    show_menu = False

    else:
        print "Sorry you are not of the correct age to be a spy"

if existing == "Y":
    start_chat(spy)
else:
   spy = Spy(" ", " ", 0, 0.0)

   spy.name = raw_input("what is your name?")
   if len(spy.name) > 0:
        print "welcome " + spy.name + ". glad to have you back"
        spy.salutation = raw_input("what do you want to be?")
        spy.name = spy.salutation + " " + spy.name
        print "Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed."

        spy.age = raw_input("what is your age?")
        print type(spy.age)
        spy.age = int(spy.age)
        print type(spy.age)
        if  spy.age > 12 and spy.age < 50:
            spy.rating = raw_input("What is your spy rating?")
            spy.rating = float(spy.rating)
            if spy.rating > 4.5:
                print "Great ace!"
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print "You are one of the good ones."
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print "You can always do better."
            else:
                print "We can use somebody to help in the office."

            spy.is_online = True
            print "Authentication complete. Welcome %s age: %d and rating of: %.2f . Proud to have you onboard." % (spy.name, spy.age, spy.rating)
            start_chat(spy)
        else:
            print "Sorry you are not of the correct age to be a spy."
   else:
        print "A spy needs to have a valid name. Try again please."


