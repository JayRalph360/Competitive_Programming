def split_and_join(line):
    # write your code here
    words = line.split()  # Split the line into a list of words
    joined_string = "-".join(words)  # Join the words using a hyphen
    return joined_string


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
