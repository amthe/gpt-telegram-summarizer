# external libraries
from openai import OpenAI

# local functions
from keys.getenv import get_key

# Open AI API Key
client = OpenAI(api_key=get_key('ENV_OPENAI_API_KEY'))
# Choose GPT model
model = "gpt-4-1106-preview"

system_prompt = {'role': 'system', 'content': """
You summarize a chatlog in english.
Empty Messages is information you do not know and can only speculate.
Do not print UserID, ChatID or MessageID in summary.
Always print User Name and Chat Name. 
If Chat name is None call it Direct message. 
Put names into square brackets like this [User Name]
Split topics by empty line for readability.
Beginning of each topic start with -

You add links to important messages that define or start a topic like shown in the example.
                                                                       
Example: 
[User Name] was talking about cars <a href="t.me/c/2101673397/41/">[1]</a> when [User Name] mentioned airplanes <a href="t.me/c/2101673397/49/">[2]</a>, then the conversation continued with airplanes for a while.

to create a link combine t.me/c/ChatID/MessageID/ 

Sort summarized text by Chat Name.
Use timestamp to provide remarks about when conversation happened.

Example of a message in a chat log: In Chat [None - ChatID:145893019] User [Red Panda - UserID:145893019] send [text message: "i had a great dinner with my wife tonight"] - [MessageID:19591]
"""}

# Summary function that accept any message string for summarizing
def summary(msg):

    # User prompt for GPT that provides content
    user_prompt = {'role': 'user', 'content': msg}

    chat_completion = client.chat.completions.create(
        model=model,
        messages=[system_prompt, user_prompt],
    )
    answer = chat_completion.choices[0].message.content.strip()
    return answer
