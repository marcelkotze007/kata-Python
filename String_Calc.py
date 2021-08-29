def Calculator(data):
    answer = 0
    values = []
    delim_list = [',','\n']

    if data == "":
        return 0
    
    for i in delim_list:
        data = data.replace(i, delim_list[0])

    values = data.split(',')

    for i in values:
        answer = answer + int(i)

    return answer