# Rule based AI python ChatBot

print("==Namaste! Welcome to my personal ChatBot==")
print("You can ask me basic question, type 'bye' to exit from the bot ")

responses = {
    "hello" : "Hello !, Welcome, Hou can i help you !!",
    "hi" : "hi !, Nice to meet you.",
    "how are you" : "I am very fine, thank you😊",
    "what is your name" : "My name is mini AI ChatBot",
    "who are you" : "I am your personal AI chatbot",
    "motivate me" : "Keep going. Every bug of your project making you a better developer!!",
    "happy" : "Great to hear that",
    "what is python" : "Python is a high-level programming language.",
    "who created python" : "Python was created by Guido ven Rossum",
    "what is html" : "HTML are created by the dynamic  structure web page.",
    "what is CSS" : "CSS are used to style the webside page.",
    "what is dictionary" : "A dictionary stores data in key-value pairs in python.",
    "what is list" : "A list is a collection that can store multiple values.",
    "what is loop" : "A loop is used to execute a block of code repeatedly",
    "what is function" : "A function is a reusable block of code.",
    "what is github" : "Github us a platform used to host and manage code repositories.",
    "wour states" : "I am build the ShopEase e-commarse store project by using the HTML, CSS, JavaScript",
    "what is chatbot" : "A chatbot is a program that communicateds with users.",
    "thank you" : "You are welcome",
    "goodbye" : "GoodBye! Have a nice day!",
}

# Method/Function to get response of ChatBot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]       
    return "I am not able to tell that yet. "

# Take user input
while True:
    userInput = input("Please ask your question: ")
    reply = getResponseOfBot(userInput)
    print("Bot Response, ",reply)

    if 'bye' in userInput.lower():
        break 
