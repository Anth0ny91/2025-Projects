import os
import pathlib
import shutil
import platform

def get_folder_stats(folder_name: str):
    folder_path = pathlib.Path.home() / folder_name
    print(f"\nScanning: {folder_path}\n")

    if not folder_path.exists():
        print("Folder does not exist.")
        return

    total_size = 0
    file_count = 0

    for dirpath, _, filenames in os.walk(folder_path):
        for file in filenames:
            try:
                full_path = os.path.join(dirpath, file)
                total_size += os.path.getsize(full_path)
                file_count += 1
            except (PermissionError, OSError):
                continue

    kb = total_size / 1024
    mb = total_size / (1024 * 1024)

    print(f"Total size: {kb:.2f} KB")
    print(f"Total size: {mb:.2f} MB")
    print(f"Total files: {file_count}")


def get_trash_size():
    trash_path = pathlib.Path.home() / ".Trash"

    if not trash_path.exists():
        print("Trash folder not found.")
        return None

    total_size = 0
    file_count = 0

    for item in trash_path.rglob("*"):
        try:
            if item.is_file():
                total_size += item.stat().st_size
                file_count += 1
        except (PermissionError, OSError):
            continue

    kb = total_size / 1024
    mb = total_size / (1024 * 1024)

    print(f"\nTrash size: {kb:.2f} KB ({mb:.2f} MB)")
    print(f"Trash files: {file_count}\n")

    return trash_path


def empty_trash():
    system = platform.system()

    if system in ["Darwin", "Linux"]:
        trash_path = get_trash_size()
        if not trash_path:
            return

        confirm = input("Delete ALL Trash files? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return

        for item in trash_path.iterdir():
            try:
                if item.is_dir():
                    shutil.rmtree(item, ignore_errors=True)
                else:
                    item.unlink(missing_ok=True)
            except (PermissionError, OSError):
                continue

        print("Trash emptied.")
    else:
        print("Trash emptying not supported on this OS.")


while True:
    print("\nChoose folder to scan / action:")
    print("1 - Desktop")
    print("2 - Downloads")
    print("3 - Documents")
    print("4 - Trash Bin (Size + Delete Option)")
    print("5 - Exit")

    choice = input("Enter choice (1/2/3/4/5): ").strip()

    if choice == "1":
        get_folder_stats("Desktop")
    elif choice == "2":
        get_folder_stats("Downloads")
    elif choice == "3":
        get_folder_stats("Documents")
    elif choice == "4":
        empty_trash()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

    again = input("\nDo you want to try again? (y/n): ").strip().lower()
    if again != "y":
        print("Exiting...")
        break