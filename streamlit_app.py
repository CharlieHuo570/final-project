import streamlit as st
from st_chat_message import message
from openai import OpenAI
import json

client = OpenAI(
    api_key = st.secrets["api_key"]
)

def get_standard_response(system_prompt, user_prompt):
    """
    Sends a prompt to the ChatGPT API where it will return a standard response.
    ChatGPT will not remember any prior conversations.

    Parameters:
    - system_prompt (str): Directions on how ChatGPT should act.
    - user_prompt (str): A prompt from the user.

    Returns:
    - (str): ChatGPT's response.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

def get_json_response(system_prompt, user_prompt):
    """
    Sends a prompt to the ChatGPT API where it will return a JSON response.
    ChatGPT will not remember any prior conversations.

    Parameters:
    - system_prompt (str): Directions on how ChatGPT should act. Remember that it must request for a JSON response and include a JSON template.
    - user_prompt (str): A prompt from the user.
    
    Returns:
    - (dict): A dictionary containing ChatGPT's response in the requested JSON format.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return json.loads(response.choices[0].message.content)

def talk_to_chatgpt(system_prompt):
    """
    Allows the user to have a conversation with the ChatGPT API.
    ChatGPT will remember what the user says to it as long as this conversation is active.
    When the function terminates, ChatGPT will forget everything the user said.
    The user can end this conversation by typing and entering "STOP".

    Parameters:
    - system_prompt (str): Directions on how ChatGPT should act.

    Returns:
    - (list(dict)): The chat history.
    """

    chat_history = [
        {"role": "system", "content": system_prompt},
    ]

    while True:
        user_prompt = input("Enter a response, or type in \"STOP\" to end this conversation. ")
        if user_prompt == "STOP":
            return chat_history
        
        chat_history.append(
            {"role": "user", "content": user_prompt},
        )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages = chat_history
        )

        assistant_response = response.choices[0].message.content
        print(assistant_response)
        print()

        chat_history.append(
            {"role": "assistant", "content": assistant_response}
        )

"""
# Would you rather game?

Put in a theme, press submit then choose one of the options.

Play with friends for more fun!
"""
with st.form ("Theme for the game"):
    Themes = st.selectbox( 
        "What theme do you want to choose?", 
        [ 
            "Superpowers",
            "Life and Death",
            "food",
            "silly",
            "sports",
            "Time travel",
            "DARK",
            "Age Based"])

    submit = st.form_submit_button("SUBMIT")
    if submit:
        u = "Give us a would you rather question with the theme " + Themes
        s = "You are an fun would you rather bot that gives players would you rather questions with a theme, make the questions more detailed and understandable"
        st.write(get_standard_response(s,u))









