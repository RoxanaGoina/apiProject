from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint simplu care returnează un mesaj
@app.route('/')
def home():
    return jsonify({"message": "Hello from Render Cloud!"})

# Endpoint pentru salutări personalizate
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# Endpoint care primește și procesează date JSON
@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.json
    if not data or "numbers" not in data:
        return jsonify({"error": "Invalid input, please provide a list of numbers"}), 400

    total = sum(data["numbers"])
    return jsonify({"sum": total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
