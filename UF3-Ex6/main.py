
import csv

def main():
    book = dict()
    book['isbn'] = input("Introdueix l'isbn del llibre: ")
    book['title'] = input("Introdueix el títol del llibre: ")
    book['author'] = input("Introdueix l'autor del llibre: ")
    book['editorial'] = input("Introdueix l'editorial del llibre: ")
    book['pub_date'] = input("Introdueix la data de publicació del llibre: ")

    try:
        with open('files/books.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['isbn', 'title', 'author', 'editorial', 'pub_date']
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writeCSV.writeheader()
            writeCSV.writerow(book)
    except:
        print("No s'ha pogut inserir el registre.")
    else:
        print("El registre s'ha inserit correctament.")

if __name__ == '__main__':
    main()
