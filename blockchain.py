# Initializing our blockchain list
blockchain = []


# this function returns the last blockchain value
def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# This function accepts two arguments.
# One required one(transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]
def add_transaction(transaction_amount, last_transaction=[1]):
    """Append a new value as well as the last blockchain value to the blockchain 

    Arguments: 
        :transaction_amount = The amount that should be added

        :last_transaction = The last blockchain transaction
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (new transaction amount) as a Float """
    # Get the user input, transform it from a string to a float and store it
    user_input = float(input('Your transaction amount please: '))
    return user_input


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
        print('Done')


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit the program')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()

        add_transaction(last_transaction=get_last_blockchain_value(),
                        transaction_amount=tx_amount)
    elif user_choice == '2':
        # Output the blockchain list to the console
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('The input was invalid, please pick a value from the list !')
    print('Choice Register')

print('Done')
