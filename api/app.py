from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/calculate_tokens', methods=['POST'])
def calculate_tokens():
    data = request.get_json()
    if not data:
        response = make_response(jsonify({"error": "Invalid JSON"}), 400)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    prompt = data.get('prompt')
    model = data.get('model')
    language = data.get('language')

    if not prompt or not model or not language:
        response = make_response(jsonify({"error": "Missing fields"}), 400)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    # Thực hiện tính toán tokens dựa trên prompt, model và language
    # Đây chỉ là ví dụ giả định, bạn cần thay thế bằng logic thật của bạn
    token_count = len(prompt.split())

    response = make_response(jsonify({"tokens": token_count}))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)

