def format_report(func):
    def wrapper(self):
        print("\n----- REPORT -----")
        func(self)
        print("------------------")
    return wrapper

class Report:
    def __init__(self, title, data):
        self.title = title
        self.data = data

    @classmethod
    def create(cls, title, data):
        return cls(title, data)

    def __str__(self):
        return self.title

    @format_report
    def generate(self):
        print("Title:", self.title)
        for item in self.data:
            print(item)

r = Report.create("Student Report",
                  ["Aryan - 85", "Rahul - 90"])

r.generate()
