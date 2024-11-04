#moving all 0s to the end of the list while maintaining the order of the other elements

def movezeros(numbers):
    non_zeros=[]
    for numb in numbers:
        if numb !=0:
            non_zeros.append(numb)
    zero_count = numbers.count(0)

    #concatinating the list of non zero at first then at the end of the list the zero's
    return non_zeros + [0]*zero_count

numbers = [0, 1, 0, 3, 15, 0, 5]
print(movezeros(numbers))

