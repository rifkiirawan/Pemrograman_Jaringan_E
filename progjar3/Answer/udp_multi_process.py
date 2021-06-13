from library import download_gambar, get_url_list, kirim_gambar
import time
import datetime
from multiprocessing import Process

def kirim_semua():
    texec = dict()
    urls = get_url_list()
    z = 0
    catat_awal = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k],k)
        print(f"downloading {urls[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multiprocess
        UDP_IP_ADDRESS = "192.168.122.220"
        UDP_IP_ADDRESS2 = "192.168.122.14"
        if z == 0:
            texec[k] = Process(target=kirim_gambar, args=(UDP_IP_ADDRESS,5050,f"{k}.jpg"))
            print('~Server 1~')
            z = z+1
        elif z == 1:
            print('~Server 2~')
            texec[k] = Process(target=kirim_gambar, args=(UDP_IP_ADDRESS2,5050,f"{k}.jpg"))
        texec[k].start()
    #setelah menyelesaikan tugasnya, dikembalikan ke main process dengan join
    for k in urls:
        texec[k].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Total Time Needed : {selesai} seconds {catat_awal} - {catat_akhir}")
#fungsi download_gambar akan dijalankan secara multi process
if __name__=='__main__':
    kirim_semua()