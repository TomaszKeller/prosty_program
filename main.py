from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()


class Currency_converter:

    def pln_to_eu(self, pln_value):
        return int(pln_value) / 4.59

    def eu_to_pln(self, eu_value):
        return int(eu_value) * 4.59

    def pln_to_usd(self, pln_value):
        return int(pln_value) / 3.92

    def usd_to_pln(self, usd_value):
        return int(usd_value) * 3.92

    def menu(self):
        print("#"*10)
        print("Pick method:\n1.PLN/EU\n2.EU/PLN\n3.PLN/USD\n4.USD/PLN")
        print("#" * 10)

        choice = int(input("CHOICE ONE AND PRESS ENTER:"))
        amount = float(input("How much money?"))
        if choice == 1:
            result = self.pln_to_eu(amount)
        elif choice == 2:
            result = self.eu_to_pln(amount)
        elif choice == 3:
            result = self.pln_to_usd(amount)
        elif choice == 4:
            result = self.usd_to_pln(amount)
        else:
            print("Wybrałes złą wartość!")
            result = -1
        print(result)
        folder_selected = filedialog.askdirectory()
        print(folder_selected)

        with open(folder_selected+'/raport.txt','a') as f:
            f.write(str(round(result,2))+"\n")

if __name__ == "__main__":
    c = Currency_converter()
    c.menu()



c = Currency_converter()
c.menu()
