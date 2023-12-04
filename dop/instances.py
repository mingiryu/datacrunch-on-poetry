from dop.client import client


def main():
    for instance in client.instance_types.get():
        print(instance)


if __name__ == "__main__":
    main()
