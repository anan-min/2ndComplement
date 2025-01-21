

def twos_complement_to_integer(binary_string, n_bytes):
    # check invalid value 
    # check for the first digit 
    # if negative
    # else positive (normal convertation)
    # return integer 

    if not is_input_valid(binary_string, n_bytes):
        raise ValueError("Error: Binary string must be 8 bits long for 1 byte.")
    
    first_digit = binary_string[0]
    result = 0
    if first_digit == "1":
        # negative number ``
        binary_string = complement(binary_string)
        result = int(binary_string, 2) - 2**(n_bytes * 8)
    else:
        # positive number
        result = int(binary_string, 2) 

    return result 

def unsigned_to_integer(unsigned_string, n_bytes):

    if not is_input_valid(unsigned_string, n_bytes):
        raise ValueError("Error: Binary string must be 8 bits long for 1 byte.")
    
    return int(unsigned_string, 2)



def is_input_valid(binary_string, n_bytes):
    # what are all the possible size
    if n_bytes not in [1, 2, 4]:
        return False
    elif len(binary_string) != n_bytes * 8:
        return False
    else:
        return True
    

def complement(binary_string):
    complemented = ''.join('1' if bit == '0' else '0' for bit in binary_string)
    return complemented



def test_binary():
    str1 =  "00000000"
    str2 =  "00000001"
    str3 =  "00000010"
    str4 =  "01111110"
    str5 =  "01111111"

    str6 =  "10000000"
    str7 =  "10000001"
    str8 =  "10000010"
    str9 =  "11111110"
    str10 = "11111111"

    positive_string= [str1, str2, str3, str4, str5]
    negative_string = [str6, str7, str8, str9, str10]

    for str in positive_string:
        print(f"\ninput: {str} 2nd output: {twos_complement_to_integer(str, 1)}")
        print(f"input: {str} unsigned output: {unsigned_to_integer(str, 1)}")

    for str in negative_string:
        print(f"\ninput: {str} 2nd output: {twos_complement_to_integer(str, 1)}")
        print(f"input: {str} unsigned output: {unsigned_to_integer(str, 1)}")



test_binary()

    