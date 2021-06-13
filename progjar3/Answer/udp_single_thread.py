from library import download_gambar, get_url_list, send_image
import time
import datetime

def send_all():
    urls = get_url_list()
    z = 0

    catat = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k], k)
        print(f"mendownload {urls[k]}")
        waktu_proses = download_gambar(urls[k])
        print(f"completed {waktu_proses} detik")
        UDP_IP_ADDRESS = "192.168.122.220"
        UDP_IP_ADDRESS2 = "192.168.122.14"
        if z == 0:
            send_image(UDP_IP_ADDRESS, 5050, f"{k}.jpg")
            print('~Server 1~')
            z = z + 1
        elif z == 1:
            print('~Server 2~')
            send_image(UDP_IP_ADDRESS2, 5050, f"{k}.jpg")
    selesai = datetime.datetime.now() - catat
    print(f"Total Time Needed : {selesai} seconds")


#fungsi download_gambar akan dijalankan secara berurutan

if __name__=='__main__':
    send_all()