from functools import reduce
import hashlib
from collections import OrderedDict
from hash_util import hash_block, hash_string_256
# Initializing our blockchain list
MINING_REWARD = 10
# initial block = genesis block
genesis_block = {'previous_hash': '',
                 'index': 0,
                 'transactions': [],
                 'proof': 100
                 }
blockchain = [genesis_block]
open_transactions = []
owner = 'Sabin'
participants = {'Sabin'}


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant]
                 for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant]
                    for block in blockchain]
    amount_received = reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


# This function accepts two arguments.
# One required one(transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain 

    Arguments: 
        :sender = The sender of the coin

        :receipient = The receiver of the coin

        :amount = The amount to be transfered (default = 1.0)
    """
    #transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    transaction = OrderedDict(
        [('sender', sender), ('recipient', recipient), ('amount', amount)])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    # reward_transaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINING_REWARD
    # }
    reward_transaction = OrderedDict(
        [('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transactions': copied_transactions,
             'proof': proof
             }
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns the input of the user (new transaction amount) as a Float """
    # Get the user input, transform it from a string to a float and store it
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    """ Returns the input of the user's choice as a Integer """
    # Get the user input and store it
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    """ Print the blocks in the blockchain """
    for block in blockchain:
        print('Outputing Block')
        print(block)
    else:
        print('*' * 20)


def verify_chain():
    ''' Verify the current blockchain and return True if it's valid, False if its invalid'''
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output the participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit the program')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient=recipient, amount=amount):
            print('Transaction Successful')
        else:
            print('Transaction Failed')
        print(open_transactions)
    elif user_choice == '2':
        # Mine a block
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        # Output the blockchain list to the console
        print_blockchain_elements()
    elif user_choice == '4':
        # Output the participants list to the console
        print(participants)
    elif user_choice == '4':
        # Verifying Transactions
        if verify_transactions():
            print('All transactions verified')
        else:
            print('There are some invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '',
                             'index': 0,
                             'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 20}]
                             }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('The input was invalid, please pick a value from the list !')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain')
        break
    print('Balance of {}: {:6.2f}'.format('Max', get_balance('Sabin')))
else:
    print('User left!')


print('Done')
