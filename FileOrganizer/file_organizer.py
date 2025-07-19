"""
A modular Python script for organizing files in a selected directory by either
file *type* (extension), *date modified* (Year/Month), or for flattening directory
structure by moving all files to a single folder and removing subfolders.
The script is structured so the core logic can be imported into a future GUI
(Tkinter, PyQt, etc.) without modification.
"""
from collections import defaultdict
from datetime import datetime
import os
import sys
import shutil

#Get the folder path after checking if the path exists 
def get_folder_path() -> str:
    """
    Prompt user for a directory path and validate it
    Returns 
    ----------
    str
        Absolute directory path provided by the user
    """
    folder_path=str(input("Enter the full path of the folder you want to organize:\n> ").strip())

    #Check if the entered path exists and is a folder
    if not os.path.exists(folder_path):
        print("The path does not exist. Exiting…")
        sys.exit(1)

    # Check if the path is in fact a directory
    if not os.path.isdir(folder_path):
        print("The path is not a directory. Exiting…")
        sys.exit(1)

    print(f"Folder found: {folder_path}")
    return os.path.abspath(folder_path)

def list_files(folder_path: str) -> list[str]:
    """Returns **file** names only (exlude sub-directories)

    Args:
        folder_path (str): _description_

    Returns:
        list[str]: _description_
    """
    return [
        f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))
    ]

def get_extension(filename:str)->str:
    """Return the clean, upper-case extension (or 'NO_EXTENSION')

    Args:
        filename (str): _description_

    Returns:
        str: _description_
    """
    _, ext=os.path.splitext(filename)
    return ext[1:].upper() if ext else "NO_EXTENSION"

def get_year_month(filename: str, folder_path:str)-> tuple[str,str]:
    """Return 

    Args:
        filename (str): _description_
        folder_path (str): _description_

    Returns:
        tuple[str,str]: _description_
    """
    full_path=os.path.join(folder_path,filename)
    ts=os.path.getmtime(full_path)
    dt=datetime.fromtimestamp(ts)
    return str(dt.year),f"{dt.month:02d}"

# Below are the function to summarize file types as needed
def summarize_by_extension(files:list[str])->dict[str,str]:
    """count how many files exists for each extension

    Args:
        files (list[str]): _description_

    Returns:
        dict[str,str]: _description_
    """
    summary: dict[str,str]=defaultdict(int)
    for f in files:
        summary[get_extension(f)]+=1
    return dict(summary)

def summarize_by_year(files: list[str],folder_path:str)->dict[str,int]:
    """Count how many files were modified in each year

    Args:
        files (list[str]): _description_
        folder_path (str): _description_

    Returns:
        dict[str,int]: _description_
    """
    summary: dict[str,int]=defaultdict(int)
    for f in files:
        year,_=get_year_month(f,folder_path)
        summary[year]+=1
    return dict(summary)

#Below are the functions to organize the files
def create_extension_folders(folder_path:str,files:list[str])->None:
    """Create a sub folder for every extension found in files

    Args:
        folder_path (str): _description_
        files (list[str]): _description_
    """
    created: set[str]=set()
    for f in files:
        ext=get_extension(f)
        if ext not in created:
            os.makedirs(os.path.join(folder_path,ext),exist_ok=True)
            print(f"Created folder:{ext}")
            created.add(ext)

def move_files_by_extension(folder_path:str,files:list[str])->None:
    """<pve eacj fo;es omtp its corresponding extension folders.

    Args:
        folder_path (str): _description_
        files (list[str]): _description_
    """
    for f in files:
        ext=get_extension(f)
        src=os.path.join(folder_path,f)
        dst_dir=os.path.join(folder_path,ext)
        dst=os.path.join(dst_dir,f)
        shutil.move(src,dst)
        print(f" Moved: {f} -> {ext}/")

def create_date_folder(folder_path:str,files:list[str])->None:
    """Create nested Year/month folders based on last modification date.

    Args:
        folder_path (str): _description_
        files (list[str]): _description_
    """
    created:set[tuple[str,str]]=set()
    for f in files:
        year, month=get_year_month(f,folder_path)
        if(year,month) not in created:
            path=os.path.join(folder_path,year,month)
            os.makedirs(path,exist_ok=True)
            print(f"Created folder: {year}/{month}")
            created.add((year,month))

def move_files_by_date(folder_path:str,files:list[str])->None:
    """Move files into year/month folders based on the last modifiecation date

    Args:
        folder_path (str): _description_
        files (list[str]): _description_
    """
    for f in files:
        year,month=get_year_month(f,folder_path)
        src=os.path.join(folder_path,f)
        dst_dir=os.path.join(folder_path,year,month)
        dst=os.path.join(dst_dir,f)
        shutil.move(src,dst)
        print(f"Moved: {f} -> {year}/{month}/")

#Cleanup function to move all the sub files into parent folder
def flatten_and_cleanup(folder_path:str)-> None:
    """move all files from subfolders into the main folder and delete the subfolders

    Args:
        folder_path (str): _description_
    """
    print("\n Flattening all files into the main folder...")
    moved_files=0
    for root, dirs, files in os.walk(folder_path,topdown=False):
        for f in files:
            src=os.path.join(root,f)
            dst=os.path.join(folder_path,f)
            if src!=dst:
                shutil.move(src,dst)
                moved_files+=1
                print(f"Moved:{src} -> {dst}")
        #Remove empty subfolders
        if root!=folder_path:
            try:
                os.rmdir(root)
                print(f" removed folder: {root}")
            except OSError:
                pass
    print(f"Flattened {moved_files} files into {folder_path}")


# Below are the functions for CLI interface 
def cli_menu()->None:
    """Simple Command line interface for user selection
    """
    folder_path=get_folder_path()
    files=list_files(folder_path)

    #Print summaries
    print("\n File type summary")
    for ext,count in summarize_by_extension(files).items():
        print(f"{ext}:{count} files")
    
    print("\n File year summary:")
    for year,count in summarize_by_year(files,folder_path).items():
        print(f"{year}: {count} files")
    
    #Menu definitions
    print("\nHow would you like to organize your files?")
    print("1. By file type (extension)")
    print("2. By date modified (Year/Month)")
    print("3. Flatten All: Move all files to root & delete subfolders")
    choice=input("Enter 1, 2 or 3 (or any other key to cancel): ").strip()

    if choice=="1":
        print("\nOrganizing by file type...")
        create_extension_folders(folder_path,files)
        move_files_by_extension(folder_path,files)
        print("Completed organization by file type.")
    
    elif choice=="2":
        print("\nOrganizing by date modified...")
        create_date_folder(folder_path,files)
        move_files_by_date(folder_path,files)
        print("Completed organization by file type.")
    
    elif choice == "3":
        print("\nFlattening folder and removing subdirectories…")
        flatten_and_cleanup(folder_path)

    else:
        print("Operation cancelled. No changes were made")
    
# Main call
if __name__=="__main__":
    cli_menu()
