# 1. Créez un nouveau fichier appelé "bank_account.py"
# 2. Définissez la classe Account et ses attributs comme spécifié ci-dessus.
class Account:

    def __init__(self, name, account_number, account_balance, account_holder):
        self.name = name
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    # 3. Définissez la méthode deposit(). Il doit prendre en compte un argument, le montant à déposer, et l'ajouter au solde du compte
    def deposit(self, amount: float):
        if amount > 0:
            self.account_balance += amount
            print(f"Le montant déposé est {amount}")
        else:
            print("Le montant doit être supérieur à zéro")

    # 4. Définissez la méthode Remove().
    # Il doit prendre en compte un argument, le montant à retirer, et le soustraire du solde du compte.
    # La méthode ne doit exécuter le retrait que si le solde du compte est supérieur ou égal au montant à retirer.
    def remove(self, subtract_amount):
        if self.account_balance >= subtract_amount:
            self.account_balance -= subtract_amount
            print(f"Le montant retiré est {subtract_amount}")
        else:
            print("Vous ne pouvez pas effectuer de retrait car le solde est insuffisant")

    # 5. Définissez la méthode check_balance(). Il devrait renvoyer le solde du compte courant.
    def check_balance(self):
        print(f"Le solde courant est : {self.account_balance}")

# 6. Créez une instance de la classe Account et affectez-la à une variable appelée "my_account".

my_account = Account("Daouda", 1355, 50000.00, 45600)

# 7. Utilisez les méthodes pour déposer, retirer de l’argent du compte et vérifier le solde du compte.
my_account.check_balance()
my_account.deposit(10000)
my_account.check_balance()
my_account.remove(3000)
my_account.check_balance()
print(f"Mr {my_account.name}, de numéro de compte {my_account.account_number}, vous avez dans votre compte {my_account.account_balance} $")
#8. Testez le programme en créant plusieurs instances
# de la classe et en effectuant différentes transactions sur celles-ci.