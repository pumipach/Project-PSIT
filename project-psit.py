import webbrowser
import folium
from nvd3 import multiBarChart

def a(name):
    chart = multiBarChart(width=250, height=150, x_axis_format=None)
    xdata = ['จำนวนทั้งหมด', 'ไม่สวมหมวก', 'ดื่มสุรา']
    ydata1 = [2, 0, 1]
    ydata2 = [3, 1, 0]

    chart.add_serie(name="ชาย", y=ydata1, x=xdata)
    chart.add_serie(name="หญิง", y=ydata2, x=xdata)
    chart.buildhtml()
    file_name = name + ".html"
    text_file = open(file_name, "w")
    text_file.write(chart.htmlcontent)
    print(chart.htmlcontent)
    text_file.close()
    return file_name


def bulid_map_51():
    """Buile html for thailand map."""
# [ละติจูด,ลองติดจูด] และการซูมลำดับ 5
map_osm = folium.Map(location=[15.0000, 100.0000], zoom_start=5)
map_osm.polygon_marker(location=[13.72842, 100.53122], popup="<iframe src='"+a("Output")+"'></iframe>",
                     fill_color='#FF0000', num_sides=3, radius=10, rotation=60)
map_osm.polygon_marker(location=[13.72842, 100.53122], popup="<iframe src='"+a("Output")+"'></iframe>",
                     fill_color='#FF0000', num_sides=3, radius=10, rotation=60)
map_osm.create_map(path='thailandmap_51.html')

year = input("ปีที่ต้องการดูตั้งแต่ปี 2551 - 2558(พ.ศ.) : ")
if "51" in year:
    bulid_map_51()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_51.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "52" in year:
    bulid_map_52()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_52.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "53" in year:
    bulid_map_53()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_53.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "54" in year:
    bulid_map_54()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_54.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "55" in year:
    bulid_map_55()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_55.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "56" in year:
    bulid_map_56()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_56.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "57" in year:
    bulid_map_57()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_57.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "58" in year:
    bulid_map_58()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_58.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
