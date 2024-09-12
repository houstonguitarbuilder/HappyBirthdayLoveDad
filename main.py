import os
from PIL import Image
import streamlit as st
from gtts import gTTS
from io import BytesIO
from datetime import datetime
import threading
import pyautogui
import time
from text_to_speech import *

# Custom CSS for birthday theme
st.markdown("""
    <style>
    /* Set background color (light pastel pink) */
    .stApp {
        background-color: #ffe4e1;  /* Pastel pink background */
        background-image: url('https://example.com/cake_and_candy_background.jpg');
        background-size: cover;
        background-position: center;
    }

    /* Set the title and headings to purple */
    h1, h2, h3, h4, h5, h6 {
        color: #da70d6;  /* Orchid purple text */
        font-family: 'Comic Sans MS', cursive, sans-serif;  /* Fun birthday-style font */
    }

    /* Set normal text to a lighter purple */
    p {
        color: #ba55d3;  /* Medium orchid text */
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }

    /* Input boxes with pastel pink background and neon pink border */
    div[data-testid="stTextInputRootElement"] input {
        background-color: #ffb6c1;  /* Light pastel pink */
        color: #4b0082;  /* Indigo text */
        border: 2px solid #ff00ff;  /* Neon pink border */
        border-radius: 10px;
        padding: 10px;
    }

    /* Button customization for pastel theme */
    button {
        background-color: #ff69b4;  /* Hot pink button */
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
    }

    /* Make the buttons larger and more playful */
    .stButton>button {
        background-color: #ff69b4;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 12px;
        margin: 5px;
    }

    /* Center the text and inputs */
    .stTextInput, .stButton {
        margin: 0 auto;
        text-align: center;
    }

    </style>
    """,
            unsafe_allow_html=True)

# Title for the app
st.title("The Happy-12th-Birthday-Jemma-BeanBean-WE-LOVE-YOU-Mad-Lib!")

# Initialize session state to track question progress
if 'step' not in st.session_state:
    st.session_state.step = 0

if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Updated Questions list
questions = [
    "Enter a name",
    "Enter a name for a friend",
    "Enter an adjective describing the friend",
    "Enter another adjective describing the friend",
    "Enter a verb related to an activity",
    "Enter another verb related to an activity",
    "Enter a fun activity",
    "Enter another fun activity",
    "Enter one more fun activity",
    "Enter an exciting adventure",
    "Enter another exciting adventure",
    "Enter a third exciting adventure",
    "Enter a favorite location",
    "Enter another favorite location",
    "Enter a third favorite location",
    "Enter an interesting object",
    "Enter a funny sound",
    "Enter a name for a snack",
    "Enter a humorous event",
    # Additional Questions
    "Enter another person's name",
    "Enter another name for the new person's friend",
    "Enter another adjective describing the second friend",
    "Enter yet another adjective describing the second friend",
    "Enter a verb related to an activity",
    "Enter another verb related to an activity",
    "Enter a fun activity",
    "Enter a nasty activity",
    "Enter an embarrassing activity",
    "Enter an exciting adventure",
    "Enter another exciting adventure.  Sorry, only one more after this.",
    "Enter a final exciting adventure. LAST ONE!",
    "Enter a nasty location",
    "Enter a dirty location",
    "Enter a gross location",
    "Enter another interesting object",
    "Enter another funny sound",
    "Enter another name for a snack",
    "Enter another humorous event"
]


# Function to handle input submission
def handle_input():
    answer = st.session_state.get('text_input')
    if answer:  # Ensure the user doesn't submit empty answers
        st.session_state.responses[st.session_state.step] = answer
        st.session_state.step += 1
        st.session_state.text_input = ""  # Clear the input after submission


# Function to save text to speech as an MP3 file
def save_audio(text):
    tts = gTTS(text=text, lang='en')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    downloads_folder = os.path.expanduser('~/Downloads')
    file_path = os.path.join(downloads_folder, f"story_{timestamp}.mp3")
    tts.save(file_path)
    return file_path


# Function to play text-to-speech in a separate thread
def speak_text(text):
    tts = gTTS(text=text, lang='en')
    with BytesIO() as fp:
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_data = fp.read()
        st.audio(BytesIO(audio_data), format='audio/mp3')


# Display current question and input box
if st.session_state.step < len(questions):
    current_question = questions[st.session_state.step]
    # st.write(current_question)
    tts(current_question)

    # Text input without autofocus
    st.text_input(current_question, key='text_input', on_change=handle_input)

    # Janky handling of text input focus.
    time.sleep(.1)
    pyautogui.press('tab')

    if st.button("Next"):
        handle_input()
else:
    # Button to generate the story after all questions are answered
    if st.button("Generate Story"):
        # Collecting all responses
        responses = st.session_state.responses

        # Extracting variables from responses
        name1 = responses[0]
        friend_name1 = responses[1]
        friend_adj1 = responses[2]
        friend_adj2 = responses[3]
        activity1_verb = responses[4]
        activity2_verb = responses[5]
        fun_act1 = responses[6]
        fun_act2 = responses[7]
        fun_act3 = responses[8]
        adventure1 = responses[9]
        adventure2 = responses[10]
        adventure3 = responses[11]
        location1 = responses[12]
        location2 = responses[13]
        location3 = responses[14]
        interesting_object = responses[15]
        funny_sound = responses[16]
        snack_name = responses[17]
        humorous_event = responses[18]

        # Additional variables
        name2 = responses[19]
        friend_name2 = responses[20]
        friend_adj1_2 = responses[21]
        friend_adj2_2 = responses[22]
        activity1_verb2 = responses[23]
        activity2_verb2 = responses[24]
        fun_act1_2 = responses[25]
        fun_act2_2 = responses[26]
        fun_act3_2 = responses[27]
        adventure1_2 = responses[28]
        adventure2_2 = responses[29]
        adventure3_2 = responses[30]
        location1_2 = responses[31]
        location2_2 = responses[32]
        location3_2 = responses[33]
        interesting_object2 = responses[34]
        funny_sound2 = responses[35]
        snack_name2 = responses[36]
        humorous_event2 = responses[37]

        # Constructing the story with additional variables
        story = f"""
        Deep down. Under the world. There was a person named {name1} who stumbled upon an amazing friend named {friend_name1}. 
        This {friend_adj1} and {friend_adj2} friend was unlike any other and immediately became a best friend. Their adventures together 
        were the stuff legends are made of.

        The first thing {name1} wanted to do was to get a little crazy. They started with {activity1_verb}, which was done with a concerningly large amount of enthusiasm. 
        To their surprise, their friend picked it up quickly and even added a little flair! Next, they tried {activity2_verb}, which brought lots of laughter. You wouldn't believe how ridiculous that looked, even if you saw it.

        Their days were filled with all kinds of sus activities. They spent their afternoons {fun_act1}, {fun_act2}, and {fun_act3}, creating plenty of memorable moments.

        Their exciting adventures took them far and wide. First, they went on a journey to {adventure1}, 
        where they encountered a {interesting_object} that made a {funny_sound}. They then stopped by {location1} for a quick snack. What else could they have? 
        A big plate of {snack_name}, of course!"""
        st.write("Please wait while we prepare the story!")
        # Load image
        image_path = "image.png"
        image = Image.open(image_path)

        # Display thumbnail
        st.image(image, caption="Click to view larger", use_column_width=True)

        # Create a clickable link to view the larger image
        st.markdown(
            f'<a href="{image_path}" target="_blank"><img src="{image_path}" style="display: none;" /></a>',
            unsafe_allow_html=True)

        tts(story)
        st.empty()

        st.write(story)

        # Save and offer the MP3 file
        file_path = save_audio(story)
        st.markdown(f"[Download the audio file]({file_path})")
