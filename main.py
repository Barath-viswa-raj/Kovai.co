from get_folders import get_folders
from create_folder import create_folder
from update_folder import update_folder
from delete_folder import delete_folder

def main():
    print(" Document360 Drive Folder API Automation (Mocked)\n")
    get_folders()
    folder_name = input("\n Enter name for new folder: ").strip()
    if not folder_name:
        print("Folder name cannot be empty.")
        return

    folder_id = create_folder(folder_name)

    if folder_id:
        new_name = input("\n Enter new name to rename the folder: ").strip()
        if new_name:
            update_folder(folder_id, new_name)
        else:
            print(" Skipping rename — no new name provided.")

        confirm = input(f"\nDo you want to delete '{new_name or folder_name}'? (yes/no): ").strip().lower()
        if confirm in ["yes", "y"]:
            delete_folder(folder_id)
        else:
            print(" Folder was not deleted.")
    else:
        print(" Folder creation failed. Aborting update/delete steps.")

if __name__ == "__main__":
    main()
