# Storage Info for a given path. Useful for DFS name spaces.
import shutil
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
    target = input("Please paste your target path to obtain disk usage (not folder size specifically): ")

    try:

        total, used, free = shutil.disk_usage(target)

        print("Disk space info for: " + str(target))
        print("Total: %d GB" % (total // (2**30)))
        print("Used: %d GB" % (used // (2**30)))
        print("Free: %d GB" % (free // (2**30)))
        print("*********************")
    except Exception as e:
        print(e)
        print("*********************")


if __name__ == "__main__":
    main()
