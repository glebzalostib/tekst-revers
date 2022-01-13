a = input("Ievadit tekst: ")
def reversWords(a):
  sar1 = a.split()
  if len(sar1)>1:
    sar1.reverse()
    a=""
    for elements in sar1:
      a += elements
      print(a)
  else:
    a = "Parāk iss teikums"
    print(a)
  return a
reversWords(a)