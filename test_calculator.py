from calculator import squared

def  main():
    test_negative()
    test_positive()
    test_neutral()

def test_positive():
    assert squared(2) == 4 # assert itu menegaskan, logic nya mengecek bener atau tidak suatu kondisi
    assert squared(5) == 25
    
def test_negative():
    assert squared(-2) == 4
    assert squared(-5) == 25
    
def test_neutral():
    assert squared(0) == 0
    
if __name__ == "__main__":
    main()