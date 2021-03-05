LAB2
# Due Date: 02/13/2021, 11:59PM

"""
### Collaboration Statement:
LA - BRIAN

"""


# Check math on Self.Balance
# x.purchase(876) gave an error on the first line in the purchase method, find out why
class VendingMachine:
    '''
        >>> x=VendingMachine()
        >>> x.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.restock(215, 9)
        'Invalid item'
        >>> x.isStocked
        True
        >>> x.restock(156, 1)
        'Current item stock: 4'
        >>> x.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.purchase(156)
        'Please deposit $1.5'
        >>> x.purchase(156,2)
        'Please deposit $3.0'
        >>> x.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> x.deposit(3)
        'Balance: $3'
        >>> x.purchase(156,3)
        'Please deposit $1.5'
        >>> x.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> x.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.deposit(300)
        'Balance: $300'
        --->>> x.purchase(876)
        'Invalid item'
        >>> x.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> x.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> x.purchase(156,3)
        'Please deposit $4.5'
        >>> x.deposit(4.5)
        'Balance: $4.5'
        >>> x.purchase(156,3)
        'Item dispensed'
        >>> x.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> x.purchase(156)
        'Item out of stock'
        >>> x.deposit(6)
        'Balance: $6'
        >>> x.purchase(254,3)
        'Item dispensed'
        >>> x.deposit(9)
        'Balance: $9'
        >>> x.purchase(879,3)
        'Item dispensed'
        -------->>> x.isStocked
        False
        >>> x.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> x.purchase(156,2)
        'Machine out of stock'
        >>> y=VendingMachine()
        >>> x.setPrice(156, 2.5)
        >>> x.getStock
        {156: [2.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> y.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
    '''

    def __init__(self):
        self.balance = 0
        self.dictionary = {
            156: [1.5, 3],
            254: [2.0, 3],
            384: [2.5, 3],
            879: [3.0, 3]
        }

    def purchase(self, item, qty=1):

    #This method attempts to make a purchase and verifies the items, stock and balance to ensure validity

        if not self.dictionary:
            return 'Machine out of stock'
        if item not in self.dictionary:
            return ("Invalid Item")
        if self.dictionary[item][1] <= 0:
            return 'Item out of stock'
        if self.dictionary[item][1] < qty:
            total = self.dictionary[item][0] * qty
            return 'Current {} stock: {}, try again'.format(item, self.dictionary[item][1])
        chaching = self.dictionary[item][0]
        totalchaching = chaching * qty
        if self.balance < totalchaching:
            return 'Please deposit ${}'.format(totalchaching - self.balance)
        change = self.balance - totalchaching  # This will calculate your change
        self.dictionary[item][1] -= qty  # This updates the dictionary
        self.balance = 0  # This updates the balance
        if change > 0:
            return 'Item dispensed, Take your ${} back'.format(change)
        return 'Item dispensed'

    def deposit(self, amount):
        # This method deposits money into the vending machine, adding it to the current balance
        if not self.dictionary:
            print("Machine out of stock. Take your ${} back".format(amount))
        else:
            self.balance += amount
            return 'Balance: ${}'.format(amount)

    def restock(self, item, stock):
        # This method adds stock to the vending machine
        if item in self.dictionary:
            self.dictionary[item] = [self.dictionary[item][0], self.dictionary[item][1] + stock]
            return ('Current item stock: ' + str(self.dictionary[item][1]))
        else:
            return 'Invalid item'

    
    @property
    def isStocked(self):
        for item in self.dictionary:
            if self.dictionary[item][1] > 0:
                return True
            else:
                return False

   
    @property
    def getStock(self):
        # This method gets the current stock status of the machine
        return self.dictionary

    def setPrice(self, item, new_price):
        # This method changes the price of an item for an instance of VendingMachine
        if item in self.dictionary:
            self.dictionary[item] = new_price
        if item in self.dictionary != item:
            return ("Invalid Item")


## Section 2
class Complex:
    '''
        >>> a=Complex(5.2,-6)
        >>> b=Complex(2,14)
        >>> a+b
        (7.2, 8i)
        >>> a-b
        (3.2, -20i)
        >>> a*b
        (94.4, 60.8i)
        >>> a/b
        (-0.368, -0.424i)
        >>> b*5
        (10, 70i)
        >>> 5*b
        (10, 70i)
        >>> 5+a
        (10.2, -6i)
        >>> a+5
        (10.2, -6i)
        >>> 5-b
        (3, -14i)
        >>> b-5
        (-3, 14i)
        >>> print(a)
        5.2-6i
        >>> print(b)
        2+14i
        >>> b
        (2, 14i)
        >>> isinstance(a+b, Complex)
        True
        >>> a.conjugate
        (5.2, 6i)
        >>> b.conjugate
        (2, -14i)
        >>> isinstance(b.conjugate, Complex)
        True
        >>> b==Complex(2,14)
        True
        >>> a==b
        False
        >>> a==9.5
        False
    '''

    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    
    @property
    def conjugate(self):
        return Complex(self.real, -(self.imag))

    
    def __str__(self):
        if self.real != 0:
            if self.imag != 0:
                return '({}, {}i)'.format(self.real, self.imag)
        else:
            return None

    def __repr__(self):
        return '({}, {}i)'.format(self.real, self.imag)

    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __radd__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __rsub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __rmul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        return Complex((self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2),
                       (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2))

    def __rtruediv__(self, other):
        return Complex((self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2),
                       (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2))
