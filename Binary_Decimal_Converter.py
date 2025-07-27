
class Binary_Decimal:

  def Decimal_value(self):
    for i in self.binary:
      if i not in '01':
        raise ValueError('Invalid Binary Digit')
    Blist = [int(digit) for digit in str(self.binary)]
    Blist.reverse()
    value = 0
    for i in range(len(Blist)):
      value += (Blist[i] * (2**i))
    return value

  def Binary_value(self):
    value = ''
    m = self.decimal
    while m > 0:
      (Divisor,Remainder) = (m//2, m%2)
      m = Divisor
      value += str(Remainder)
    return value[::-1]

  def __init__(self,n, input_type):
    if input_type == 'binary':
      self.binary = str(n)
      self.decimal = self.Decimal_value()
    elif input_type == 'decimal':
      self.decimal = int(n)
      self.binary = self.Binary_value()
    else:
      raise ValueError("input type must be either 'binary' or 'decimal'")
