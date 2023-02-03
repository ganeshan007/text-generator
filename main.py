import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen

st.title("Text Generator App:")

# instantiate the model / download
ai = aitextgen(model_folder="QProject1/",tokenizer_file="Qproject1/aitextgen.tokenizer.json")

# create a prompt text for the text generation 
#prompt_text = "Python is awesome"
prompt_text = st.text_input(label = "Enter your prompt text...",
            value = "Sherlock Holmes")

with st.spinner("AI is at Work........"):
    # text generation
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 100 )
st.success("The AI Successfully generated the below text ")
# st.balloons()
# print ai generated text
print(gpt_text)

st.text(gpt_text)