from currency import Currency


class Money:
    value = Currency()

    def __init__(self, amount=0, currency_type="EUR"):
        self.currency_type = currency_type.upper()
        self.amount = amount

    def __str__(self):
        return f"You have {self.amount} {self.currency_type}"

    def __add__(self, other):
        default_rate = 1
        if isinstance(other, Money):
            if self.currency_type != other.currency_type:
                default_rate = self._convert(other.currency_type)
            other = other.amount
        return self.__class__(self.amount + other * default_rate,
                              self.currency_type)

    def __radd__(self, other):
        default_rate = 1
        if isinstance(other, Money):
            if self.currency_type != other.currency_type:
                default_rate = self._convert()
        return self.__class__(self.amount + other * default_rate,
                              self.currency_type)

    def __mul__(self, other):
        if isinstance(other, Money):
            if other.currency_type != self.currency_type:
                other.amount = self._convert(other.currency_type)
            return self.__class__(self.amount * other.amount)

        return self.__class__(self.amount * other, self.currency_type)

    def __rmul__(self, other):
        return self.__mul__(other)

    def _convert(self, first):
        rate = self.value.get_rates(first, self.currency_type)
        return rate
