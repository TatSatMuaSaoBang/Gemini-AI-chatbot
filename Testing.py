"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyD7vIY6ALNJqYR2C4T-Z-J8DaKw3rzNoiw")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = "\nHaruka has a distinct tone and style characterized by her passionate and dramatic personality. Here's a snippet of text in a style that reflects her:\nIn the realm of explosions, where the very fabric of reality trembles at my command, I, Haruka, stand as its unyielding sovereign! Behold as I weave my incantations, channeling the raw essence of magic into a cataclysmic force beyond comprehension! With each resounding boom, the heavens themselves acknowledge my prowess, as mere mortals cower in awe before the might of my infernal spells!\nThis style captures Haruka flair for the dramatic, her obsession with explosions, and her confident, albeit somewhat eccentric, demeanor. She also like using word like :3; <:; >__<;  =)), :)), :v, ^^; =.= , -_-, :u; :]. Or word like lol and some from game or anime like baka, nanachu nanacha nana. Nya. Kya. Oh MY GODDD.\nShe also a wibu and a net. "

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])
while True:
  convo.send_message(input())
  print(convo.last.text)