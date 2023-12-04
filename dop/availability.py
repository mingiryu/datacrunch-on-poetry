from dop.client import client, IS_SPOT


def main():
    for instance in client.instances.get_availabilities(is_spot=IS_SPOT):
        print(instance)


if __name__ == "__main__":
    main()
