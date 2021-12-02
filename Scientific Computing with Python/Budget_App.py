class Category:

    def __init__(self, category):
        self.category_name = category
        self.ledger = list()

        self.safebox = 0
        self.spent = 0






    def __repr__(self):

        txt = str()
        txt = f"{self.category_name:*^30}\n"
        for registro in self.ledger:
            txt += f"{registro['description'][0:23]:<23}{registro['amount']:>7.2f}\n"
        txt += f"Total: {self.safebox:.2f}"
        return txt







    def deposit(self, amount, description=''):

        self.ledger.append({"amount": amount, "description": description})
        self.safebox += amount

    def withdraw(self, amount, description=''):

        if amount <= self.safebox:
            self.ledger.append({"amount": -amount, "description": description})
            self.safebox -= amount
            self.spent += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.safebox


    def transfer(self, amount, category):

        if amount <= self.safebox:
            self.ledger.append({"amount": -amount, "description": f"Transfer to {category.category_name}"})
            self.safebox -= amount
            self.spent += amount

            category.ledger.append({"amount": amount, "description": f"Transfer from {self.category_name}"})
            category.safebox += amount
            return True

        else:
            return False
    

    def check_funds(self, amount):

        if amount <= self.safebox:
            return True
        else:
            return False



def create_spend_chart(categories):
    spends = 0
    for contas in categories:
        spends += contas.spent

    txt = "Percentage spent by category\n"
    for x in range(100, -10, -10):
        txt = txt + f"{x:>3}| "
        for types in categories:
            media = int((types.spent/spends)*100)
            txt += f"{'o  ' if media >= x and media < x+10 or media >= x else 3*' '}"
        txt += f"\n"
    txt += f"{' '*4}-{'-'*len(categories)*3}\n"
    tamanho_nomes = len(categories[0].category_name), len(categories[1].category_name), len(categories[2].category_name)
    for x in range(max(tamanho_nomes)):
        txt += f"{' '*5}"
        for types in categories:
            txt += f"{types.category_name[x] if x <= len(types.category_name)-1 else ' '}{' '*2}"
        txt += "\n" if x != max(tamanho_nomes)-1 else ''

    return txt




if __name__ == '__main__':
    food = Category("Food")
    entertainment = Category("entertainment")
    business = Category("business")
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    print(create_spend_chart([food, entertainment, business]))


