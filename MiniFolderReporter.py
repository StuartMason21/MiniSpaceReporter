# Storage Info for a given path. Useful for DFS name spaces.
import os
import time


def main():
    while True:
        print("*********************")
        get_target_space()
        user_continue = input(
            "Would you like to get the details of another path? Y/N: "
        )
        if user_continue.lower() != "y":
            print("Thanks for using this program, goodbye!")
            time.sleep(3)
            quit()


def get_target_space():
    target = input("Please paste your target path to obtain folder size (including sub-directories from this path): ")

    try:

        total_size = 0
        for dirpath, dirnames, filenames in os.walk(target):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
               
        print("Folder Size: %d GB" % (total_size // (2**30)))
        
        print("*********************")
    except Exception as e:
        print(e)
        print("*********************")


if __name__ == "__main__":
    main()
