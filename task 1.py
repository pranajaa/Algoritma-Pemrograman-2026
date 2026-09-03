print("menghitung nilai rata-rata")

nilaiTugas = float(input("masukkan nilaiTugas: "))
nilaiUTS = float(input("masukkan nilaiUTS: "))
nilaiUAS = float(input("masukkan nilaiUAS: "))

totalnilai = nilaiTugas + nilaiUTS + nilaiUAS

print("jadi total nilai adalah:", str(totalnilai))
banyaknilai = int(input("masukkan banyak nilai: "))
ratarata = totalnilai/banyaknilai
print("jadi rata ratanya adalah", str(ratarata))
