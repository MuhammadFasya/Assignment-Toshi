def main ():
  num = int(input("what's ur number ? "))
  print(f"Squared number of {num} is", squared (num))
  
def squared (n):
  return n*n

if __name__ == "__main__":
  main()