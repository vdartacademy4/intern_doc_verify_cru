import os

def create_intern_folder(reg_no, name):

    folder_name = f"{reg_no}_{name}"

    folder_path = os.path.join(
        "uploads",
        folder_name
    )

    os.makedirs(
        folder_path,
        exist_ok=True
    )

    return folder_path