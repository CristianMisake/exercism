class Allergies:

    def __init__(self, score):
        self.score = score
        self.items = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128,
        }

    def allergic_to(self, item):
        if self.score == 0:
            return False
        return self.items[item] in self.pown_two()

    def pown_two(self):
        score = self.score
        while score > 256:
            score -= 256
        ult = 128
        resp = []
        while score != 0 and ult != 0:
            if score >= ult:
                resp.append(ult)
                score -= ult
            ult //= 2
        return resp

    @property
    def lst(self):
        if self.score == 0:
            return []
        find_in = self.pown_two()
        return [value for value in self.items if self.items[value] in find_in]
