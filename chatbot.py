import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Sahil Gujral. you can call me xD!",]
    ],
    [
        r"which courses can i apply for ?",
        ["This are the courses in our college:"
         "CSE-DS,AI-DS,IT,Computer,Civil,Extc,Mech",]
],
    [
        r"Is there any contact available?",
        ["This are contacts you can refer:986542356 and 6553213545",]
    ],
    [
        r"What is the address of college?",
        ["KT Nagar. It is near Vasai Road Station.",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
[
        r"Is it a private college or government college?",
        ["It is a Government College.",]
    ],
    [
        r"What is the name of college?",
        ["Vidyavardhini College of Engineering.",]
    ],
    [
        r"How many seats are available for Computer Science (Data Science) Branch?",
        ["There are 60 seats available for Computer Science (Data Science) Branch.",]
    ],
    [
        r"What are more facilities available inside college?",
        ['There is playground,gymkhana,multiple laboratories with computers available,Seminar halls and much more things.',]
    ],

]
def chat():
    print("Hi! I am a chatbot created by Sahil Gujral for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()