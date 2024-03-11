import os #this library is to work with files and directories 

def organize_files(directory, prefix=""):  
    '''
    directory: The directory containing the files to be renamed.
    prefix: The prefix to be added to each file name (default is "new").
    '''

    # check if directory exists
    if not os.path.exists(directory):
        print("Errox: the specified directory does not exist.")
        return

    # iterate through files in the specified directory
    for filename in os.listdir(directory):
         # get the full file path
         file_path = os.path.join(directory, filename)
         # check if the file is a regular file
         if os.path.isfile(file_path):
             # split filename and extension
             base_name, file_extension = os.path.splitext(filename)
             # construct new filename with prefix and suffix
             new_filename = f"{prefix}{base_name}{file_extension}"
             # construct new directory path based on file extension
             new_directory = os.path.join(directory, file_extension[1:].upper())
             # create directory if it doesn't exist
             if not os.path.exists(new_directory):
                 os.makedirs(new_directory)
             # move the file to the new directory
             os.rename(file_path, os.path.join(new_directory, new_filename))
             print(f"Moved {filename} to {new_directory}")



def main():
    directory = input("Enter the directory path: ")
    prefix = input("Enter the prefix: ")
    organize_files(directory, prefix)

if __name__ == "__main__":
    main()