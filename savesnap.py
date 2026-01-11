import os
import sys
import shutil
import hashlib
import webbrowser
from datetime import datetime

# ------------------- EDUCATION MODE -------------------

##Google_Colab = "https://colab.research.google.com/drive/1AShUGvvM2ZmdErMFRafbgLjgvEYSthTN#scrollTo=9MFcR2b0wnhl"
##
##def education_mode():
##    print("\nSaveSnap – Educational Mode")
##    print("Opening interactive explanations in Google Colab...\n")
##    webbrowser.open(Google_Colab)


def education_mode():
    while True:
        print("-------------------Educational Mode-------------------")
        print("1. init --- Initialization of repository")
        print("2. commit --- commit+hashing")
        print("3. checkout --- Checkout process")
        print("4. undo-checkout --- Undo Checkout")
        print("5. log --- Commit Logs")
        print("0. Exit")

        choice=int(input("Enter your choice : "))

        match choice:

            case 1:
                webbrowser.open('https://colab.research.google.com/drive/1lZbSa9P5UNq2tAZEyibrduXhcKrvA7zr#scrollTo=mEK7Byc97Kx6')

            case 2:
                webbrowser.open('https://colab.research.google.com/drive/1qQc-7of7ecQ2jTD1j-kB_3i4NfXUmyQu#scrollTo=XLCNtVcO5IEl')

            case 3:
                webbrowser.open('https://colab.research.google.com/drive/1zTVtdyLFdhpE6ib0LCQ4ZmWFKJBDhgj1#scrollTo=qZ7BjCc-6Lsr')

            case 4:
                webbrowser.open('https://colab.research.google.com/drive/1zTVtdyLFdhpE6ib0LCQ4ZmWFKJBDhgj1#scrollTo=qZ7BjCc-6Lsr')

            case 5:
                webbrowser.open('https://colab.research.google.com/drive/15vf06o9cw4sAZJObZ5bhH3gJ-wIJy_oz')

            case _:
                print("Invalid Choice ")

        if choice == 0:
            print('Exiting Education Mode......')
            break

#-----------------Global Configuration-------------------

repo_folder='.savesnap'
commits_folder=os.path.join(repo_folder,'commits')
backup_folder = os.path.join(repo_folder, ".checkout_backup")
log_file=os.path.join(repo_folder,'commit_log.txt')


#--------Initializing an repository-----------------

def init_repo():
    if os.path.exists(repo_folder):
        print('repository already exists')
        return

    os.makedirs(commits_folder)

    with open(log_file,'w') as f:
        f.write("SaveSnap Commit Log \n")

    print("SaveSnap repository created successfully ")


#-------------------Hashing function---------------------------------

def calculate_hash(file_path):
    hasher=hashlib.sha256()

    with open(file_path,'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()

#-------------create commits-------------

def create_commits(message , edu=False):
    if not os.path.exists(repo_folder):
        print("Repository not initialized Run initialisation first")
        return

    commit_id=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    commit_folder=os.path.join(commits_folder,f'commit_{commit_id}')
    os.makedirs(commit_folder)

    metadata_path = os.path.join(commit_folder,'metadata.txt')

    if edu:
        print('EDUCATIONAL MODE')
        print('Step 1 : Generating commit ID using timestamp')
        print("Step 2: Hashing files using SHA-256\n")

    with open(metadata_path,'w') as meta:
        meta.write('File MetaData (SHA-256 hashes) \n\n')

        for file in os.listdir():
            if file.startswith('.') or not os.path.isfile(file):
                continue

            file_hash = calculate_hash(file)
            shutil.copy(file,commit_folder)

            meta.write(f'\n\n{file} : {file_hash}\n\n')

            if edu:
                print(f'{file} hashed')
                print(f'Hash : {file_hash[:12]}')

    with open(log_file,'a') as f:
        f.write(f'\n Commit ID : {commit_id}\n')
        f.write(f'Time : {datetime.now()}\n')
        f.write(f'Message : {message}\n')

    print(f'Commit {commit_id} created successfully')


#------------Show logs------------------

def show_log():
    if not os.path.exists(log_file):
        print('No commit histroy available')
        return

    with open(log_file,'r') as f:
        print(f.read())


#---------------Checkout Commit-----------------

def checkout(commit_id):
    commit_folder = os.path.join(commits_folder, f'commit_{commit_id}')
    backup_folder = os.path.join(repo_folder, ".checkout_backup")

    if not os.path.exists(commit_folder):
        print('Commit not found')
        return

    # -------- Step 1: Backup current working directory --------
    if os.path.exists(backup_folder):
        shutil.rmtree(backup_folder)
    os.makedirs(backup_folder)

    for file in os.listdir():
        if file.startswith('.') or not os.path.isfile(file):
            continue
        shutil.copy(file, backup_folder)

    # -------- Step 2: Restore files from commit --------
    for file in os.listdir(commit_folder):
        if file == 'metadata.txt':
            continue
        src = os.path.join(commit_folder, file)
        dst = file
        shutil.copy(src, dst)

    print(f'Checked out commit {commit_id} successfully')
    print('Backup created. Use "undo-checkout" to restore previous state.')

#------------------------Undo Checkout--------------------------
def undo_checkout():
    if not os.path.exists(backup_folder):
        print("No checkout to undo.")
        return

    for file in os.listdir(backup_folder):
        shutil.copy(
            os.path.join(backup_folder, file),
            file
        )

    shutil.rmtree(backup_folder)
    print("Checkout undone. Working directory restored.")


#------------------------Main CLI---------------------------

def main():
    if len(sys.argv) < 2:
        print('Usage : ')
        print(' python savesnap.py init')
        print(" python savesnap.py commit \"message\"")
        print(" python savesnap.py log")
        print(' python savesnap.py checkout <commit_id>')
        print(' python savesnap.py undo-checkout')
        print(" python savesnap.py edu\n")
        return

    command = sys.argv[1]

    if command == 'init' :
        init_repo()

    elif command == 'commit' :
        if len(sys.argv) < 3:
            print('Commit message required')
            return
        message = sys.argv[2]
        create_commits(message)

    elif command == 'log' :
        show_log()

    elif command == 'checkout':
        if len(sys.argv) < 3:
            print('Commit ID required ')
            return
        checkout(sys.argv[2])

    elif command == 'undo-checkout':
        undo_checkout()


    elif command == 'edu':
        education_mode()

    else:
        print('Unknown command')

if __name__ == '__main__':
    main()
