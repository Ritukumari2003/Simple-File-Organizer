import os  # Provides functions to interact with the operating system

def arrange_files(files, ext, folder_name):
    """
    Moves files of a given extension into a user-selected folder.
    Includes error handling to avoid crashes.
    """

    try:
        # Select only files (ignore folders) that match the given extension
        files_with_ext = [
            file for file in files
            if file.endswith(ext) and os.path.isfile(file)
        ]

        # If no matching files are found, stop execution
        if not files_with_ext:
            print(f"No {ext} files found.")
            return

        # Create the folder if it does not exist
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print(f"Folder '{folder_name}' created.")
        else:
            print(f"Using existing folder '{folder_name}'....")

        count = 0  # Counter for successfully moved files

        # Loop through each file that matches the extension
        for file in files_with_ext:
            try:
                # Destination path for the file
                new_path = os.path.join(folder_name, file)

                # Skip file if it already exists in the destination folder
                if os.path.exists(new_path):
                    print(f"{file} File already exists in the selected folder!!...")
                    continue

                # Move the file to the chosen folder
                os.rename(file, new_path)
                count += 1

            except PermissionError:
                # Raised if file is open or access is denied
                print(f"Permission denied while moving: {file}")

            except FileNotFoundError:
                # Raised if file is missing during execution
                print(f"File not found: {file}")

            except Exception as e:
                # Handles any unexpected error for a specific file
                print(f"Error moving {file}: {e}")

        # Display summary after moving files
        print()
        print(f"{count} file(s) moved to '{folder_name}'.")
        print()

    except Exception as e:
        # Handles unexpected errors in the function
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    try:
        # Get all files and folders from the current directory
        files = os.listdir()

        # Ask user for file extension
        ext = input("Enter file extension (e.g. .jpg, .pdf): ").strip()

        # Validate file extension format
        if not ext.startswith("."):
            raise ValueError("Extension must start with '.'")

        # Ask user how they want to handle folders
        print("\nChoose folder option:")
        print("1. Use an existing folder")
        print("2. Create a new folder")
        print()

        choice = input("Enter 1 or 2: ").strip()
        print()

        # Validate choice input
        if choice not in ("1", "2"):
            raise ValueError("Invalid choice. Please enter 1 or 2.")

        # Ask user for folder name
        folder_name = input("Enter folder name: ").strip()
        print()

        # Ensure folder name is not empty
        if not folder_name:
            raise ValueError("Folder name cannot be empty.")

        # Call the function to organize files
        arrange_files(files, ext, folder_name)

    except ValueError as ve:
        # Handles incorrect user inputs
        print("Input Error:", ve)

    except Exception as e:
        # Handles any other unexpected error
        print("Something went wrong:", e)
