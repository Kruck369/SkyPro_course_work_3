class Operation:
    def __init__(self, date, description, where_from, where_to, summ, currency, status):
        self.date = date
        self.description = description
        self.where_from = where_from
        self.where_to = where_to
        self.summ = summ
        self.currency = currency
        self.status = status

    def build_output(self):
        return f"""{self.date} {self.description}
{self.where_from} -> {self.where_to}
{self.summ} {self.currency}
"""

