from functools import total_ordering


def bonAppetit(bill, k, b):
    total_ordering = sum(bill) - bill[k]
    if total_ordering/2-b==0:
        print("Bon Appetit")
    else:
        print(abs(total_ordering//2-b))

if __name__ == "__main__":
    bill= [3,10,2,9]
    k = 1
    b = 12
    bonAppetit(bill,k,b)