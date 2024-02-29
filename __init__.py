from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def get_personas():
    return jsonify({"personas": personas})

if __name__ == "__main__":
    personas = [
        {"name": "Lina", "age": 21, "city": "Barranquilla"},
        {"name": "Teimineitor", "age": 53, "city": "Lima"},
        {"name": "Goku", "age": 25, "city": "Tokio"},
    ]
    app.run(debug=True, port=5000)
