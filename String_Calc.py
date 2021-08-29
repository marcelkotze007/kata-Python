def Calculator(data):
    answer = 0
    values = []

    if data == "":
        return 0
    
    values = data.split(',')

    for i in values:
        answer = answer + int(i)

    return answer