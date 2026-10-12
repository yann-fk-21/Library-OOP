from models import Book, Member
from library import Library




def show_menu():
    print("=== Bibliothèque ===")
    print("1. Lister les livres disponibles")
    print("2. Ajouter un livre")
    print("3. Ajouter un membre")
    print("4. Emprunter un livre")
    print("5. Retourner un livre")
    print("0. Quitter")

library = Library(name="Localhost Librairie")


while True:
    show_menu()
    choice = int(input("Choix : "))
    if choice == 0:
        break
    elif choice == 1:
        print("=== Liste des livres disponibles")
        available_books = library.list_available_books()
        for i, available_book in enumerate(available_books):
            print(f"{i+1}. Titre: {available_book.title}, Auteur: {available_book.author}, ISBN: {available_book.isbn}")
    elif choice == 2:
        title_book = input("Entrez le titre du livre: ")
        author_book = input("Entrez le nom de l'auteur: ")
        isbn_book = input("Entrez le ISBN: ")

        book = Book(title=title_book, author=author_book, isbn=isbn_book)
        library.add_book(book)
        print(f"Le livre {title_book} a été ajouter avec succès!")

    elif choice == 3:
        member_name = input("Entrez votre nom: ")
        member_id = input("Entrez vote ID: ")

        member = Member(name=member_name, member_id=member_id)
        library.add_member(member)

    elif choice == 4:
        print("=== Liste des livres disponibles")
        available_books = library.list_available_books()
        for i, available_book in enumerate(available_books):
            print(f"{i+1}. Titre: {available_book.title}, Auteur: {available_book.author}, ISBN: {available_book.isbn}")

        try:
            num_book = int(input("Entrez le numéro du livre à emprunter: "))
            borrowed_book = library.books[num_book-1]
        except IndexError as error:
            print("[ERROR] Numéro du livre inexistant!")
        else:
            borrowed_book.mark_as_borrowed()
            print(f"Vous avez emprunter le livre {borrowed_book.title}")

    elif choice == 5:
        isbn_book = input("Entrez l'ISBN du livre: ")
        return_book = [book for book in library.books if book.isbn == isbn_book]

        if len(return_book) == 0:
            print("Ce livre n'existe pas!")
        else:
            return_book[0]._is_available = True
            print("Vous avez retourner le livre avec succès!")
    else:
        print("Choix invalide!")


    

        

            
    
