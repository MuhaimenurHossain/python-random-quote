import random
def amd():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 16
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  tie = random.randint(2, 4)
  if rnd == rnd2:
        rnd2 = (rnd + tie)//2
        print(str.rstrip(quotes[rnd]), str.rstrip(quotes[rnd2]))
  else:
    print(str.rstrip(quotes[rnd]) + ". " + str.rstrip(quotes[rnd2]) + ".")

if __name__== "__main__":
  amd()
