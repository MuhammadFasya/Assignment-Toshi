def main ():
  str = input("What's ur name? ")
  print(hello())
  print(hello(str))
  
  
def hello(to="World"):
  return f"Hello, {to}"

if __name__ == "__main__":
  main()