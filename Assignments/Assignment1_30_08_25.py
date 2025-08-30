# Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
product = ("Laptop", 50000, "Black" ,'Samsung', "Electronics")
print(product)

# Access and print the second element of the tuple product.
secondProperty = product[1]
print("Second property of the Product is - ", secondProperty)

# Slice and print the last two elements of the product tuple.
fewProperties = product[len(product)-2:]
print("Last two property of the Product is - ", fewProperties)


# Check whether "Electronics" is present in the product tuple and print a message.
# property = input("Enter the property you searching for - ")
property = "Electronics"
if property in product:
    print(property, " is a property of this product")
else:
    print(property, "is not a property of this product")

# Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
productPrices = (1000, 1500, 1200, 1100, 900)
print ("1000 is the price of ", productPrices.count(1000), "Products")

# Find and print the maximum and minimum price from the prices tuple.
pricelist = list(productPrices)
pricelist.sort()
print("Maximum price is - ", pricelist[-1])
print("Minimum price is - ", pricelist[0])

# Use a loop to print each item from the product tuple on a new line.
print("Properties of the product are - ")
for i in product:
    print(i,"\n")

# Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
latestProduct = list(product)
priceIndex = product.index(50000)
latestProduct[priceIndex] = 55000

newProduct = tuple(latestProduct)
print("Price is updated, now product - ", newProduct)

# Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
newProperty = ('In Stock',)
updatedProduct = newProduct + newProperty
print("After adding a new property", updatedProduct)

# Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
removeProperty = list(updatedProduct)
removeProperty.remove("Electronics")
updatedProduct = tuple(removeProperty)
print("After removing 'Electronics' property - ", updatedProduct)

# Unpack the tuple product into three variables and print each variable.
productType, price, *others = updatedProduct
print("Product type - ", productType, ", Price -", price, " and Other propeties - ", others)

# Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.
products = (("Laptop", 50000, "Black" ,'Samsung', "Electronics"), ("TV", 25000, "Black" ,'Llyod', "Electronics"), ("AC", 35000, "White" ,'LG', "Electronics"))
print("Name of the second product - ", products[1][0])