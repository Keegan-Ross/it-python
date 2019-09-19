from banner import banner
banner("DEEP THOUGHTS", "Keegan Ross")

def main():
    run_event_loop()

def run_event_loop():
    print("What do you want to do with your journal?")
    command = None
    journal_data = []

    while command != "x":
        command = input("[L]ist entries, [A]dd an entry, E[x]it: ")

        if command == "L":
            list_entries(journal_data)
        elif command == "A":
            add_entry(journal_data)
        elif command != "x":
            print("Sorry, we do not understand")

def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for num, entry in enumerate(entries):
        print(f"[{num+1}] {entry}")

def add_entry(data):
    entry = input("Type your entry, <ENTER> to exit: ")
    data.append(entry)

main()