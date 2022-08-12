
def find_name(info, data):
    if len(data) > 0:
        find =[]
        for row in data: 
            for x in row:
              if info in x:
                find.append(row)
                break
        return find
    else:
        return []

    