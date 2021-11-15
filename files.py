with open('dream_team.txt', mode='r') as f:
    # f.write('Add this content ! \n')
    file_content = f.readlines()
    print(f'{file_content[0][:-1]} {file_content[1]}')
    print(f'{file_content[2][:-1]} {file_content[3]}')
    print(f'{file_content[4][:-1]} {file_content[5]}')
    print(f'{file_content[6][:-1]} {file_content[7]}')
    print(f'{file_content[8][:-1]} {file_content[9]}')
    print(
        f'Total {int(file_content[1][:-1]) + int(file_content[3][:-1]) + int(file_content[5][:-1]) + int(file_content[7][:-1]) + int(file_content[9][:-1])}')
