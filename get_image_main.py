import get_image
import os
import route_sarch


start_name = input("Start >>")
end_name = input("End >>")

url = route_sarch.makeNaviURL(start_name, end_name)
latlonlist = route_sarch.printNaviRes(url, timeout=10)
latlonlist_n = len(latlonlist)

for i in range(latlonlist_n):
    lat = float(latlonlist[i]["lat"])
    lng = float(latlonlist[i]["lng"])
    url_N = get_image.make_one_url(lat, lng, 0)
    #North
    url_S = get_image.make_one_url(lat, lng, 180)
    #South
    url_W = get_image.make_one_url(lat, lng, 270)
    #West
    url_E = get_image.make_one_url(lat, lng, 90)
    #East
    if (i == latlonlist_n):
        break
    try:
        new_dir = str(lat)+","+str(lng)
        try:
            os.mkdir(new_dir)
        except OSError:
            print('already exists')
        os.chdir(new_dir)
        image_N = get_image.download_image(url_N)
        get_image.save_image("North.png", image_N)
        image_S = get_image.download_image(url_S)
        get_image.save_image("South.png", image_S)
        image_W = get_image.download_image(url_W)
        get_image.save_image("West.png", image_W)
        image_E = get_image.download_image(url_E)
        get_image.save_image("East.png", image_E)
        os.chdir('../')
    except Exception as err:
        print(err)

