from currency import Currency
from money import Money

a = Currency()

x = Money(10, "BYN")
y = Money(11)
z = Money(2, "EUR")

print(z + 3.11 * x + y * 0.8)

lst = [x, y, Money(12.01, "JPY")]
s = sum(lst)
print(s)
