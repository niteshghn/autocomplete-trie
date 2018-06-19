import csv
import os
from trie import Trie


class Connector:
    @staticmethod
    def search(word):
        return list(trie.search(word))


FILE = os.environ.get("FILE", "baby-names.csv")
trie = Trie()
with open(FILE) as f:
    readCSV = csv.reader(f, delimiter='\n')
    for row in readCSV:
        trie.insert(row[0].lower())


if __name__ == '__main__': # for testing purpose
    res = Connector.search('james')
    if res:
       print("Result PASS")
    else:
        print("Test fail")