#Storage Info for a given path. Useful for DFS name spaces.
import shutil

def main():
    target = input("please paste your target path: ")
       
    try:
        
        total, used, free = shutil.disk_usage(target)       

        print ("Disk space info for: " + str(target))
        print("Total: %d GB" % (total // (2**30)))
        print("Used: %d GB" % (used // (2**30)))
        print("Free: %d GB" % (free // (2**30)))
    except Exception as e:
        print (e)

if __name__ == '__main__':
    main()
