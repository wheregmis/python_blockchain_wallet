with open('demo.txt', mode='r') as f:
    # f.write('Add this content ! \n')
    file_content = f.readline()
    print(file_content)
print('done')
