class Course:
    def __init__(self, cid, name, credit):
        self.cid = cid
        self.name = name
        self.credit = credit

    def show(self):
        print(f"{self.cid} - {self.name} - {self.credit} credits")
