import os

folders = os.listdir("uploads")

for folder_name in folders:

    folder_path = os.path.join(
        "uploads",
        folder_name
    )

    if os.path.isdir(folder_path):

        print(folder_name)