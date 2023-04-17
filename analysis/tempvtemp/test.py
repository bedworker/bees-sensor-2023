with open('tempvtemp.log') as fp:
    average_array, outside_array = [], []

    for line in fp.readlines():
        average, outside = line.split(':')
        average_array.append(float(average))
        outside_array.append(float(outside))
    
    print(sorted(average_array))
    # print(len(outside_array))
    # print(f'Inside Max: {sorted(average_array, reverse=True)[0]}')
    # print(f'Outside Max: {sorted(outside_array, reverse=True)[0]}')

    # x = np.array(average_array)
    # y = np.array(outside_array)
