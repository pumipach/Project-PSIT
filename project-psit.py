import webbrowser
import folium
from nvd3 import multiBarChart

year = input("ปีที่ต้องการดูตั้งแต่ปี 2551 - 2558(พ.ศ.) : ")
if "51" in year:
    import year_51
    year_51.bulid_map_51()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_51.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "52" in year:
    import year_52
    year_52.bulid_map_52()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_52.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "53" in year:
    import year_53
    year_53.bulid_map_53()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_53.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "54" in year:
    import year_54
    year_54.bulid_map_54()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_54.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "55" in year:
    import year_55
    year_55.bulid_map_55()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_55.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "56" in year:
    import year_56
    year_56.bulid_map_56()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_56.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "57" in year:
    import year_57
    year_57.bulid_map_57()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_57.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
elif "58" in year:
    import year_58
    year_58.bulid_map_58()
    # Open the page in a new browser tab
    webbrowser.open_new_tab('thailandmap_58.html')
    print("สีแดง คือ ผู้บาดเจ็บเพศหญิง")
    print("สีแดง คือ ผู้บาดเจ็บเพศชาย")
