from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]

        if score <= 100 and score >= 90:
            return "A"
        elif score <= 89 and score >= 80:
            return "B"
        elif score <= 79 and score >= 70:
            return "C"
        elif score <= 69 and score >= 60:
            return "D"
        elif score <= 59 and score >= 50:
            return "E"
        else:
            return "F"

    def find(self, find_score):
        list_of_index = []

        for i, score in enumerate(self.scores):
            if score == find_score:
                list_of_index.append(i)

        return list_of_index


    def get_sorted(self):
        scores = self.scores[:]
        for i in range(len(scores)):
            for y in range(0, (len(scores)) - i - 1):
                if scores[y] > scores[y + 1]:
                    scores[y], scores[y + 1] = scores[y + 1], scores[y]

        return scores


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count())

    for i, score in enumerate(results.scores):
        print(f"Student {i}: {results.scores[i]} points – {results.get_grade(i)}")

    for i, score in enumerate(results.scores):
        if results.scores[i] == 100:
            print(i)

    print(results.get_sorted())


    random_results = StudentsGrades(random_numbers(30, 0, 100))

    print(random_results.count())
    print(random_results.get_sorted())



if __name__ == "__main__":
    print(main())




