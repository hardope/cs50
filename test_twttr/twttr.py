def main():
    ...
    text = input("Input: ")

    print(f"Output: {shorten(text)}")

def shorten(word):
    ...
    vowels = ['a','e','i','o','u']
    
    word = word.replace('a', "")
    word = word.replace('u', "")
    word = word.replace('o', "")
    word = word.replace('i', "")
    word = word.replace('e', "")
    word = word.replace('A', "")
    word = word.replace('E', "")
    word = word.replace('I', "")
    word = word.replace('O', "")
    word = word.replace('U', "")
    

    return word


if __name__ == "__main__":
    main()

