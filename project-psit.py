import webbrowser
import folium

def bulid_map_51():
    """Buile html for thailand map."""
# [ละติจูด,ลองติดจูด] และการซูมลำดับ 5
map_osm = folium.Map(location=[15.0000, 100.0000], zoom_start=5)
map_osm.polygon_marker(location=[13.72842, 100.53122], popup='โรงพยาบาลกรุงเทพคริสเตียน',
                     fill_color='#FF0000', num_sides=3, radius=10, rotation=60)
map_osm.create_map(path='thailandmap_51.html')

year = input("ปีที่ต้องการดู(พ.ศ.) : ")
if "51" in year:
    bulid_map_51()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_51.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")