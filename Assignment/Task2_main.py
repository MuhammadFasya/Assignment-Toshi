from Task2_konversi import konversi_suhu
from Task2_unitTest import test_konversi_suhu

if __name__ == "__main__":
    input_suhu = input("Masukkan suhu dalam derajat Celcius: ")
    hasil = konversi_suhu(input_suhu)
    print(hasil)
    
    # Menjalankan fungsi pengujian
    test_konversi_suhu()