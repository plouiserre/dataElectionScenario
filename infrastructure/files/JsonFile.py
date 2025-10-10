class JsonFile : 
    def __init__(self):
        pass


    def write(self, content):
        with open("C:\\Users\\ploui\\OneDrive\\Bureau\\jsonresult\\data.json", "w") as f : 
            f.write(content)
        