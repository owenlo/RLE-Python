def main():    
    rle = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"  
    encoded = encode(rle)  
    decoded = decode(encoded)

    print('Test Vector: ' + rle)
    print('Encoded Result: ' + encoded)  #Expected output: 12WB12W3B24WB14W
    print('Decoded Result: ' + decoded)  #Expected output: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

def encode(input):    
    count = 1
    result = ""
    
    for x in range(len(input)):
        if (x == 0):           
            continue              
        elif (input[x] == input[x - 1]):
            count += 1        
        else:        
            if(count == 1):
                result += input[x - 1]        
            else:
                result += str(count) + input[x - 1]        
            count = 1
    
    if(count == 1):
        result += input[len(input) - 1]
    else:
        result += str(count) + input[len(input) - 1]

    return(result)

def decode(input):
    count = ""
    result = ""

    for x in range(len(input)):
        if input[x].isdigit():
            count += input[x]
        else:
            if(count != ""):
                result += input[x] * int(count)
            else:
                result += input[x]
            count = ""

    return(result)

if __name__ == '__main__':
    main()