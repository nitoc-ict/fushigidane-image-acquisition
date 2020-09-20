import json
import urllib.request
import imshime
import os

imshime.api_create()

def makeNaviURL(startName, endName):
    api_key = os.getenv('API_KEY_ROUTE')
    #URLに日本語が入るのはいまいちなので修正
    startName = urllib.parse.quote_plus(startName, encoding='utf-8')
    endName = urllib.parse.quote_plus(endName, encoding='utf-8')
    result_str = r"https://maps.googleapis.com/maps/api/directions/json?key="+str(api_key)+"&origin=$"+startName+"&destination=$"+endName
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
        return (latlng)
    except:
        print("ERR!")
        import traceback
        traceback.print_exc()

