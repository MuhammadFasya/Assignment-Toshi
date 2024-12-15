'''
Menyaring Nama Kucing
'''
def filter_cat_names():
    n = int(input("Enter the number of cat names: "))  
    names = [input().strip() for _ in range(n)]
    valid_names = list(filter(lambda name: len(name) > 4 and name[0].lower() in 'aeiou', names))
    print("\n")
    print("\n".join(valid_names))

if __name__ == "__main__":
    filter_cat_names()
