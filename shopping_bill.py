def calculateElectronicsGST(a, b):
    amount = a + b
    return amount + (amount * 18 / 100)

def calculateFashionGST(c, d):
    amount = c + d 
    return amount + (amount * 13 / 100)
 
def calculateFoodGST(e):
    return e + (e * 7 / 100)

def totalBill(a,b,c,d,e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    return electronics + fashion + food

def calculateDiscounteBill(a,b,c,d,e):
    total = totalBill(a,b,c,d,e)
    discount = total * 20/100
    return total - discount

a,b,c,d,e = 100, 100, 100, 100, 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a,b,c,d,e)
discount = total * 20/100
final_amount = calculateDiscounteBill(a,b,c,d,e)

print(f"Electronics after GST:{electronics:.2f}")
print(f"Fashion after GST:{fashion:.2f}")
print(f"Food after GST:{food:.2f}")
print(f"Total after GST:{total:.2f}")
print(f"Discount:{discount:.2f}")
print(f"Final payable amount:{final_amount:.2f}")