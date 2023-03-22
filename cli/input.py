def list(alternativeList, question):
    print(question)
    for i in range(0, len(alternativeList)):
        print('  ', i+1, ': ', alternativeList[i], sep='')

    while True:
        answer = int(input("Select a number: "))
        if answer > 0 and answer <= len(alternativeList):
            return answer - 1
            