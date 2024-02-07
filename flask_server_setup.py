from flask import Flask, render_template, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API key
# openai.api_key = 'your-openai-api-key'

# Global variable to store conversation history
# conversation_history = []

@app.route('/test')
def hello():
    print("Hello")

# Default route to serve index.html
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# # API route to handle POST requests
# @app.route('/api', methods=['POST'])
# def api():
#     global conversation_history
#
#     # Get the string from the request data
#     input_string = request.form.get('input_string')
#
#     # Append user input to conversation history
#     conversation_history.append({'role': 'user', 'message': input_string})
#
#     # Call OpenAI API to generate a response
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt="\n".join([f"{entry['role']}: {entry['message']}" for entry in conversation_history]),
#         max_tokens=50
#     )
#
#     # Extract the generated text from the OpenAI response
#     generated_text = response.choices[0].text.strip()
#
#     # Append bot response to conversation history
#     conversation_history.append({'role': 'bot', 'message': generated_text})
#
#     # Return the generated text as JSON response
#     return jsonify({'generated_text': generated_text})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
