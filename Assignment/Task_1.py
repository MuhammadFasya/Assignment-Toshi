#Cek valid ISBN
def validate_isbn(isbn):
    isbn = isbn.strip() # Hapus spasi di sekitar string ISBN jika pengguna tidak sengaja memberi space yang memunculkan error yang tidak terlalu penting
    if len(isbn) != 10: # Validasi panjang string wajib 10 
        return "Error: Invalid ISBN format."
    total = 0 # Inisialisasi variabel untuk total
    
    for i in range(10): # Iterasi melalui karakter ISBN
        char = isbn[i]
        # Jika karakter terakhir adalah 'X', ubah menjadi 10
        if i == 9 and char.upper() == 'X':
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return "Error: Invalid ISBN format." # Jika ditemukan karakter tidak valid
        total += (i + 1) * value # Tambahkan ke total dengan perhitungan sesuai rumus
    # Validasi berdasarkan modulo 11
    if total % 11 == 0:
        return "Valid ISBN."
    else:
        return "Invalid ISBN."

# Input
isbn_input = input("Masukkan ISBN-10: ")
result = validate_isbn(isbn_input)
print(result)
