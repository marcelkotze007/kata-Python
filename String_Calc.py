def Calculator(data):
    answer = 0
    list_delim = [",", "\n"]
    neg_message = 'negatives not allowed'
    
    if data == "":
        return answer
    elif "//" in data and "[" not in data:
        delim_end = data.index('\n')
        delim = data[2:delim_end]
        list_delim.append(delim)
        data = data[delim_end+1:]
    elif "[" in data and "][" not in data:
        delim_end = data.index(']\n')
        delim = data[3:delim_end]
        list_delim.append(delim)
        data = data[delim_end+2:]
    elif "][" in data:
        delim_end = data.index(']\n')
        delims = data[3:delim_end].split('][')
        for delim in delims: 
            list_delim.append(delim)
        data = data[delim_end+2:]

    for i in list_delim:
        data = data.replace(i, list_delim[0])
    values = data.split(',')

    for i in values:
        if int(i) < 0:
            neg_message = neg_message + " " + str(i)
        elif int(i) > 1000:
            pass
        else:
            answer = answer + int(i)

    if neg_message != 'negatives not allowed':
        return neg_message
    else:
        return answer