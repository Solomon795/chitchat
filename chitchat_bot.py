from openai import OpenAI
import yaml


with open('config.yaml') as f:
    config_yaml = yaml.load(f, Loader=yaml.FullLoader)
api_key = config_yaml['token']
client = OpenAI(api_key=api_key)
# roles: system, user, assistant
 #system - sets the behavior of the assistant (tells them what they are)
 #user - provides requests or comments for the assistant to respond to
 #assistant - stores previous assistant responses
messages = [
     {'role': 'user', 'content': 'Name 3 colors. Only write the colors.'}
 ]
model = 'gpt-3.5-turbo'
ans = client.chat.completions.create(
    model='gpt-3.5-turbo-0125',
    max_tokens=1000,
    messages=messages
)

class Chatbot:

    def __init__(self, api_key):
        self.model = OpenAI(api_key=api_key)
        self.conversation_history = []

    def initiate_conversation(self, language, scenario, level):
        self.language = language
        self.scenario = scenario
        self.level = level

        if self.level == 'Beginner':
            level_req = '''use simple and limited vocabulary and sentence structure. Must avoid expressions, 
            slang, or complex grammar. Must avoid highly technical language. Use present tense only.'''

        elif self.level == 'Intermediate':
            level_req = '''use a wider range of vocabulary and sentence structure. You can use some very common
            expressions or slang terms, but avoid highly technical language or nuanced sentences. 
            Use present or past tenses only. Keep your response short.'''

        elif self.level == 'Advanced':
            level_req = '''use a wide range of vocabulary and sentence structure. You can use
            expressions, slang terms, and highly technical language where you find it appropriate in the conversation. 
            The conversation does not need to be complicated if there is no reason to be complicated.
            You can use present, past, or future tenses.'''

        else:
            level_req = '''use simple and limited vocabulary and sentence structure. Must avoid expressions, 
            slang, or complex grammar. Must avoid highly technical language. Use present tense only.'''

        prompt = f'''
        You are simulating a typical conversation while {self.scenario}. Act as only one of the typical roles in this 
        kind of scenario. You are to respond to another person with a different but also typical role in 
        this scenario. The conversation must be conducted in {self.language}. 
        This simulated scenario is designed for {self.language} students to learn how to converse in {self.language} 
        while {self.scenario}.
        You may correct spelling mistakes, but then you need to continue the conversation as if the mistake 
        did not occur. You should assume the student's level in {self.language} is a {self.level} level. Therefore,
        you must {level_req}. Make the conversation sound natural, like a typical conversation in this kind of scenario.
        You are the one starting the conversation.You are the one starting the conversation, but it is very important 
        to remember that you do not create a dialogue of both parties. You only act as your single role. 
        Keep your response short, but keep the conversation going by asking questions.
        '''

        return prompt

    def add_message_to_conversation_history(self, message):
        self.conversation_history.append(message[0])

    def continue_conversation(self, message):
        user_message = [
            {'role': 'user', 'content': message}
        ]
        self.add_message_to_conversation_history(user_message)
        # prompt = '\n'.join(message['content'] for sublist in self.conversation_history for message in sublist)
        ans = self.model.chat.completions.create(model='gpt-3.5-turbo-0125',
                                                 messages=self.conversation_history,
                                                 max_tokens=100)
        response = ans.choices[0].message.content
        gpt_message = [
            {'role': 'system', 'content': response}
        ]
        self.add_message_to_conversation_history(gpt_message)
        return response


#
# bot = Chatbot(api_key)
# initial_prompt = bot.initiate_conversation(language='hebrew', scenario='buying from a grocery store', level='Beginner')
# # ans = client.chat.completions.create(
# res = bot.continue_conversation(initial_prompt)
# print(bot.conversation_history)
# print(res)
# print('\n')

#     model='gpt-3.5-turbo-0125',
#     max_tokens=1000,
#     messages=initial_prompt
# )

# messages = [
# #     {'role': 'user', 'content': 'Name 3 colors. Only write the colors.'}
#     {}
# # ]


# def continue_conversation(self, message):
#     user_message = [
#         {'role': 'user', 'content': message}
#     ]
#     self.add_message_to_conversation_history(message)
#
#     # prompt = '\n'.join(self.conversation_history)
#     ans = self.model.chat.completions.create(model='gpt-3.5-turbo-0125',
#                                              messages=message,
#                                              max_tokens=100)
#     response = ans.choices[0].message.content
#     gpt_message = [
#         {'role': 'gpt', 'content': response}
#     ]
#     self.add_message_to_conversation_history(message)
#     return response

#
# user_message = [
#             {'role': 'user', 'content': 'hi how are you'}
#             {'role': 'gpt', 'content': 'good how are oyu'}
#
#         ]
