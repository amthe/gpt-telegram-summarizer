# external libraries
from openai import OpenAI

# local functions
import getenv

# Open AI API Key
client = OpenAI(api_key=getenv.get_key('ENV_OPENAI_API_KEY'))
# Choose GPT model
model = "gpt-4-1106-preview"


# Summary function that accept any message string for summarizing
def summary(msg):

    # System prompt for GPT, that explains what to do
    system_prompt = {'role': 'system', 'content': """
    You summarize a chatlog in english.
    Empty Messages is information you do not know and can only speculate.
    Do not print UserID, ChatID or MessageID.
    Always print User Name and Chat Name, if Chat name is None call it Direct message.
    Sort summarized text by Chat Name.

    Example of a message in a chat log: In Chat [None - ChatID:145893019] User [Red Panda - UserID:145893019] send [text message: "i had a great dinner with my wife tonight"] - [MessageID:19591]
    """}

    # User prompt for GPT that provides content
    user_prompt = {'role': 'user', 'content': msg}

    chat_completion = client.chat.completions.create(
        model=model,
        messages=[system_prompt, user_prompt],
    )
    answer = chat_completion.choices[0].message.content.strip()
    return answer
