class JsonFile : 
    def __init__(self, path):
        self.path = path
        pass

    def write(self, content):
        with open(self.path, "w") as f :          
            f.write(content)
        