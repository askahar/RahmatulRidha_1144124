Representasi pengetahuan adalah menyampaikan atau menyajikan ulang tentang sebuah pengetahuan yang diperoleh oleh ke dalam suatu skema atau diagram, sehingga kita dapat mengetahui relasi antara satu pengetahuan dan pengetahuan lainnya. Representasi pengetahuan merupakan menyampaikan kembali suatu pengetahuan. 

Representasi ini terbagi menjadi 5 kelompok :
* Representasi Logika
* Jaringan Semantik
* Frame
* Script atau Naskah
* Aturan Produksi

Tahu = Paham = Belajar
> Paham itu sudah asti tahu, tapi tahu itu belum tentu paham. Apabila kita tahu dan kemudian kita ingin paham dengan apa yang harus kita lakukan itu di sebut proses berfikir dan belajar agar kita bisa memahami apa yang kita tahu. Rasa ragu itu adalah suatu hasil dari proses berfikir.

PRAKTEK

Roadmap jalur terpendek, jalur dari Rahma Home sampai dengan MTsN Salido.

input :

graph = {
             'Rahma Home': ['Painan Timur'],
             'Painan Timur': ['Rawang'],
             'Rawang': ['Pagaruyung I'],
             'Pagaruyung I': ['Salido'],
             'Salido': ['MTsN Salido'],
             'MTsN Salido': ['Salido'],
        }

def mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
            if not graph.has_key(jalanawal):
                    return None
        jalurpendek = None
        for node in graph[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(graph, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Jalan Raya Dari Rahma Homes Sampai MTsN Salido")
print("(Rahma Home, Painan Timur, Rawang, Pagaruyung I)")
print("(Salido, MTsN Salido)")
print("\n")
jalanawal = raw_input("Masukan jalanawal : ")
jalantujuan = raw_input("Masukan jalantujuan : ")
hasil = mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil
