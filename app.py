from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import os

# Initialize the Flask app
app = Flask(__name__)

# Set up the generative AI model
model = genai.GenerativeModel('gemini-pro')


# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 8014,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]


# Configure the API key for the generative AI model
genai.configure(api_key="AIzaSyD7vIY6ALNJqYR2C4T-Z-J8DaKw3rzNoiw")

# Configurating
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


# Define a 404 error handler to redirect to the index page (Not important to mention)
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

# Define the index route for both GET and POST requests
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
            # Get the user's prompt from the form
            prompt = request.form['prompt']
            question = prompt

            # Generate a response based on the user's prompt
            convo = model.start_chat(history=[])
            convo.send_message(question)

            # Return the generated text as the response
            return convo.last.text
    # Render the index.html template for GET requests
    return render_template('index.html')

# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
