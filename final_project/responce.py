from validatorcollection import validators

def main():
    email = input("What's your e-mail adress? ")

    try:
        valid = validators.email(email)
        return 'Valid'
    except:
        return 'Invalid'
        
if __name__ == "__main__":
    main()