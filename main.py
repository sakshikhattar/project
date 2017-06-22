from spy_details import spy, Spy, friends, ChatMessage
from steganography.steganography import Steganography
from termcolor import colored

#list of older status messages

STATUS_MESSAGES = ["Don\'t tell people your dreams, SHOW THEM!", "Take a deep breath and start again", "Keep Smiling & One day Life will tired of upsetting you" ]

#string for alert generation

SPECIAL_WORDS = ["HELP ME", "SAVE ME", "URGENT", "TROUBLE"]


#method to count number of words in a string

def count_words(word):
    word.split()
    length = len(word.split())
    return length


#method to remove a friend


def remove_friend(friend_position):       #in the function we pass the index of the friend to be removed as a parameter
    print colored("Removing " + friends[friend_position].name + ".", "green", "on_grey")
    del friends[friend_position]
    print colored("Spy removed.", "green", "on_grey")
    print len(friends)


#method to read chat history of a friend


def read_chat_history():
    read_for = select_friend()

    for chats in friends[read_for].chats:
        if chats.sent_by_me:
            #adding different colors to the text
            print ("[%s] %s %s" % (colored(chats.time.strftime("%d %B %Y"), "blue"), colored("Me:", "red"), chats.message))
        else:
            print ("[%s] %s said: %s" % (colored(chats.time.strftime("%d %B %Y"), "blue"), colored(friends[read_for].name, "red"), chats.message))


#method to send message to a friend using steganography

def send_message():
    choose_friend = select_friend()
    print choose_friend
    image_name = raw_input(colored("Enter the name of the image", "green", "on_grey"))  #name of the original image
    output_path = "secret.jpg"                             #name of the output file
    text = raw_input(colored("What do you want to say?", "green", "on_grey"))           #message to be sent

    Steganography.encode(image_name, output_path, text)
    new_chat = ChatMessage(text, True)
    friends[choose_friend].chats.append(new_chat)
    print colored("Your secret message is ready!", "green", "on_grey")

#method selects a friend from the list and the file to decode the message

def read_message():
    sender = select_friend()

    output_path = raw_input(colored("What is the name of the file?", "green", "on_grey"))
    secret_text = Steganography.decode(output_path)
    if secret_text.upper() in SPECIAL_WORDS:
        #prints alert for some special words defined by the user
        print colored("SPY ALERT! SPY ALERT! SPECIAL MESSAGE GENERATED: " + secret_text, 'green', 'on_grey')

    number = count_words(secret_text)  #counts the number of words in the string
    if number > 50:
        remove_friend(sender)          #removes the friend if the friend speaks more than hundred words
    else:
        print secret_text
        new_chat = ChatMessage(secret_text, False)
        friends[sender].chats.append(new_chat)

        print colored("Your secret message has been saved!", "green", "on_grey")

#method to select a friend from the list of friends and returning the index of that friend in the list


def select_friend():
    item_number = 1

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number, friend.name,
                                                             friend.age,
                                                             friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input(colored("Choose from your friends", "green", "on_grey"))

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


#method to add a friend

def add_friend():
    new_friend = Spy(" ", " ", 0, 0.0)

    new_friend.name = raw_input(colored("Please add your friend's name:", "green", "on_grey"))
    new_friend.salutation = raw_input(colored("Are they Mr. or Ms.?: ","green", "on_grey"))

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input(colored("Age?", "green", "on_grey"))
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input(colored("Spy rating?", "green", "on_grey"))
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        #rating of friend should be more or equal to the rating of spy
        friends.append(new_friend) #new friend should be appended in the  list of friends

        print colored("Friend added!", "green", "on_grey")

    else:
        print colored("Sorry! Invalid entry. We can\'t add spy with the details you provided", "red")

    return len(friends)


#method to add status or to choose from old ones

def add_status():
    updated_status_message = None
    if spy.current_status_message != None:
        print "Your current status message is " + spy.current_status_message + "\n"
    else:
        print "You don\'t have any status message currently \n"

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":  #upper() method to conver the character to upper case
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == "Y":
        item_position = 1

        for message in STATUS_MESSAGES:
            print "%d. %s" % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print colored("The option you choose is not valid! Press either y or n.", "red")

    if updated_status_message:
        print colored("Your updated status message is: %s" % updated_status_message, "green", "on_grey")
    else:
        print colored("You did not update your status message", "red")

    return updated_status_message


#initiates the menu display and activities for the passed object spy

def start_chat(spy):

    current_status_message = None

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:
        print colored("Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(
            spy.rating) + " Proud to have you onboard", "green", "on_grey")

        show_menu = True

#show menu will become false when the user selects something that doesnt match any option

        while show_menu:
            menu_choices = ("What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user  \n 6. Remove friend \n 7. Close Application")
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
                if(menu_choice == 1):
                    spy.current_status_message = add_status()
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
        print colored("Sorry you are not of the correct age to be a spy", "red")


#the program starts from here

print colored("Welcome to Spychat", "green", "on_grey")

question = colored("Continue as " + spy.salutation + " " + spy.name + "(Y/N)? ", "green", "on_grey")
existing = raw_input(question)

#if the user wants to continue with the same old name set by default

if existing == "Y":
    start_chat(spy)

#if user wants to create a new entry

else:

    spy = Spy(" ", " ", 0, 0.0)
#getting various inputs from user as per the class spy

    spy.name = raw_input(colored("what is your name?", "green", "on_grey"))
    if len(spy.name) > 0:
        print "welcome " + spy.name + ". glad to have you back"
        spy.salutation = raw_input(colored("what do you want to be?", "green", "on_grey"))
        spy.name = spy.salutation + " " + spy.name
        print "Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed."

        spy.age = raw_input(colored("what is your age?", "green", "on_grey"))
        print type(spy.age)
        spy.age = int(spy.age)
        print type(spy.age)
        if  spy.age > 12 and spy.age < 50:

            spy.rating = raw_input(colored("What is your spy rating?", "green", "on_grey"))
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
            print colored("Sorry you are not of the correct age to be a spy.", "red")
    else:
        print colored("A spy needs to have a valid name. Try again please.", "red")


