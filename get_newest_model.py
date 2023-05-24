import os
rootdir = './custom-models'


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def get_newest_model():
    _max = 0
    cdir = ""
    for subdir, dirs, _ in os.walk(rootdir):
        for _dir in dirs:
            if hasNumbers(_dir):
                time_stamp = int(_dir.split("-")[0])
                if max(_max, time_stamp) == time_stamp:
                    _max = max(_max, time_stamp)
                    cdir = os.path.join(subdir, _dir)
    if cdir != "":
        return cdir
    else:
        return 'en_core_web_lg'


print(get_newest_model())
