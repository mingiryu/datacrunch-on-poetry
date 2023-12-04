from dop.client import client


def main():
    ssh_keys = client.ssh_keys.get()

    for ssh_key in ssh_keys:
        print(ssh_key.id, f"({ssh_key.name})")


if __name__ == "__main__":
    main()
