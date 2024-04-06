from openai import OpenAI

class Chat():
    def __init__(self, major, interests, major_map):
        self.client = OpenAI(token = "token")
        self.messages = [{"role": "system", "content": f"You are a helper for a college student trying to navigate college. The student is majoring in {major} and is interested in {interests}. Your job is to first look at the major map and list which classes may be most helpful in the student's future career. Then, list some extracirricular activities that the student can participate in to achieve success in their future career. After printing out both of these, you will answer any questions that the student will ask, keeping the student's professional and career success in mind while answering. The major map for the student's major is given here:\n{major_map}"}]
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=self.messages)
        return completion.choices[0].message
        
    def getResponse(self,message):
        self.messages.append(message)
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=self.messages)
        return completion.choices[0].message