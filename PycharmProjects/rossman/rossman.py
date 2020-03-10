import requests
import json
from bs4 import BeautifulSoup


for shop_id in range(970, 2528):
    try:
        print('shop_id=', shop_id)
        url_link = 'https://www.rossmann.pl/drogerie/shop,id,4,' + str(shop_id)
        page = requests.get(url_link)

        soup = BeautifulSoup(page.content, 'html.parser')

        json_tag = soup.find('script', id="__NEXT_DATA__")

        json_data = json_tag.text
        # print("json_data=", json.dumps(json_data, indent=4, sort_keys=True))
        parsed_json = (json.loads(json_data))
        props = parsed_json.get("props")
        # print("props=", props)

        page_props = props.get("pageProps")
        # print("page_props=", page_props)

        initialReduxState = page_props.get("initialReduxState")
        shops = initialReduxState.get("shops")
        # print("shops=", shops)
        shops_details = shops.get("details")
        # print("shops_details=", shops_details)
        shops_data = shops_details.get("data")
        print("shops_data=", json.dumps(shops_data, indent=4, sort_keys=True))
        if shops_data is None:
            continue
        city = shops_data.get("City")
        if city is None:
            continue
        address = shops_data.get("Street")
        if address is None:
            continue
        PostCode = shops_data.get("PostCode")
        print("address=%s, city=%s, PostCodee=%s" % (city, address, PostCode))
        print("address=" + address)
        print("PostCode=" + PostCode)

        latitude = str(shops_data.get("Latitude"))
        print("latitude=", latitude)

        longitude = str(shops_data.get("Longitude"))
        print("longitude=", longitude)

        hoursMonday = str(shops_data.get("MondayOpenFrom")) + " - " + str(shops_data.get("MondayOpenTo"))
        print("hoursMonday=" + hoursMonday)

        hoursTuesday = str(shops_data.get("MondayOpenFrom")) + " - " + str(shops_data.get("TuesdayOpenTo"))
        print(("hoursTuesday=" + hoursTuesday))

        hoursWednesday = str(shops_data.get("WednesdayOpenFrom")) + " - " + str(shops_data.get("WednesdayOpenTo"))
        print("hoursWednesday=" + hoursWednesday)

        hoursThursday = str(shops_data.get("ThursdayOpenFrom")) + " - " + str(shops_data.get("ThursdayOpenTo"))
        print("hoursThursday=" + hoursThursday)

        hoursFriday = str(shops_data.get("FridayOpenFrom")) + " - " + str(shops_data.get("FridayOpenTo"))
        print("hoursFriday=" + hoursFriday)

        hoursSaturday = str(shops_data.get("SaturdayOpenFrom")) + " - " + str(shops_data.get("SaturdayOpenTo"))
        print("hoursSaturday=" + hoursSaturday)

        hoursSunday = str(shops_data.get("SundayOpenFrom")) + " - " + str(shops_data.get("SundayOpenTo"))
        print("hoursSunday=" + hoursSunday)

        # shopDataString = "#" + shop_id + "#" + address + "#" + city + "#" + PostCode + "#" + latitude + "#" + longitude + "#" + hoursMonday + "#" + hoursTuesday + "#" + hoursWednesday + "#" + hoursThursday + "#" + hoursFriday + "#" + hoursSaturday + "#" + hoursSunday

        shopDataString = "#".join((address, city, PostCode, latitude, longitude, hoursMonday, hoursTuesday, hoursWednesday, hoursThursday, hoursFriday, hoursSaturday, hoursSunday))
        print("shopDataString:\n" + shopDataString)
        # result_file.write(shopDataString + "\n")
    except AttributeError as e:
        print(e)
        # shopDataString = shop_id + '#' + 'NO_DATA'


# else:
#     print("shop_id=" + str(shop_id) + " doesn't exist")

# file_with_shops_list.close()
# result_file.close()