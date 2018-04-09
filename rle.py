def main():    
    rle = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"  
    encoded = encode(rle)  
    decoded = decode(encoded)

    print('Test Vector: ' + rle)
    print('Encoded Result: ' + encoded)  # Expected output: 12WB12W3B24WB14W
    print('Decoded Result: ' + decoded)  # Expected output: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW


def encode(plaintext):
    count = 1
    result = ""
    
    for x in range(len(plaintext)):
        if x == 0:
            continue              
        elif plaintext[x] == plaintext[x - 1]:
            count += 1        
        else:        
            if count == 1:
                result += plaintext[x - 1]
            else:
                result += str(count) + plaintext[x - 1]
            count = 1
    
    if count == 1:
        result += plaintext[len(input) - 1]
    else:
        result += str(count) + plaintext[len(plaintext) - 1]

    return result


def decode(cipher):
    count = ""
    plaintext = ""

    for x in range(len(cipher)):
        if cipher[x].isdigit():
            count += cipher[x]
        else:
            if count != "":
                plaintext += cipher[x] * int(count)
            else:
                plaintext += cipher[x]
            count = ""

    return plaintext


if __name__ == '__main__':
    main()
