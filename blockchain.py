# Initializing our blockchain list
# initial block = genesis block
genesis_block = {'previous_hash': '',
                 'index': 0,
                 'transactions': []
                 }
blockchain = [genesis_block]
open_transactions = []
owner = 'Sabin'
participants = {'Sabin'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant]
                 for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant]
                    for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


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
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transactions': open_transactions
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
    return True


waiting_for_input = True
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output the participants')
    print('h: Manipulate the chain')
    print('q: Quit the program')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient=recipient, amount=amount)
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
    print(get_balance('Sabin'))
else:
    print('User left!')


print('Done')
