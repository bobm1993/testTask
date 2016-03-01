binary_digit = [1, 1, 1, 0, 0, 1, 1]


def decimal_output(bin_temp):

    dec_value = 0
    output = []
    if bin_temp[0] == 0 and len(bin_temp) > 1:
        print("ERROR! The first number in binary digit must be '1'")
        quit()
    for i in bin_temp:
        if i != 0 and i != 1:
            print("ERROR! Binary digit contains only '0' or '1'")
            quit()
    for idx, val in enumerate(bin_temp):
        if val == 1:
            dec_value += (-2)**idx
    inv_value = -1 * dec_value
    inv_value_saved = inv_value
    if bin_temp == [0]:
        output = [0]
    else:
        while inv_value != 0:
            if inv_value % 2 == 0:
                inv_value = (inv_value)/(-2)
                output.append(0)
            else:
                inv_value = (inv_value - 1)/(-2)
                output.append(1)
    return dec_value, inv_value_saved, output

print(decimal_output(binary_digit))