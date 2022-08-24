# with open('./pairs.txt') as result:
#     uniqlines = set(result.readlines())
#     with open('./pairs1.txt', 'w') as rmdup:
#         rmdup.writelines(set(uniqlines))


with open("./pairs.txt", 'r+') as reader:

    while reader:
        symbol = reader.readline()
        print("==>> symbol: ", symbol)
        if symbol == '':
            break
    reader.close()
