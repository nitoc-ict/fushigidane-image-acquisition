import json
import urllib.request
import imshime
import os
from math import sin, cos, acos, radians

imshime.api_create()

def makeNaviURL(startName, endName):
    api_key = os.getenv('API_KEY_ROUTE')
    #URLに日本語が入るのはいまいちなので修正
    startName = urllib.parse.quote_plus(startName, encoding='utf-8')
    endName = urllib.parse.quote_plus(endName, encoding='utf-8')
    result_str = r"https://maps.googleapis.com/maps/api/directions/json?key="+str(api_key)+"&origin=$"+startName+"&destination=$"+endName
    print(result_str)
    return result_str

#APIに実際にアクセスして、結果をprint
def printNaviRes(url, timeout = 10):
    try:
        with urllib.request.urlopen(url) as url_opend:
            html = url_opend.read().decode('utf-8')
            json_content = json.loads(html)
            json_content_legs = json_content["routes"][0]["legs"]

            latlng = []
            i = 0
            try:
                while ((json_content_legs[0]["steps"][i]["end_location"] is not None) and (json_content_legs[0]["steps"][i]["start_location"] is not None)):
                    latlng.append(json_content_legs[0]["steps"][i]["end_location"])
                    latlng.append(json_content_legs[0]["steps"][i]["start_location"])
                    i += 1
            except IndexError:
                print("")
        print(latlng)
        return (latlng)
    except:
        print("ERR!")
        import traceback
        traceback.print_exc()

earth_rad = 6378.137

def latlng_to_xyz(lat, lng):
    rlat, rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)

def dist_on_sphere(pos0, pos1, radius=earth_rad):
    xyz0, xyz1 = latlng_to_xyz(*pos0), latlng_to_xyz(*pos1)
    return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radius

# 距離に応じて、分割を実施し、中間点を補完する
#中間点の補完処理によって、latlnglistを補完する
def hokanlatlist(input_latlnglist, bunkatu_kyori):

    latlnglist = []
    befor_latlng = input_latlnglist[0]
    for input_latlng in input_latlnglist[1:]:
        #m単位の２点距離を算出
        distance = dist_on_sphere(befor_latlng, input_latlng) * 1000

        #距離に応じて、何分割するか決める
        bunkatu_suu = int(distance/bunkatu_kyori)+1

        befor_lat = befor_latlng[0]
        befor_lng = befor_latlng[1]
        now_lat = input_latlng[0]
        now_lng = input_latlng[1]

        #分割数分繰り返して、リストを作る
        #終点は、+1しているために、この処理で含んで登録される。
        for num in range(bunkatu_suu):
            lat = befor_lat + ((num+1) * (now_lat - befor_lat)) / bunkatu_suu
            lon = befor_lng + ((num+1) * (now_lng - befor_lng)) / bunkatu_suu
            latlnglist.append([lat, lon])

        #次の処理に行く前に出発点を移動する
        befor_latlng = input_latlng
    print(latlnglist)
    return latlnglist

