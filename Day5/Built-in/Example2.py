#Decimal fixed point

from decimal import Decimal, ROUND_HALF_UP
print(Decimal('10.25') + Decimal('2.34'))
#print(10.25)
#print(Decimal('10.25') + 2.34)

#Rounding decimals
print(Decimal('2.345').quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))

#Decimal - used for precise decimal value
#ROUND_HALF_UP - rounding rule

#.quantize - Round the number to 2 decimal places(0.01)
#ROUND_HALF_UP - 2.345 = 2.35

