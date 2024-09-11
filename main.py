import os
import streamlit as st
from gtts import gTTS
from io import BytesIO
from datetime import datetime

# Initialize session state to track question progress
if 'step' not in st.session_state:
    st.session_state.step = 0

if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Updated Questions list
questions = [
    "Enter a name",
    "Enter a name for a companion",
    "Enter an adjective describing the companion",
    "Enter another adjective describing the companion",
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
    "Enter a second name",
    "Enter a second name for another companion",
    "Enter another adjective describing the second companion",
    "Enter yet another adjective describing the second companion",
    "Enter a second verb related to an activity",
    "Enter another second verb related to an activity",
    "Enter a second fun activity",
    "Enter another second fun activity",
    "Enter one more second fun activity",
    "Enter a second exciting adventure",
    "Enter another second exciting adventure",
    "Enter a third second exciting adventure",
    "Enter a second favorite location",
    "Enter another second favorite location",
    "Enter a third second favorite location",
    "Enter a second interesting object",
    "Enter a second funny sound",
    "Enter a second name for a snack",
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


# Display current question and input box
if st.session_state.step < len(questions):
    current_question = questions[st.session_state.step]
    st.text_input(current_question, key='text_input', on_change=handle_input)

    if st.button("Next"):
        handle_input()
else:
    # Button to generate the story after all questions are answered
    if st.button("Generate Story"):
        # Collecting all responses
        responses = st.session_state.responses

        # Extracting variables from responses
        name1 = responses[0]
        companion_name1 = responses[1]
        companion_adj1 = responses[2]
        companion_adj2 = responses[3]
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
        companion_name2 = responses[20]
        companion_adj1_2 = responses[21]
        companion_adj2_2 = responses[22]
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
        Once upon a time, there was a person named {name1} who stumbled upon an amazing companion named {companion_name1}. 
        This {companion_adj1} and {companion_adj2} companion was unlike any other and immediately became a best friend. Their adventures together 
        were the stuff of legends.

        The first thing {name1} wanted to do was engage in some incredible activities. They started with {activity1_verb}, which was done with great enthusiasm. 
        To their surprise, their companion picked it up quickly and even added a little flair! Next, they tried {activity2_verb}, which brought lots of laughter.

        Their days were filled with fun activities too. They spent their afternoons {fun_act1}, {fun_act2}, and {fun_act3}, creating plenty of memorable moments.

        Their exciting adventures took them far and wide. First, they went on a journey to {adventure1}, where they encountered unexpected wonders. 
        Next, they ventured to {adventure2}, where they tried something new and exciting. Finally, they explored {adventure3}, uncovering hidden surprises!

        {name1} also had favorite places to visit. They first went to {location1}, where they enjoyed a fun time with a giant {interesting_object}. 
        Then they traveled to {location2}, a place known for its unique snacks like {snack_name}. Their last stop was {location3}, where they enjoyed a lively atmosphere filled with {funny_sound} sounds.

        But the story doesn't end there. The adventures continued with {name2} and their new companion, {companion_name2}. This second companion was 
        equally {companion_adj1_2} and {companion_adj2_2}, and they joined in on all the fun. They learned to {activity1_verb2} and {activity2_verb2} 
        with just as much enthusiasm. Their new fun activities included {fun_act1_2}, {fun_act2_2}, and {fun_act3_2}.

        Their new adventures took them to {adventure1_2}, where they discovered more wonders, {adventure2_2}, where they created even more memories, 
        and {adventure3_2}, a place full of new experiences. They loved visiting {location1_2}, {location2_2}, and {location3_2}, enjoying a new 
        {interesting_object2} and sampling {snack_name2}. They ended their adventures with a lively experience at {location3_2}, where the crowd made 
        even more delightful {funny_sound2} sounds.

        In the end, {name2} and {companion_name2} knew that their friendship, like {name1} and {companion_name1}'s, was filled with laughter, joy, and endless fun. 
        Their days were unforgettable, filled with every type of excitement imaginable.
        """
        st.subheader("Your Story:")
        st.write(story)

        # Save the audio and provide a download link
        file_path = save_audio(story)
        st.success(f"Audio saved to {file_path}.")
        st.audio(file_path, format='audio/mp3')
