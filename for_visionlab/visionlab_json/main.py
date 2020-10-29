import json
import logging

logging.basicConfig(filename="comparison.log", filemode='w', level=logging.INFO)
with open('books.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)


def book_count():
    # this function can count books with the same lang
    languages = {}
    for book in data:
        if book['language'] not in languages.keys():
            languages[(book['language'])] = [book['id']]
        else:
            languages[(book['language'])].append(book['id'])

    print(languages)
    logging.info(languages)
    return languages


def find_books(book_list):
    # in this function compares books which were founded two more times
    expensive_book = {'price': 0}
    cheapest_book = {'price': 99999}
    for id in book_list:
        for book in data:
            if book['id'] == id:
                cheapest_book = book if cheapest_book['price'] > book['price'] else cheapest_book
                expensive_book = book if expensive_book['price'] < book['price'] else expensive_book
    return cheapest_book, expensive_book


def compare_books(cheap, expensive):
    # compare the cheapest and the most expensive books and
    print(f'\n\n{cheap["language"]}')
    logging.info(f'\n\n{cheap["language"]}')
    for key, value in cheap.items():
        if value != expensive[key]:
            if type(value) == float:
                value = round(value, 5)
                expensive[key] = round(expensive[key], 5)
            logging.info(f'{value}  -------->  {expensive[key]}')
            print(f'{value}  -------->  {expensive[key]}')



def main():
    languages = book_count()
    for lang_list in languages.items():
        if len(lang_list[1]) > 1:
            cheap_book, expensive_book = find_books(lang_list[1])
            compare_books(cheap_book, expensive_book)
    logging.shutdown()

if __name__ == '__main__':
    main()
