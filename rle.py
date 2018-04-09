def main():
    rle = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = encode(rle)
    decoded = decode(encoded)

    print("Test Vector: " + rle)
    print("Encoded Result: " + encoded)  # Expected output: 12WB12W3B24WB14W
    print("Decoded Result: " + decoded)  # Expected output: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW


def encode(sequence):
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
