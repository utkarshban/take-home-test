from flask import Flask, jsonify, request
from user_transactions import UserTransactions, TransactionsException

class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv

app = Flask(__name__)

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(TransactionsException)
def transactions_exception_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/user/add/transaction", methods=['POST'])
def add_transaction():
    data = request.get_json()
    add_transaction_validate(data)
    transactions.add_transaction(data)
    return jsonify({"message": "Successfully added!"})

@app.route("/user/spend", methods=['POST'])
def spend():
    data = request.get_json()
    spend_validate(data)
    return jsonify(transactions.spend(data))

@app.route("/user/balance")
def balance():
    return jsonify(transactions.balance())

def add_transaction_validate(data):
    check_data(data)
    if ("payer" in data and "points" in data and "timestamp" in data) == False:
        raise InvalidAPIUsage("Pass 'payer', 'points', and 'timestamp' in the body!")
    if (isinstance(data["payer"], str) and isinstance(data["points"], int) and isinstance(data["timestamp"], str)) == False:
        raise InvalidAPIUsage("'payer' should be a string, 'points' should be an integer, and 'timestamp' should be a string!")

def spend_validate(data):
    check_data(data)
    if "points" not in data:
        raise InvalidAPIUsage("Pass 'points' in the body!", 400)
    if not isinstance(data["points"], int):
        raise InvalidAPIUsage("'points' should be an integer!")

def check_data(data):
    if data == None or isinstance(data, dict) == False:
        raise InvalidAPIUsage("JSON Body is required!")


if __name__ == '__main__':
    transactions = UserTransactions()
    app.run(host='0.0.0.0')
