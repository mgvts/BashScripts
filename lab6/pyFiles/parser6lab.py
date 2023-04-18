from pprint import pprint
d = {}

with open("2/11/11.1", "r") as f:
    for l in f:
        if l.count("data for N=") == 1:
            a = l.split()
            n = int(a[-1].split("=")[-1])
            d[n] = {"real": [],
                    "user": [],
                    "sys": [], }
        else:
            if len(l.split()) == 0:
                continue
            param, value = l.split()
            d[n][param].append(value)
# pprint(d)

for key in d.keys():
    realsum = 0
    for val in d[key]['real']:
        m, s = val.split("m")
        s = s.split("s")
        realsum += float(s[0]) + float(m)*60
    usersum = 0
    for val in d[key]['user']:
        m, s = val.split("m")
        s = s.split("s")
        usersum += float(s[0]) + float(m)*60
    syssum = 0
    for val in d[key]['sys']:
        m, s = val.split("m")
        s = s.split("s")
        syssum += float(s[0]) + float(m)*60
    res = [key, realsum/10, usersum/10, syssum/10]
    print(f"{res[0]} {res[1]} {res[2]} {res[3]}".replace(".", ",", 1000))

