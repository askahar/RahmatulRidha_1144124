import sys
print("Langkah Benar 5-1-4-2-3-1-5\n")
print (" 1.Petani kembali\n 2.Petani dan Ayam kembali\n 3.Petani dan Gabah menyebrang\n 4.Petani dan Harimau menyebrang\n5.Petani dan Ayam menyebrang")
def game():
		langkah1 = raw_input("Langkah ke-1 : ")
		if langkah1 == '5'		: langkah2 = raw_input("Langkah ke-2 : ")
		else 			: print("Failed")
		if langkah2 == '1' 		: langkah3 = raw_input("Langkah ke-3 : ")
		else 			: print("Failed")
		if langkah3 == '4' 		: langkah4 = raw_input("Langkah ke-4 : ")
		else 			: print("Failed")
		if langkah4 == '2' 		: langkah5 = raw_input("Langkah ke-5 : ")
		else 			: print("Failed")
		if langkah5 == '3' 		: langkah6 = raw_input("Langkah ke-6 : ")
		else 			: print("Failed")
		if langkah6 == '1' 		: langkah7 = raw_input("Langkah ke-7 : ")
		else 			: print("Failed")
		if langkah7 == '5' 		: langkah8 = raw_input("GOOD JOB!")
game()