
#* For Anidado y while
vocales= ["a", "b", "c"]

# tabla de multiplicar
for i in vocales:
  # print(i)


  for i in range(1, 11):
    print()
    for j in range(1, 11):
      resultado= i * j
      print(f"{i}x{j}= {resultado}")

i = 1
while i <=3:
    j = 1
    print("j en 1 while =", i)
  
    while j <=3:
        print("j en 2 while =", j)
        j += 1
    i += 1
    print("*********************")
