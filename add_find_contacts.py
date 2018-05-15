class ContactBook(object):
    """docstring for ContactBook"""

    def __init__(self):
        super().__init__()  # for multiple inheritance
        self.contact_indices = {}

    # all letters, a, ab, abc, ..
    def all_orderings(self, contact):
        return [contact[0:idx] for idx in range(1, len(contact) + 1)]

    def add(self, contact):
        for key in self.all_orderings(contact):
            self.contact_indices[key] = self.contact_indices.get(key, 0) + 1

    def find(self, name):
        return self.contact_indices.get(name, 0)

    # n = int(input().strip())

    # for a0 in range(n):
    #     op, contact = input().strip().split(' ')
    #     if op == 'add':
    #         add(contact)
    #     elif op == 'find':
    #         count = find(contact)
    #         print(count)


if __name__ == '__main__':
    contact_book = ContactBook()
    contact_book.add('Sammy Al Hashemi')
    contact_book.add('Chris Natale')
    contact_book.add('Michael Pham-Hung')
    contact_book.add('Kelly Hunter')
    contact_book.add('Sammy Sosa')
    contact_book.add("Sam Harris")
    print(contact_book.find('Sam'))
