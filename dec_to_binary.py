def dec_to_bin(num_dec):
    num_bin = ''
    while num_dec >= 1:
        remainder = str(num_dec%2)
        num_bin = remainder + num_bin
        num_dec = num_dec//2
    return num_bin
    
num_dec = int(input("Enter an integer number: "))
num_bin = dec_to_bin(num_dec)
print(f"{num_dec} in binary is {num_bin}")