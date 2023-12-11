#modul produksi
#fungsi keuntungan penjualan
def profit(data):
    total_sales = data["jumlah_produk"] * data["harga_jual"]
    total_cost = data["jumlah_produk"] * data["biaya_produksi"]
    final_profit = total_sales - total_cost
    print(f'profit yang didapatkan adalah {final_profit}')


#fungsi harga pokok penjualan
def hpp(data):
    cogs = data["biaya_produksi"] + data["jumlah_produk"] - data["persediaan_sisa"]
            
    print(f'cogs yang didapatkan adalah {cogs}')
