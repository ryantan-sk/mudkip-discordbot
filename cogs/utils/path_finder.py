import os


def file_paths(path):
    all_path = []
    for root, dirs, file in os.walk(path):
        for name in file:
            all_path.append(os.path.join(root, name))

    return all_path


def file_name(path):
    basename = os.path.basename(path)
    return os.path.splitext(basename)[0]


