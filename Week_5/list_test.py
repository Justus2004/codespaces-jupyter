
def transaction_tracking():
    transactions_list = list()
    transactions_list.append(new_transaction(input("Eine Art der Transaction eingeben: "),input("Eine Menge eingeben: "),input("Ein Datum eingeben: ")))
    print(sum_day_trans(transactions_list))
    
def sum_day_trans(transaction_list):
    date =  "2024-01-15"
    date in transaction_list


def new_transaction(kind,price,date):
    transaction = {'type':kind,'amount':price,'date':date}
    return transaction

transaction_tracking()