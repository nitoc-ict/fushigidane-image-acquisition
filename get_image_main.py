import get_image
import os

coord = input("Coordinate >>")
coord = coord.split(',')
lat = float(coord[0])
long = float(coord[1])


url_N = get_image.make_one_url(lat, long, 0)
#North
url_S = get_image.make_one_url(lat, long, 180)
#South
url_W = get_image.make_one_url(lat, long, 270)
#West
url_E = get_image.make_one_url(lat, long, 90)
#East

try:
    new_dir = str(lat)+","+str(long)
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
    print("done")
except Exception as err:
       print(err)