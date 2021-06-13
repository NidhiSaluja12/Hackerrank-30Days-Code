print_object = print

def print(*items_to_print):
    if 'Grade: ' in items_to_print:
        items_to_print = map(str, items_to_print)
        
        print_object(''.join(items_to_print))
    else:
        print_object(*items_to_print)

 

    
        
class Student(Person):
    # Using a super is the whole point of the exercise!
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if avg>=90 and avg<=100:
            return 'O'
        elif avg>=80 and avg<90:
            return 'E'
        elif avg>=70 and avg <80:
            return 'A'
        elif avg>=55 and avg<70:
            return 'P'
        elif avg>=40 and avg<55:
            return 'D'
        elif avg<40:
            return 'T'
    
