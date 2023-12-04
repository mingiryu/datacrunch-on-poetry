from dop.client import client


def main():
    for image in client.images.get():
        print(image.image_type)


if __name__ == "__main__":
    main()
