from PIL import Image
import os
import sys
import json

i = open("meta.json", "r+")
data = json.load(i)

def filecheck(file, filetype):
    filefound = True
    if file not in data[filetype]:
        if filetype == "photos":
            imgURL = "photos/" + file
            try:
                img = Image.open(imgURL)
                img.show()
            except:
                print("Can't show file.", file)
            print("--- %s ---" % (file))
            name = input("Name: ")
            year = input("Year: ")
            location = input("Location: ")
            desc = input("Description: ")
            camera = input("Camera: ")
            film = input("Type of film: ")
            data[filetype][file] = {
                "filename": file,
                "name": name,
                "year": year,
                "location": location,
                "desc": desc,
                "camera": camera,
                "film": film
            }
        elif filetype == "videos":
            print("--- %s ---" % (file))
            name = input("Name of file: ")
            year = input("Year: ")
            desc = input("Description: ")
            role = input("Role: ")
            comments = input("Comments: ")
            data[filetype][file] = {
                "filename": file,
                "name": name,
                "year": year,
                "desc": desc,
                "role": role,
                "comments": comments
            }
        elif filetype == "scripts":
            print("--- %s ---" % (file))
            name = input("Name of file: ")
            year = input("Year: ")
            desc = input("Synopsis: ")
            writers = input("Writers: (Jake Williams) ")
            comments = input("Comments: ")
            if writers:
                writers = writers
            else:
                writers = "Jake Williams"
            data[filetype][file] = {
                "filename": file,
                "name": name,
                "year": year,
                "desc": desc,
                "writers": writers,
                "comments": comments
            }

def updateEntry(file):
    print("Keys available:")
    for a in data[file]:
        print(a)
    k = input("Which entry would you like to update? ")
    print("Old value: ", data[file][k])
    n = input("New value: ")
    print("Entry changed from %s to %s." % (data[file][k], n))
    data[file][k] = n

def updates():
    c = input("Would you like to update any existing entries? (y/n): ")
    if c == "y":
        return True
    elif c == "n":
        return False
    else:
        updates()

def dir(q):
    if q == "photos":
        print("Cycling through photos.")
        directory = os.fsencode("photos")
    elif q == "videos":
        print("Cycling through videos.")
        directory = os.fsencode("videos")
    elif q == "scripts":
        print("Cycling through scripts.")
        directory = os.fsencode("scripts")
    updatesValue = updates()
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith("."):
            print("Potentially ignoring:", filename)
            f = input("Would you like to ignore this file? (y/n): ")
            if f == "n":
                filecheck(filename, q)
            elif f == "y":
                print("Ignoring:", filename)
            else:
                print("Invalid input. Ignoring:", filename)
            continue
        else:
            filecheck(filename, q)
            print("Entry exists for:", filename)
            if updatesValue == True:
                u = input("Update entry for %s? (y/n): " % (filename))
                if u == "y":
                    updateEntry(filename)
                elif u == "n":
                    continue
                else:
                    print("Invalid input. Continuing...")
            else:
                continue
    writeData()
    main()

def writeData():
    print("Writing new data...")
    i.seek(0)
    i.write(json.dumps(data))
    i.truncate()
    print("File updated. Exiting.")

def main():
    print("Would you like to cycle through 'photos', 'videos', or 'scripts'?")
    print("Press enter to exit.")
    q = input("> ")
    if q:
        dir(q)
    else:
        writeData()
        sys.exit()

main()