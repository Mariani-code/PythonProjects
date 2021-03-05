basic_numbers = set("123456789")
product_list = []

for multiplicand in range(1,99):
    for multiplier in range(12,9999):
    
        product = multiplicand * multiplier
        combined = str(product) + str(multiplicand) +str(multiplier)


        if len(combined) > 9 :
            break


        if set(combined) == basic_numbers:
            product_list.append(product)


unique_product_list = set(product_list)

print(sum(unique_product_list))
