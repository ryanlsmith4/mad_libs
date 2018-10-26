from stories import stories
from stories import stories_mad
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#storing the madlib variables in the dict
words = {
"verb": '',
"place": '',
"name": '',
"pronoun": '',
"option": ''
}
#end dict

# method to take input
def user_input(prompt):
    user_input = input(prompt)
    return user_input
#end user input

#Method taking the noun, adj, verb, and place
def make_story():
    name = user_input('Please give me a name: ')
    words["name"] = name
    pronoun = user_input('Please give me a pronoun:  ')
    words["pronoun"] = pronoun
    verb = user_input("Please give me a verb: ")
    words["verb"] = verb
    place = user_input("Please specify a place: ")
    words["place"] = place
    return(words)
#end make_story

#method for user selection to print story before they madlib it
def select(option):
    if option == 1:
        print(stories[0])
    elif option == 2:
        print(stories[1])
    elif option == 3:
        print(stories[2])
    elif option == 4:
        print(stories[3])
    else:
        print("not a story in our stories :( ")
#end select

#method to actually show the story
def show_story():
    make_story()

    print(stories_mad[int(words.get("option")) -1].format(words.get("name"), words.get("verb"), words.get("place"), words.get("pronoun")))


game = True
while game:
    try:
        selection = int(user_input("select an story 1 - 4: "))
        select(selection)
        result = user_input("Did you want to madPrince that one? y/n: ").upper()
        if result == 'Y':
            words["option"] = selection
            clear()
            show_story()
            play_again = user_input("Wanna play again? y/n: ").upper()
            if play_again == 'Y':
                pass
            else:
                game = False
    except:
        print("Use an Integer")
