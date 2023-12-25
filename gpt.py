# external libraries
from openai import OpenAI

# local functions
from keys.getenv import get_key

# Open AI API Key
client = OpenAI(api_key=get_key('ENV_OPENAI_API_KEY'))
# Choose GPT model
model = "gpt-3.5-turbo-1106"

system_prompt = {'role': 'system', 'content': """
You summarize a chatlog in english.

Empty Messages and content of media is information you do not know and can only speculate from context.
Do not talk about empty messages in summary.
Do not print UserID, ChatID or MessageID in summary.
Instead print *User Name* and *Chat Name*.

Sort summarized text by Chat Name.

Split topics by Ordered List in markdown for readability.
Sort topics by time like Morning, Day, Evening, Night etc.

You add links to important messages that define or start a topic like shown in the example.                                                                      
Example: 
In the morning User Name was talking about cars [1](t.me/c/ChatID/MessageID/) when User Name mentioned airplanes [2](t.me/c/ChatID/MessageID/), then the conversation continued with airplanes for a while.

to create a link combine t.me/c/ChatID/MessageID/
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
