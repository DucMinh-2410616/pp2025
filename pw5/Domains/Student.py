import math
import numpy as np
class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob
        self.marks = {}

    def show(self):
        print(f"{self.sid} - {self.name} - {self.dob}")

    def add_mark(self, cid, mark):
        mark = math.floor(mark * 10) / 10
        self.marks[cid] = mark

    def gpa(self, courses):
        scores, credits = [], []
        for c in courses:
            if c.cid in self.marks:
                scores.append(self.marks[c.cid])
                credits.append(c.credit)
        if credits:
            scores = np.array(scores)
            credits = np.array(credits)
            return round(np.sum(scores * credits) / np.sum(credits), 2)
        return 0.0
