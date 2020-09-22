import requests
import os
import imshime

imshime.api_create()

def make_one_url(lon, lat, heading):
    api_key = os.getenv('API_KEY')
    url_str = r"https://maps.googleapis.com/maps/api/streetview?size=500x300"
    url_str += r"&location=" + str(lon) + r"," + str(lat)
    url_str += r"&heading="+ str(heading) + "&fov=120"
    #以下のオプションをつけたほうが望ましいと考えられる
    url_str += r"&key=" + str(api_key)
    return url_str

# 画像をダウンロードする
# 指定したURLの画像データを返す関数
def download_image(url, timeout = 30):
    response = requests.get(url, allow_redirects=False, timeout=timeout)

    if response.status_code != 200:
        e = Exception("HTTP status: " + response.status_code)
        raise e

    content_type = response.headers["content-type"]
    if 'image' not in content_type:
        e = Exception("Content-Type: " + content_type)
        raise e

    return response.content

# 画像を保存する関数
def save_image(filename, image):
    with open(filename, "wb") as fout:
        fout.write(image)



