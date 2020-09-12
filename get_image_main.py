import get_image

C_1 = float(input("Coordinate1 >>"))
#緯度
C_2 = float(input("Coordinate2 >>"))
#経度

url_N = get_image.make_one_url(C_1, C_2, 0)
#North
url_S = get_image.make_one_url(C_1, C_2, 180)
#South
url_W = get_image.make_one_url(C_1, C_2, 270)
#West
url_E = get_image.make_one_url(C_1, C_2, 90)
#East

try:
    image_N = get_image.download_image(url_N)
    get_image.save_image("North.png", image_N)
    image_S = get_image.download_image(url_S)
    get_image.save_image("South.png", image_S)
    image_W = get_image.download_image(url_W)
    get_image.save_image("West.png", image_W)
    image_E = get_image.download_image(url_E)
    get_image.save_image("East.png", image_E)
    print("done")
except Exception as err:
       print(err)