print("pradzia")

authors = [
    {
        "id":1,
        "name":"Jane",
        "surname":"Austen"
    },
    {
        "id":2,
        "name":"George",
        "surname":"Orwell"
    },
    {
        "id":3,
        "name":"Ernest",
        "surname":"Hemingway"
    }
]
id_counter = 3
while True:
    print("1 - Check the authors available")
    print("2 - Add an author to library")
    print("3 - Edit an author")
    print("4 - Remove an author")
    print("5 - Exit library")
    option = input()
    match option:
        case "1":
            print("Here is the list of authors:")
            for author in authors:
                print(author)
        case "2":
            print("Enter author's first name:")
            first_name = input()
            print("Enter author's surname:")
            last_name = input()
            id_counter +=1
            author = {"id":id_counter, "name":first_name, "surname":last_name}
            authors.append(author)
        case "3":
            print("Enter the ID of the author you want to edit:")
            edit_id = input()
            for i, author in enumerate(authors):
                if str(author["id"]) == edit_id:
                    print("Enter the author's first name:")
                    authors[i]["name"] = input()
                    print("Enter the author's last name:")
                    authors[i]["surname"] = input()
        case "4":
            print("Enter the ID of the author you want to delete:")
            del_id = input()
            for author in authors:
                if str(author["id"]) == del_id:
                    authors.remove(author)
                    break
        case "5":
            print("You have left the library")
            break
        case _ :
            print("Please insert a valid author ID")
