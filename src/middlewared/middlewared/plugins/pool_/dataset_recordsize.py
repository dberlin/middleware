def generate_recordsize_choices():
    with open('/sys/module/zfs/parameters/zfs_max_recordsize') as f:
        val = int(f.read().strip())
        choices = []
        for raw_val, human_readable in MAPPING.items():
            if int(raw_val) <= val:
                choices.append(human_readable)
        return choices


# https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Module%20Parameters.html#zfs-max-recordsize
# Maximum supported (at time of writing) is 16MB.
MAPPING = {
    f'{1 << 9}': '512B',
    f'{2 << 9}': '1K',
    f'{2 << 10}': '2K',
    f'{2 << 11}': '4K',
    f'{2 << 12}': '8K',
    f'{2 << 13}': '16K',
    f'{2 << 14}': '32K',
    f'{2 << 15}': '64K',
    f'{2 << 16}': '128K',
    f'{2 << 17}': '256K',
    f'{2 << 18}': '512K',
    f'{2 << 19}': '1M',
    f'{2 << 20}': '2M',
    f'{2 << 21}': '4M',
    f'{2 << 22}': '8M',
    f'{2 << 23}': '16M',
}
ZFS_DATASET_RECORDSIZE_CHOICES = generate_recordsize_choices()
