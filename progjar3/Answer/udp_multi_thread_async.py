from library import download_gambar,get_url_list, send_image
import time
import datetime
import concurrent.futures

def kirim_semua():
    texec = dict()
    urls = get_url_list()
    z = 0
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    catat_awal = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k], k)
        print(f"downloading {urls[k]}")
        waktu = time.time()
        UDP_IP_ADDRESS = "192.168.122.220"
        UDP_IP_ADDRESS2 = "192.168.122.14"
        if z == 0:
            texec[k] = task.submit(send_image,UDP_IP_ADDRESS, 5050, f"{k}.jpg")
            print('~Server 1~')
            z = z + 1
        elif z == 1:
            print('~Server 2~')
            texec[k] = task.submit(send_image,UDP_IP_ADDRESS2, 5050, f"{k}.jpg")

    for k in urls:
        status_task[k]=texec[k].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Total Time Needed : {selesai} seconds {catat_awal} - {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)

if __name__=='__main__':
    kirim_semua()