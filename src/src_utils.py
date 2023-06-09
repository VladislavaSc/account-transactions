import os
import json

path_to_file = os.path.abspath('../hjk/')
path_to_transaction = os.path.join(path_to_file, 'operations.json')


def download_transactions():

    with open(path_to_transaction, 'r', encoding='utf8') as file:
        transactions_list = json.load(file)

        return transactions_list


def last_five_transactions(transaction_list):

    sort_list = [transac for transac in transaction_list if transac != {} and transac['state'] == 'EXECUTED']
    sort_list.sort(key=lambda dictionary: dictionary['date'], reverse=True)
    clean_list = sort_list[0:5]

    return clean_list
