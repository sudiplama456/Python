def my_split(sentence, separator):
    result = []
    current = ""
    for char in sentence:
        if char == separator:
            result.append(current)
            current = ""
        else:
            current += char
    result.append(current)
    return result

def my_join(items, separator):
    result = ""
    for i, item in enumerate(items):
        result += item
        if i < len(items) - 1:
            result += separator
    return result

def main():
    sentence = input("Please enter sentence: ")
    split_result = my_split(sentence, " ")
    print(my_join(split_result, ","))
    for word in split_result:
        print(word)

if __name__ == "__main__":
    main()