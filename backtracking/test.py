def get_century():
    year = int(input("Enter year: \n"))
    century = year // 100
    decade = (year - (century * 100)) // 10
    return str(century), str(decade) + "0"


century, decade = get_century()
print("century is " + century)
print("decade is " + decade)
