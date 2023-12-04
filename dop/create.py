from dop.client import client, IS_SPOT, SSH_KEY_ID, HOSTNAME


def main(
    instance_type="CPU.4V.16G",
    image="ubuntu-22.04-cuda-12.0-docker",
    ssh_key_id=SSH_KEY_ID,
    hostname=HOSTNAME,
    description=None,
    is_spot=IS_SPOT,
):
    instance = client.instances.create(
        instance_type=instance_type,
        image=image,
        ssh_key_ids=[ssh_key_id],
        hostname=hostname,
        description=description or f"{image} on {instance_type}",
        is_spot=is_spot,
    )
    print(instance)


if __name__ == "__main__":
    main()
