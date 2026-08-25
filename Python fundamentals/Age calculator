from datetime import datetime

Subjects = [
    {"name":"Lionel Messi", "birthdate": "1987/07/24"},
    {"name":"Cristiano Ronaldo", "birthdate": "1985/02/05"},
    {"name":"Pelé", "birthdate": "1940/10/23"},
    {"name":"Diego Maradona", "birthdate": "1960/10/30"},
    {"name":"Johan Cruyff", "birthdate": "1947/04/25"},
    {"name":"Zinedine Zidane", "birthdate": "1972/06/23"},
    {"name":"Ronaldinho", "birthdate": "1980/03/21"},
    {"name":"Franz Beckenbauer", "birthdate": "1945/09/11"},
    {"name":"Ronaldo Nazário", "birthdate": "1976/09/18"},
    {"name":"Neymar", "birthdate": "1992/02/05"}
]

search_date = input("Which date do you want to search? (YYYY/MM/DD): ")

search_date = datetime.strptime(search_date, "%Y/%m/%d")

print("\nSubjects Information")
for subject in Subjects:
    birthdate = datetime.strptime(subject["birthdate"], "%Y/%m/%d")
    age = (search_date - birthdate).days // 365
    
    # Check if it's their birthday
    if search_date.month == birthdate.month and search_date.day == birthdate.day:
        if age == 0:
            print(f"\033[94mName: {subject['name']}, Age: {age} - It's their birthday! They just arrived!\033[0m")
        else:
            print(f"\033[94mName: {subject['name']}, Age: {age} - It's their birthday!\033[0m")
    # Check if age is 0 (just born)
    elif age == 0 and search_date >= birthdate:
        print(f"Name: {subject['name']}, Age: {age} - I just arrived!")
    # Check if the person hasn't been born yet
    elif search_date < birthdate:
        # Calculate years, months, and days until birth
        days_until_birth = (birthdate - search_date).days
        years_until = days_until_birth // 365
        remaining_days = days_until_birth % 365
        months_until = remaining_days // 30
        days_remaining = remaining_days % 30
        
        print(f"Name: {subject['name']}, Age: {age} - {years_until} years, {months_until} months and {days_remaining} days until birth")
    else:
        # Calculate days/months until next birthday
        next_birthday = birthdate.replace(year=search_date.year)
        if next_birthday < search_date:
            next_birthday = next_birthday.replace(year=search_date.year + 1)
        
        days_until = (next_birthday - search_date).days
        months_until = days_until // 30
        remaining_days = days_until % 30
        
        print(f"Name: {subject['name']}, Age: {age} - {months_until} months and {remaining_days} days until birthday")
