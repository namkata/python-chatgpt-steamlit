import streamlit as st
import openai
from streamlit_chat import message

with open("apiKey.txt", "r") as f:
    openai.api_key = f.readline()


# Create a function which will generate the calls from the api

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        n=1,
        max_tokens=1024,
        stop=None,
        temperature=0.5,
    )
    msg = completions.choices[0].text
    return msg


st.title("Giải đáp thắc mắc của bạn tại đây?")

# Storing the chat

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ", "Nhập câu hỏi tại đây?", key="input")
    return input_text


user_input = get_text()
if st.button("Trả lời"):
    output = generate_response(user_input)

    # store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')