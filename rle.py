"""Run-length encoding and decoding functions."""


def main():
    """Demo usage of functions."""
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
    result = []

    for x,item in enumerate(sequence):
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:
            if count == 1:
                result.append(sequence[x - 1])
            else:
                result.append(str(count) + sequence[x - 1])
            count = 1

    if count == 1:
        result.append(sequence[len(sequence) - 1])
    else:
        result.append(str(count) + sequence[len(sequence) - 1])

    return "".join(result)


def decode(sequence):
    """Decode a sequence of characters.

       Keyword arguments:
       sequence -- the sequence of characters to decode.
       """
    count = ""
    result = []

    for x,item in enumerate(sequence):
        if item.isdigit():
            count += item
        else:
            if count != "":
                result.append(item * int(count))
            else:
                result.append(item)
            count = ""

    return "".join(result)


if __name__ == "__main__":
    main()
