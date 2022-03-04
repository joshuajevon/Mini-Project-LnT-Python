print("Selamat datang di toko jaya baru")
print("List Menu:")
print("1. Nasi Goreng = Rp20.000")
print("2. Bakso = Rp15.000")
print("3. Soto Ayam = Rp10.000")
print("4. Nasi Padang = Rp25.000")
print("5. Teh = Rp5.000")

pilihan = int(input("Pilih Menu:"))
if pilihan == 1:
    pilihan1 = int(input("Jumlah porsi nasi goreng:"))
    totalHarga = pilihan1 * 20000
    print("Total Harga:Rp",totalHarga)
    uang = int(input("Uang yang dibayarkan:Rp"))
    kembalian = uang - totalHarga
    print("Uang kembalian:Rp",kembalian)
elif pilihan == 2:
    pilihan1 = int(input("Jumlah porsi bakso:"))
    totalHarga = pilihan1 * 15000
    print("Total Harga:Rp",totalHarga)
    uang = int(input("Uang yang dibayarkan:Rp"))
    kembalian = uang - totalHarga
    print("Uang kembalian:Rp",kembalian)
elif pilihan == 3:
    pilihan1 = int(input("Jumlah porsi soto ayam:"))
    totalHarga = pilihan1 * 10000
    print("Total Harga:Rp",totalHarga)
    uang = int(input("Uang yang dibayarkan:Rp"))
    kembalian = uang - totalHarga
    print("Uang kembalian:Rp",kembalian)
elif pilihan == 4:
    pilihan1 = int(input("Jumlah porsi nasi padang:"))
    totalHarga = pilihan1 * 25000
    print("Total Harga:Rp",totalHarga)
    uang = int(input("Uang yang dibayarkan:Rp"))
    kembalian = uang - totalHarga
    print("Uang kembalian:Rp",kembalian)
elif pilihan == 5:
    pilihan1 = int(input("Jumlah teh:"))
    totalHarga = pilihan1 * 5000
    print("Total Harga:Rp",totalHarga)
    uang = int(input("Uang yang dibayarkan:Rp"))
    kembalian = uang - totalHarga
    print("Uang kembalian:Rp",kembalian)
else:
    print("Mohon Maaf Menu Tidak Ada")