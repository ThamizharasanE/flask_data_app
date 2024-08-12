from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for processed data
processed_data = {}

# Mock data for simulation
mock_data = [
    {"id": 1, "value": "hello world"},
    {"id": 2, "value": "flask example"},
    {"id": 3, "value": "data processing"}
]


@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Simulate fetching data from an external service
    return jsonify(mock_data)


@app.route('/process-data', methods=['POST'])
def process_data():
    # Fetch data (using mock data for simplicity)
    data = mock_data

    # Process data: Convert all text to uppercase
    processed = [{"id": item["id"], "value": item["value"].upper()} for item in data]

    # Store processed data in in-memory storage
    processed_data['data'] = processed

    return jsonify({"message": "Data processed successfully"})


@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    # Return the processed data
    return jsonify(processed_data)


if __name__ == '__main__':
    app.run(debug=True)
