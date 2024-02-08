# Single Responsibility Principle - Separation Of Concerns
class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)
    
    #def save(self, filename):
    #    file = open(filename, 'w')
    #    file.write(str(self))
    #    file.close()

    #def load(self, filename):
    #    pass

    #def load_from_web(self, uri):
    #    pass

class PersistenceManager:
    @staticmethod
    def save_to_file(jounal, filename):
        file = open(filename, 'w')
        file.write(str(jounal))
        file.close()
    

if __name__ == '__main__':
    j = Journal()
    j.add_entry('I cried today.')
    j.add_entry('I ate a bug.')
    print(f'Journal entries:\n{j}')

    filename = r'./journal.txt'
    PersistenceManager.save_to_file(j, filename)

    with open(filename) as fh:
        print(fh.read())
