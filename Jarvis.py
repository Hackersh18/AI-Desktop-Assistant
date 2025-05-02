from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
print(">> Starting the Jarvis : Wait For Some Seconds")
print(">> Starting the Jarvis : Wait For Few Seconds More")
from Body.Listen import MicExecution
from Body.Speak import Speak
from Main import MainTaskExecution

def MainExecution():

    Speak("Welcome Master Harsh")
    Speak("I'm Jarvis, I'm Ready To assist you Sir.")

    while True: 

        Data =MicExecution()
        Data=str(Data)
        ValueReturn =MainTaskExecution(Data)
        if ValueReturn==True:
            
            pass

        if len(Data)<3:
            pass

        elif "what is" in Data or "where is" in Data or "question" in Data or "Answer" in Data:
            Reply= QuestionsAnswer(Data)

        elif "my name" in Data:
            Reply="Your name is Harsh Dayal"
            Speak(Reply)

        elif " my team members" in Data:
            Reply="Your Team member are awesom and very skilled they are Arnav, Alisha, Ritik, Gaurav, Asad, Siddharth, Sujeet, Amit and Yash"
            Speak(Reply)

        else:
            Reply=ReplyBrain(Data)
            Speak(Reply)

MainExecution()




