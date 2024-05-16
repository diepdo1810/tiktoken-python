from flask import Flask, request, jsonify
import tiktoken

app = Flask(__name__)

# Load encoding models
encodings = {
    'gpt-3.5-turbo': tiktoken.encoding_for_model('gpt-3.5-turbo'),
    'gpt-4': tiktoken.encoding_for_model('gpt-4'),
}

@app.route('/calculate_tokens', methods=['POST'])
def calculate_tokens():
    data = request.json

    prompt = data.get('prompt', '')
    model = data.get('model', 'gpt-3.5-turbo')
    language = data.get('language', 'English')

    if model not in encodings:
        return jsonify({'error': 'Model not supported'}), 400

    if language not in ['Vietnamese', 'English']:
        return jsonify({'error': 'Language not supported'}), 400

    encoding = encodings[model]
    tokens = encoding.encode(prompt)
    token_count = len(tokens)

    return jsonify({
        'prompt': prompt,
        'model': model,
        'language': language,
        'token_count': token_count
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

