from stories import stories
words = {
"noun": '',
"adjective": '',
"verb": '',
"place": ''
}


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def make_story():
    noun = user_input('Please give me a noun: ')
    words["noun"] = noun
    adjective = user_input("Please give me an adjective: ")
    words["adjective"] = adjective
    verb = user_input("Please give me a verb: ")
    words["verb"] = verb
    place = user_input("Please specify a place: ")
    words["place"] = place

def select(option):
    if option == 1:
        print(stories[0])
    elif option == 2:
        print(stories[1])
    elif option == 3:
        print(stories[2])
    else:
        print("not a story in our stories :( ")

def show_story():
    make_story()
    print(stories[0].format(words.get("noun"), words.get('verb'), words.get("place")))


selection = int(user_input("select an story 1 - 3: "))
select(selection)
# show_story()
# def test():
