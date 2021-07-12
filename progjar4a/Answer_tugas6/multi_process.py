from file_client_cli import remote_get
import time
import datetime
from multiprocessing import Process

def downloads():
    texec = dict()
    catat_awal = datetime.datetime.now()
    namafile = 'pokijan.jpg'
    for k in range(100):
        print(f"download iteration - {k}")
        waktu = time.time()
        texec[k] = Process(target=remote_get, args=(namafile,))
        texec[k].start()
    for k in range(100):
        texec[k].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"TIME NEEDED {selesai} seconds {catat_awal} - {catat_akhir}")

if __name__ == '__main__':
    downloads()