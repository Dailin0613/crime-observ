class SaveCSVFile:
    def __init__(self, filename):
        self.file_name = filename

    def __enter__(self):
        self.file_cont = open(self.file_name, mode='w')
        return self.file_cont

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_cont:
            self.file_cont.close()
