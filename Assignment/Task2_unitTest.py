# Unit test

from Task2_konversi import konversi_suhu

def test_konversi_suhu():
    # Menguji input valid
    assert konversi_suhu(0) == "Fahrenheit: 32.00\nKelvin: 273.15", "Test case 0 failed"
    assert konversi_suhu(100) == "Fahrenheit: 212.00\nKelvin: 373.15", "Test case 100 failed"
    assert konversi_suhu(-40) == "Fahrenheit: -40.00\nKelvin: 233.15", "Test case -40 failed"
    
    # Menguji input invalid
    assert konversi_suhu("abc") == "Error: Invalid input.", "Test case 'abc' failed"
    assert konversi_suhu("10.5.6") == "Error: Invalid input.", "Test case '10.5.6' failed"
    assert konversi_suhu("") == "Error: Invalid input.", "Test case '' failed"


    print("Semua test case berhasil!")