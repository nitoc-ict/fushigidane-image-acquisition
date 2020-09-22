import get_image
import os
import route_sarch


start_name = input("start>>")
end_name = input("END")

url = route_sarch.makeNaviURL(start_name, end_name)
latlng = route_sarch.printNaviRes(url, timeout=10)
print(latlng)
latlng_n = len(latlng)
latlng_input = []
for n in range(latlng_n):
    lat = latlng[n]["lat"]
    lng = latlng[n]["lng"]
    latlng_input.append([lat, lng])
latlng_list = route_sarch.hokanlatlist(latlng_input, 300)
latlng_list_n = len(latlng_list)
for i in range(latlng_list_n):
    lat = float(latlng_list[i][0])
    lng = float(latlng_list[i][1])
    url_N = get_image.make_one_url(lat, lng, 0)
    #North
    url_S = get_image.make_one_url(lat, lng, 120)
    #South
    url_W = get_image.make_one_url(lat, lng, 240)
    #West
    if (i == latlng_n):
        break
    try:
        new_dir = str(lat)+","+str(lng)
        try:
            os.mkdir(new_dir)
        except OSError:
            print('already exists')
        os.chdir("syahin")
        os.chdir(new_dir)
        image_N = get_image.download_image(url_N)
        get_image.save_image("North.png", image_N)
        image_S = get_image.download_image(url_S)
        get_image.save_image("South.png", image_S)
        image_W = get_image.download_image(url_W)
        get_image.save_image("West.png", image_W)
        os.chdir('../')
    except Exception as err:
        print(err)

