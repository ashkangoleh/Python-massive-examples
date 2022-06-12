import argparse
# from faker import Faker
# import json

# Adding optional argument
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-m", "--message", type=str, help="Message", required=False)
parser.add_argument("-n1", "--number1", type=int, help="number 1", required=False)
parser.add_argument("-n2", "--number2", type=int, help="number 2", required=False)
# Read arguments from command line
args = parser.parse_args()
print('args: ', args)


def main(message: str = None, num1: int = 1, num2: int = 2):
    return message, num1 + num2


# fake = Faker()


# def get_registered_user():
#     return {
#         "name": fake.name(),
#         "address": fake.address(),
#         "created_at": fake.year()
#     }


if __name__ == "__main__":
    # fakeData = json.dumps(get_registered_user(), indent=4)
    # print('fakeData: ', fakeData)
    # msg, add = main()
    msg, add = main(args.message, args.number1, args.number2)
    print(msg) if msg is not None else print('',end="")
    print(f"{add=}")
