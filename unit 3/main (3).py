def linearSearchProduct(productList, targetProduct):
  indices = [] 
  
  for Index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(Index)
      
  return indices 

#example usage
products = ["shoes", "boot", "loafer", "shoes", "sandal",
"shoes"] 
target = "shoes"
result = linearSearchProduct(products, target)
print(result)