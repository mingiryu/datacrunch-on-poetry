from dop.client import client


def main():
    for volume in client.volumes.get():
        print(volume)


if __name__ == "__main__":
    main()
