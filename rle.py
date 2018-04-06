import sys

def main():    
    rle = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = encode(rle)  

    print('RLE Vector: ' + rle)
    print('Encoded Result: ' + encoded)  

def encode(input):
    count = 1
    result = ''
    
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
        result += input[len(input)-1]
    else:
        result += str(count) + input[len(input)-1]

    return result

if __name__ == '__main__':
    main()