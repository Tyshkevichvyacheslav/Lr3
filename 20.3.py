print("Несвежие анекдоты")
def print_only_new():
    old_messages = set()
    while True:
        message = input()
        if message not in old_messages:
            print(message)
        old_messages.add(message)


if __name__ == '__main__':
    print_only_new()

input("Press any key to exit")
exit(0)
