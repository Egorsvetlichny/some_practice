import decimal

context = decimal.getcontext()
context.rounding = decimal.ROUND_DOWN

number1 = decimal.Decimal(0.3)
number2 = decimal.Decimal('0.3')
number3 = number2.quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_FLOOR)

if __name__ == '__main__':
    print(context, context.rounding, sep='\n', end='\n\n')
    print(number1, number2, number3, sep='\n', end='\n\n')
