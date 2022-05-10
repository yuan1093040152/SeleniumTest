import os
from .path import WEBPICTUREPATH,DELREPORTPATH


class Tool(object):
    def __init__(self):
        self.filelist = os.listdir(WEBPICTUREPATH)

    def error_picture(self):
        picture = []
        for item in self.filelist:
            if item.endswith('.jpg'):
                picture.append((item,))
        return picture

    def clear_picture(self):
        list(map(os.remove, map(lambda file: WEBPICTUREPATH + file, self.filelist)))







def delreport():
    file = os.listdir(DELREPORTPATH)
    report_dict = {}
    for i , f in enumerate(file):
        report_dict[i] = os.path.join(DELREPORTPATH,f)
        # print(report_dict)
    if len(report_dict) >= 13:
        for s in range(0,len(report_dict)-13):
            rpath = report_dict[s]
            os.remove(rpath)

    else:
        pass
