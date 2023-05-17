import datetime

print("Diary app(is this an app?) by Aria Crestia\n")
print("Do you want to make a diary entry?")
choice = " "

# The while block below prompts the user for input
# Included an exception catcher for KeyboardInterrupt
try:
    while (choice != "y") or (choice != "n"):
        choice = str.lower(input("[Y/N]: "))
        if (choice == "y"):
            print("Starting entry...")
            break
        elif (choice == "n"):
            print("As you wish. Exiting the program...")
            quit()
            break
        else:
            print("Invalid input.")
except KeyboardInterrupt:
    print("Exiting the application...")
    quit()

# Newline
# print("\n")
# The paragraph entry is done below.
# The user is also prompted about
# whether or not to keep the entry.
keep = " "
try:
    diaryEntryParagraph = str(input("\nStart your entry here: "))
    print("\nWould you like to keep this entry?")
    while (keep != "y") or (keep != "n"):
        keep = str.lower(input("[Y/N]: "))
        if (keep == "y"):
            print("As you wish...")
            # This will save the diary entry to a file
            filename = 'Diary Entries.txt'
            with open(filename, 'a') as file_object:
                file_object.write(str(datetime.datetime.now().date()) +
                                  "\n" +
                                  str(datetime.datetime.now().time().hour) + ":" +
                                  str(datetime.datetime.now().time().minute) + ":" +
                                  str(datetime.datetime.now().time().second) +
                                  "\n" +
                                  "-" + "\n" +
                                  diaryEntryParagraph +
                                  "\n-\n\n")
            print("Entry saved.\n"
                  "Exiting the program...")
            quit()
            break
        elif (keep == "n"):
            print("As you wish. Exiting the program...")
            quit()
            break
        else:
            print("Invalid input.")
except KeyboardInterrupt:
    print("Exiting the application...")
    quit()
