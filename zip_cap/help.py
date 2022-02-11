import zipfile
import requests
class help:
    def __init__(self, url):
        zip = requests.get(url)
        with zipfile.ZipFile(zip) as f:
            print('hi')


    def hits(self, string):
        pass

    def files(self, string):
        pass

    def grep(self, string):
        pass

if __name__ == '__main__':
    zpath = 'https://docs.python.org/3/archives/python-3.10.2-docs-text.zip'
    h = help(zpath)