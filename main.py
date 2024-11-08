def binary_to_decimal(binary):
    binary_dict = {'0':0, '1':1}
    decimal_value = 0
    for i in range(len(binary)):
        decimal_value = decimal_value * 2 + binary-dict[binary[i]]
    return decimal_value
binary_input =input("Enter a binary number: ")
print("The decimalform of", binary_input,"is",binary_to_decimal(binary_input))

