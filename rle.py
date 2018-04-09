def main():
    rle = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = encode(rle)
    decoded = decode(encoded)

    print("Test Vector: " + rle)

    # Expected output: 12WB12W3B24WB14W
    print("Encoded Result: " + encoded)

    # Expected output: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
    print("Decoded Result: " + decoded)


def encode(sequence):
    """Encode a sequence of characters.

    Keyword arguments:
    sequence -- the sequence of characters to encode.
    """
    count = 1
    result = ""

    for x in range(len(sequence)):
        if x == 0:
            continue
        elif sequence[x] == sequence[x - 1]:
            count += 1
        else:
            if count == 1:
                result += sequence[x - 1]
            else:
                result += str(count) + sequence[x - 1]
            count = 1

    if count == 1:
        result += sequence[len(sequence) - 1]
    else:
        result += str(count) + sequence[len(sequence) - 1]

    return result


def decode(sequence):
    """Decode a sequence of characters.

       Keyword arguments:
       sequence -- the sequence of characters to decode.
       """
    count = ""
    result = ""

    for x in range(len(sequence)):
        if sequence[x].isdigit():
            count += sequence[x]
        else:
            if count != "":
                result += sequence[x] * int(count)
            else:
                result += sequence[x]
            count = ""

    return result


if __name__ == "__main__":
    main()
