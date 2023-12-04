from dop.client import client


def main(
    instance_id="",
):
    client.instances.action(instance_id, client.constants.instance_actions.DELETE)


if __name__ == "__main__":
    main()
