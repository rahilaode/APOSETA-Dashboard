from get_data import *

def data_point():
    jumlah_kunjungan_2020 = get_data('jumlah_kunjungan_2020')
    jumlah_kunjungan_2021 = get_data('jumlah_kunjungan_2021')
    #print(jumlah_kunjungan_2020)
    
    #Total kunjungan
    total_2020 = jumlah_kunjungan_2020.total_kunjungan.sum()
    total_2021 = jumlah_kunjungan_2021.total_kunjungan.sum()
    #print(total_2020, total_2021)
    
    #Rata - Rata Kunjungan tiap puskesmas   
    rata_2020 = int(jumlah_kunjungan_2020["total_kunjungan"].mean())
    rata_2021 = int(jumlah_kunjungan_2021["total_kunjungan"].mean())
    
    ## Jenis Kunjungan total
    rawat_jalan_2020 = int(jumlah_kunjungan_2020["rawat_jalan_lp"].sum())
    rawat_inap_2020 = int(jumlah_kunjungan_2020["rawat_inap_lp"].sum())
    gangguan_jiwa_2020 = int(jumlah_kunjungan_2020["gangguan_jiwa_lp"].sum())
    rawat_jalan_2021 = int(jumlah_kunjungan_2021["rawat_jalan_lp"].sum()) 
    rawat_inap_2021 = int(jumlah_kunjungan_2021["rawat_inap_lp"].sum())
    gangguan_jiwa_2021 = int(jumlah_kunjungan_2021["gangguan_jiwa_lp"].sum())
    
    return total_2020, total_2021, rata_2020, rata_2021, rawat_jalan_2020, rawat_inap_2020, gangguan_jiwa_2020, rawat_jalan_2021, rawat_inap_2021, gangguan_jiwa_2021

total_kunjungan_2020, total_kunjungan_2021, rata_2020, rata_2021, rawat_jalan_2020, rawat_inap_2020, gangguan_jiwa_2020, rawat_jalan_2021, rawat_inap_2021, gangguan_jiwa_2021 = data_point()
# tahun = [['2020', int(total_kunjungan_2020)], ['2021', int(total_kunjungan_2021)]]
# df_1 = pd.DataFrame(tahun, columns=['Tahun', 'Total'])
# print(df_1.dtypes)

#data_point()

    