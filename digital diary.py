import json
import os
from datetime import datetime

DIARY_FILE = "digital_diary.json"


def load_entries():
    if not os.path.exists(DIARY_FILE):
        return []
    with open(DIARY_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_entries(entries):
    with open(DIARY_FILE, "w", encoding="utf-8") as file:
        json.dump(entries, file, indent=2, ensure_ascii=False)


def format_entry(entry):
    date = entry["date"]
    title = entry["title"]
    content = entry["content"]
    return f"Date: {date}\nTitle: {title}\n{content}\n{'-' * 40}"


def is_entry_editable(entry):
    try:
        entry_date = datetime.strptime(entry["date"], "%Y-%m-%d %H:%M")
    except ValueError:
        return False
    return entry_date.date() == datetime.now().date()


def update_entry(entries, index):
    entry = entries[index]
    print("\nUpdate entry - you can continue writing.")
    print("Press Enter twice to finish the update.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    if not lines:
        print("No new text added. Entry was not changed.")
        return entries
    entry["content"] += "\n" + "\n".join(lines)
    save_entries(entries)
    print("Entry updated successfully.\n")
    return entries


def display_entry_menu(entries, index):
    entry = entries[index]
    print("\n" + "-" * 40)
    print(format_entry(entry))
    editable = is_entry_editable(entry)
    if editable:
        print("Options:")
        print("1. Read only")
        print("2. Update this entry")
        print("3. Return")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            print("\nRead-only mode. No changes were made.")
            return entries
        elif choice == "2":
            return update_entry(entries, index)
        else:
            return entries
    else:
        print("This entry is older than today, so it is read-only.")
        input("Press Enter to return.")
        return entries


def add_entry(entries):
    print("\nAdd a new diary entry")
    print("-" * 30)
    title = input("Title: ").strip()
    if not title:
        title = "Untitled"
    print("Write your diary entry. Press Enter twice to finish.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    content = "\n".join(lines).strip()
    if not content:
        print("No content entered. Entry was not saved.")
        return entries

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "title": title,
        "content": content,
    }
    entries.append(entry)
    save_entries(entries)
    print("Entry saved successfully.\n")
    return entries


def view_entries(entries):
    print("\nYour diary entries")
    print("-" * 40)
    if not entries:
        print("No diary entries yet. Add one from the menu.")
        return entries
    for index, entry in enumerate(entries, start=1):
        print(f"Entry {index}")
        print(format_entry(entry))

    print("Enter an entry number to open it, or press Enter to return to the menu.")
    choice = input("Entry number: ").strip()
    if not choice:
        return entries
    if not choice.isdigit() or not (1 <= int(choice) <= len(entries)):
        print("Invalid entry number.")
        return entries
    return display_entry_menu(entries, int(choice) - 1)


def search_entries(entries):
    if not entries:
        print("\nNo entries to search. Add an entry first.")
        return
    search_term = input("\nEnter a keyword to search in titles and content: ").strip().lower()
    if not search_term:
        print("Search term is empty.")
        return
    matches = [entry for entry in entries if search_term in entry["title"].lower() or search_term in entry["content"].lower()]
    print(f"\nSearch results for '{search_term}':")
    print("-" * 40)
    if not matches:
        print("No matching entries found.")
        return
    for index, entry in enumerate(matches, start=1):
        print(f"Match {index}")
        print(format_entry(entry))


def main():
    entries = load_entries()
    while True:
        print("\nDigital Diary")
        print("1. Add entry")
        print("2. View all entries")
        print("3. Search entries")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            entries = add_entry(entries)
        elif choice == "2":
            entries = view_entries(entries)
        elif choice == "3":
            search_entries(entries)
        elif choice == "4":
            print("Goodbye! Your diary is saved in digital_diary.json.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
