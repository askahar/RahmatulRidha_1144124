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
