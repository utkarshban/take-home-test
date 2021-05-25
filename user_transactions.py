import heapq
from collections import defaultdict
class UserTransactions:
    def __init__(self):
        self.transactions_heap = []
        self.payer_points = defaultdict(int)
        self.total_user_points = 0

    def add_transaction(self, data):
        payer, points, timestamp = data["payer"], data["points"], data["timestamp"]
        self.validate_add_transaction_data(data)
        self.payer_points[payer] += points
        self.total_user_points += points
        heapq.heappush(self.transactions_heap, [timestamp, points, payer])

    def spend(self, data):
        self.validate_spend_data(data)
        spend_amount = data["points"]
        self.total_user_points -= spend_amount
        deductions = defaultdict(int)
        while(spend_amount):
            [timestamp, points, payer] = heapq.heappop(self.transactions_heap)
            if spend_amount >= points:
                spend_amount -= points
                self.payer_points[payer] -= points
                deductions[payer] -= points
            else:
                remaining_points = points - spend_amount
                heapq.heappush(self.transactions_heap, [timestamp, remaining_points, payer])
                self.payer_points[payer] -= spend_amount
                deductions[payer] -= spend_amount
                spend_amount = 0
        return UserTransactions.dict_to_list(deductions)

    def balance(self):
        return self.payer_points

    def validate_add_transaction_data(self, data):
        if data["points"] + self.payer_points[data["payer"]] < 0:
            raise TransactionsException("Payer points can't go negative!")

    def validate_spend_data(self, data):
        if data["points"] < 0:
            raise TransactionsException("Should spend non-negative points!", 400)
        if data["points"] > self.total_user_points:
            raise TransactionsException("Not enough points!", 400)

    @classmethod
    def dict_to_list(cls, deductions):
        deductions_list = []
        for deduction in deductions:
            deductions_list.append({"payee": deduction, "points": deductions[deduction]})
        return deductions_list

class TransactionsException(Exception):
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
