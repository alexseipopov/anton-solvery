class Solver:
    sumer_procent = 3000
    cost_per_people = 10000
    
    def __init__(self, month:str, count:int):
        self.month = month
        self.count = count
        self.N_month = None
        self.result = None
        self.conters()
        
    def conters(self):
        self.__month_to_int()
        self.solve_result()
        self.discount()
        self.price_down()

    def __month_to_int(self):
        mth = ["JAN", "FEB", "MARCH", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        if self.month in mth:
            self.N_month = mth.index(self.month)

    def price_down(self):
        if self.result > 60_000:
            self.result -= 10_000

    def discount(self):
        if self.count > 5:
            self.result *= 0.4

    def summer_cost(self):
        return (self.cost_per_people + self.sumer_procent) * self.count

    def winter_cost(self):
        return (self.cost_per_people * 0.9) * self.count

    def solve_result(self):
        if 5 <= self.N_month <= 7:
            self.result = self.summer_cost()
        elif self.N_month == None:
            print("Что-то не так")
        else:
            self.result = self.winter_cost()



obj = Solver("JAN", 5)
print(obj.result)