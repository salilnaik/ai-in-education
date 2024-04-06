from openai import OpenAI
import json

class Chat():
    def __init__(self, major, interests, major_map):
        out = ""
        f = open("shortclubs.json")
        j = json.load(f)
        for element in j:
            out += element["name"] + "\n"
        self.client = OpenAI(api_key="token")
        self.messages = [{"role": "system", "content": f"You are a helper for a college student trying to navigate college. Your responses must be detailed and precise. The responses must also explain the reasons behind the decisions the model is making. The student is majoring in {major} and is interested in {interests}. Your job is to first look at the major map and list which classes may be most helpful in the student's future career. Then, list some extracirricular activities that the student can participate in to achieve success in their future career. After printing out both of these, you will answer any questions that the student will ask, keeping the student's professional and career success in mind while answering. The major map for the student's major is given here:\n{major_map}\n\nThe list of extracurricualr activities is here: \n{out}"}]
        self.completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=self.messages)
    
    def getInit(self):
        return self.completion.choices[0].message.content
        
    def getResponse(self,message):
        self.messages.append({"role": "user", "content": message})
        self.completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=self.messages)
        self.messages.append({"role": "assistant", "content": self.completion.choices[0].message})
        return self.completion.choices[0].message.content
    
# c = Chat("t", "d", "d")
# print(c.getInit())
# print(c.getResponse("tst"))