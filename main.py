import sys
import requests
import json
import pandas as pd
import numpy as np
import csv
import time
import matplotlib.pyplot as plt
import re
import ast
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from pyecharts.faker import Faker
import pyecharts.options as opts
from pyecharts.charts import Bar, Line,Geo
from scipy.integrate import odeint
import random
import scipy
from pyecharts.charts import Map

filepath = sys.path[0]  #get file path

# 获取部分国家数据
# Get some country data
def crawlsomecountry():
    first_url = "https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryMerge"
    res = requests.post(first_url)
    data = json.loads(res.content.decode())
    # print(data)
    data_i = pd.DataFrame(data['data']['FAutoCountryMerge'])
    # print(data_i)
    b = []
    c = []
    # a["date"] = data_i[0]["list"]
    for i in data_i["美国"]["list"]:
        b.append(i["date"])
    #print(b)
    d = {}
    d["date"] = b
    c = list(data_i.keys())
    # print(c)
    a = pd.DataFrame(d)
    # print(a)
    e = [0] * a.shape[0]
    # count = 0
    # print(a["date"][count])
    for i in range(len(c)):
        count = 0
        for j in data_i[c[i]]["list"]:
            # print(j["date"])
            while (j["date"] != a["date"][count]):
                count += 1
            if (j["date"] == a["date"][count]):
                e[count] = j["confirm"]
                # print(j["confirm"])
            count += 1
            # print(e)
            if (count == len(e)):
                break

        # print(e)
        a[c[i]] = e
        # print(a)
        e = [0] * a.shape[0]
    b = pd.DataFrame(a["date"])
    b["俄罗斯"] = a["俄罗斯"]
    b["美国"] = a["美国"]
    b["英国"] = a["英国"]
    b["法国"] = a["法国"]
    # print(b)

    b.to_csv('foreign.csv')
    # print(c)
    # for i in range(len(c)):

    # print(a)


# 获取各大洲数据
# Get data on all continents
def crawleverycontinent():
    q_url = "https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoContinentStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd"
    res = requests.post(q_url)
    data = json.loads(res.content.decode())
    # print(data)
    data_i = pd.DataFrame(data["data"]["FAutoContinentStatis"])
    a = pd.DataFrame()
    yazhou = []
    qita = []
    beimeizhou = []
    dayangzhou = []
    nanmeizhou = []
    ouzhou = []
    feizhou = []
    data_i = data_i.drop([0, 1])
    # print(data_i)
    a["date"] = data_i["date"]
    # print(data_i.head())
    for i in data_i["statis"]:
        yazhou.append(i["亚洲"])
        qita.append(i["其他"])
        beimeizhou.append(i["北美洲"])
        nanmeizhou.append(i["南美洲"])
        ouzhou.append(i["欧洲"])
        feizhou.append(i["非洲"])
    a["亚洲"] = yazhou
    a["北美洲"] = beimeizhou
    a["南美洲"] = nanmeizhou
    a["非洲"] = feizhou
    a["欧洲"] = ouzhou
    a["其他"] = qita
    # print(a.dtypes)
    # print(a)
    a.to_csv("各洲的数据.csv")
    # a.plot()
    # print(a)
    # print(data_i)


# 获取中国每日数据
# Get daily data from China
def CrawlChinadata():
    q_url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,cityStatis,nowConfirmStatis,provinceCompare"
    res = requests.post(q_url)
    data = json.loads(res.content.decode())
    # print(data)
    data_i = pd.DataFrame(data["data"]["chinaDayAddList"])
    # print(data_i)
    df = pd.DataFrame(data_i["date"])
    df["confirm"] = data_i["confirm"]
    df["death"] = data_i["dead"]
    df["suspect"] = data_i["suspect"]
    df["heal"] = data_i["heal"]
    data_i = pd.DataFrame(data["data"]["chinaDayList"])
    df["totalconfirm"] = data_i["confirm"]
    df["totoalheal"] = data_i["heal"]
    df.to_csv("chinadailyconfirm.csv")
    # print(df)
    # print(data_i)


# 处理各洲数据、绘图（所有）
# Process data and draw pictures of all continents (all)
def dealcontinentdata():

    #print(filepath)    #just to test the file path
    #df = pd.read_csv("/Users/caizhen/Desktop/疫情分析项目/各洲的数据.csv")

    df = pd.read_csv(filepath + "/各洲的数据.csv")
    data_i = pd.DataFrame(df["date"])

    data_i.date = "2020/" + data_i.date
    # print(data_i)
    data_i.date = pd.to_datetime(data_i.date)
    # print(data_i)
    # print(df["date"])
    # print(data_i)

    df["date"] = data_i.date
    df.set_index("date", inplace=True)
    # print(df.head())
    # print(data_i["date"])
    di = [41.67, 12.26, 5.79, 4.34, 7.4]
    dict = {"Asia": df["亚洲"] / di[0], "Afica": df["非洲"] / di[1], "NorthAmerica": df["北美洲"] / di[2],
            "SouthAmerica": df["南美洲"] / di[3], "Europe": df["欧洲"] / di[4]}
    line = pd.DataFrame(dict, index=data_i["date"])
    line.plot()
    plt.title("Continent confirm(Global)")
    plt.show()
    # print(data_i)


# 处理各洲数据、绘图（三月份）
# Process data and draw pictures of all continents (March)
def dealcontinentdatathree():

    #df = pd.read_csv("/Users/caizhen/Desktop/疫情分析项目/各洲的数据.csv")
    df = pd.read_csv(filepath + "/各洲的数据.csv")
    data_i = pd.DataFrame(df["date"])

    data_i.date = "2020/" + data_i.date
    # print(data_i)
    data_i.date = pd.to_datetime(data_i.date)
    # print(data_i)
    # print(df["date"])
    df = df.drop(labels=range(7, len(df)))
    # print(data_i)

    df["date"] = data_i.date
    df.set_index("date", inplace=True)
    # print(df.head())
    # print(data_i["date"])
    di = [41.67, 12.26, 5.79, 4.34, 7.4]
    dict = {"Asia": df["亚洲"] / di[0], "Afica": df["非洲"] / di[1], "NorthAmerica": df["北美洲"] / di[2],
            "SouthAmerica": df["南美洲"] / di[3], "Europe": df["欧洲"] / di[4]}
    line = pd.DataFrame(dict, index=data_i["date"])
    line.plot()
    plt.title("Continentconfirm(March)")
    plt.show()
    # print(data_i)


# 联合国五大国绘图（所有）
# Drawings of the five major nations of the United Nations (all)
def dealwithfivecountry():
    df1 = pd.read_csv("foreign.csv", dtype={"date": str})
    df2 = pd.read_csv("chinadailyconfirm.csv", dtype={"date": str})
    df = pd.DataFrame({"date": ["1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27"]})
    # print(df)
    a = [0] * 8
    df["俄罗斯"] = a
    df["美国"] = a
    df["英国"] = a
    df["法国"] = a
    # print(df)
    # df["confirm"] = a
    # print(df)
    df = df.append(df1, ignore_index=True)
    del df['Unnamed: 0']
    # print(df)
    # df.drop(labels=len(df) - 9,inplace=True)
    d = pd.DataFrame(df2["totalconfirm"])
    df["中国"] = d
    # print(df)
    df.to_csv("fivecountry.csv")
    data_time = pd.DataFrame(df["date"])
    data_time.date[:347] = "2020." + data_time.date[:347]
    data_time.date[347:] = "2021." + data_time.date[347:]
    # print(data_time)
    data_time.date = pd.to_datetime(data_time.date)
    df["date"] = data_time.date
    # print(df.head())
    df.set_index("date", inplace=True)
    di = [14.00, 3.30, 1.46, 0.66, 0.67]
    dict = {"China": df["中国"], "US": df["美国"], "Russia": df["俄罗斯"], "England": df["英国"],
            "France": df["法国"]}
    line = pd.DataFrame(dict, index=data_time["date"])
    line.plot()
    plt.title("Permanent member differences(Global)")
    plt.show()
    #print(df["美国"])
    # print(data_time["date"])
    # print(dict)
    # print(data_time["date"])
    # data_time.set_index("date",inplace=True)


# 联合国五大国绘图（三月）
# Drawings of the five major nations of the United Nations (March)
def dealwithfivecountrythree():
    df1 = pd.read_csv("foreign.csv", dtype={"date": str})
    df2 = pd.read_csv("chinadailyconfirm.csv", dtype={"date": str})
    df = pd.DataFrame({"date": ["1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27"]})
    # print(df)
    a = [0] * 8
    df["俄罗斯"] = a
    df["美国"] = a
    df["英国"] = a
    df["法国"] = a
    # print(df)
    # df["confirm"] = a
    # print(df)
    df = df.append(df1, ignore_index=True)
    del df['Unnamed: 0']
    # print(df)
    # df.drop(labels=len(df) - 9,inplace=True)
    d = pd.DataFrame(df2["totalconfirm"])
    df["中国"] = d
    china = [0]
    russia = [0]
    us = [0]
    en = [0]
    france = [0]
    for i in range(1,len(df)):
        china.append(df["中国"][i] - df["中国"][i - 1])
        russia.append(df["俄罗斯"][i] - df["俄罗斯"][i - 1])
        us.append(df["美国"][i] - df["美国"][i - 1])
        en.append(df["英国"][i] - df["英国"][i - 1])
        france.append(df["法国"][i] - df["法国"][i - 1])
    df["俄罗斯k"] = russia
    df["中国k"] = china
    df["美国k"] = us
    df["英国k"] = en
    df["法国k"] = france
    #print(first)
    # print(df)
    df.to_csv("fivecountry.csv")
    # print(type(df["date"]))
    data_time = pd.DataFrame(df["date"])
    data_time.date[:347] = "2020." + data_time.date[:347]
    data_time.date[347:] = "2021." + data_time.date[347:]
    # print(data_time)
    data_time.date = pd.to_datetime(data_time.date)
    df["date"] = data_time.date
    # print(df.head())
    df.set_index("date", inplace=True)
    df = df[41:72]
    di = [14.00, 3.30, 1.46, 0.66, 0.67]
    dict = {"China": df["中国k"], "US": df["美国k"], "Russia": df["俄罗斯k"], "England": df["英国k"],
            "France": df["法国k"]}
    line = pd.DataFrame(dict)
    line.plot()
    plt.title("Permanent member differences(March)")
    plt.show()
    # print(data_time["date"])
    # print(dict)
    # print(data_time["date"])
    # data_time.set_index("date",inplace=True)


# 获取日本数据
# Get Japanese data
def crawljapan():
    url = "https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=1&stage=publish&callback=jsonp_1606311406202_98489"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15"}
    res = requests.get(url, headers=headers)
    # print(res.text)
    result = re.findall("\{\"name\":\"日本\".*\"新加坡\"", res.text)
    # print(result)
    # print(result)
    r = re.findall(".*\"治愈\"", str(result))
    # print(r)
    # print(r)
    a = str(r).replace("[\'[\\\'{\"name\":\"日本\",\"trend\":", "")
    a = a.replace(",{\"name\":\"治愈\"\']", "")
    a = a.replace("\"list\":[{\"name\":\"确诊\",", "")
    # print(rs)
    # print(a)
    # print(type(a))
    a = ast.literal_eval(a)
    b = pd.DataFrame(a)
    # print(b)
    b.to_csv("japandata.csv")

# 获取印度数据
# Get Indian data
def crawlindian():
    url = "https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=1&stage=publish&callback=jsonp_1606311406202_98489"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15"}
    res = requests.get(url, headers=headers)
    result = re.findall("\{\"name\":\"印度\".*\"菲律宾\"", res.text)
    r = re.findall(".*\"治愈\"", str(result))
    #print(r)
    #print(r)
    a = str(r).replace("[\'[\\\'{\"name\":\"印度\",\"trend\":", "")
    a = a.replace(",{\"name\":\"治愈\"\']", "")
    a = a.replace("\"list\":[{\"name\":\"确诊\",", "")
    # print(rs)
    # print(a)
    # print(type(a))
    a = ast.literal_eval(a)
    b = pd.DataFrame(a)
    # print(b)
    b.to_csv("indiandata.csv")

# 亚洲地区处理
# Process data in Asia
def dealwithAsian():
    japan = pd.read_csv("japandata.csv")
    indian = pd.read_csv("indiandata.csv")
    cn = pd.read_csv("chinadailyconfirm.csv", dtype={"date": str})
    jpa = [0] * (cn.shape[0] - japan.shape[0])
    jpa.extend(japan["data"])
    # print(a)
    ina = [0] * (cn.shape[0] - indian.shape[0])
    ina.extend(indian["data"])
    df = pd.DataFrame({"date": cn["date"], "china": cn["totalconfirm"], "japan": jpa, "india": ina})
    # print(df)
    data_time = pd.DataFrame(df["date"])
    data_time.date[:347] = "2020." + data_time.date[:347]
    data_time.date[347:] = "2021." + data_time.date[347:]
    # print(data_time)
    data_time.date = pd.to_datetime(data_time.date)
    df["date"] = data_time.date
    # print(df.head())
    df.set_index("date", inplace=True)
    df.to_csv("temp.csv")
    #people = [14, 1.26, 13.24]
    #print(df["china"])
    #print(df["japan"])
    dict = {"china confirm": df["china"], "japan confirm": df["japan"], "indian confirm": df["india"]}
    print(dict)
    line = pd.DataFrame(dict, index=data_time["date"])
    line.plot()
    plt.title("Asian confirm")
    plt.show()

# 排名
# Rank
def crawl5():
    q_url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
    res = requests.post(q_url)
    data = json.loads(res.content.decode())
    data_i = pd.DataFrame(data['data'])
    data_i.to_csv("data.csv")
    return data_i

# 世界当日数据
# World daily Data
def run4():
    df = pd.read_csv("chinadailyconfirm.csv")
    data5 = crawl5()
    country_d = list(data5.name)
    confirm_d = list(data5.confirmAdd)
    #print(len(country_d))

    #print(len(country_d))

    #print(len(country_d))
    #print(len(confirm_d))
    #print(country_d[len(country_d) - 1])
    #print(confirm_d[len(country_d) - 1])
    #print(country_d)
    #print(confirm_d)
    # print(data5)
    #print(confirm_draw)
    country_draw = []
    confirm_draw = []
    for i in range(len(country_d)):
        country_draw.append(new_dict[country_d[i]])
        confirm_draw.append(confirm_d[i])
    z = [list(z) for z in zip(country_draw, confirm_draw)]
    #country_d.append("中国")
    #confirm_d.append(df["confirm"][df.shape[0] - 1])
    #chinadata = df["confirm"][df.shape[0] - 1]
    #print(chinadata)
    chinadata = int(df["confirm"][df.shape[0] - 1])
    z.append(["China",chinadata])
    #print(z)
    #print([list(z) for z in zip(country_draw, confirm_draw)])
    #print( [list(z) for z in zip(Faker.country, Faker.values())])
    #print(confirm_draw)
    #print(country_draw)
    #print(country_draw)
    #print(confirm_draw)
    #print(country_draw)
    #print(confirm_draw)

    c = (
        Map()
            .add("世界当日数据",z , "world",)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-世界地图当日数据"),
            visualmap_opts=opts.VisualMapOpts(max_=100000),
        )
            .render("./运行结果/world_daily_confirm.html")
    )





namemap = {
    "China": "中国",
    "Maldives": "马尔代夫",
    "The Federation of Saint Kitts and Nevis": "圣基茨和尼维斯",
    "Marshall Islands": "马绍尔群岛",
    "Republic of the Congo": "刚果（布）",
    "Principat d'Andorra": "安道尔",
    "Repubblica di San Marino": "圣马力诺",
    "Fürstentum Liechtenstein": "列支敦士登公国",
    "Diamond Princess": "钻石号邮轮",
    "La Principauté de Monaco": "摩纳哥",
    "The Commonwealth of Dominica": "多米尼克",
    "Martinique": "马提尼克岛",
    "Vatican": "梵蒂冈",
    "Somalia": "索马里",
    "Liechtenstein": "列支敦士登",
    "Morocco": "摩洛哥",
    "W. Sahara": "西撒哈拉",
    "Serbia": "塞尔维亚",
    "Afghanistan": "阿富汗",
    "Angola": "安哥拉",
    "Albania": "阿尔巴尼亚",
    "Andorra": "安道尔共和国",
    "United Arab Emirates": "阿联酋",
    "Argentina": "阿根廷",
    "Armenia": "亚美尼亚",
    "Australia": "澳大利亚",
    "Austria": "奥地利",
    "Azerbaijan": "阿塞拜疆",
    "Burundi": "布隆迪",
    "Belgium": "比利时",
    "Benin": "贝宁",
    "Burkina Faso": "布基纳法索",
    "Bangladesh": "孟加拉",
    "Bulgaria": "保加利亚",
    "Bahrain": "巴林",
    "Bahamas": "巴哈马",
    "Bosnia and Herz.": "波黑",
    "Belarus": "白俄罗斯",
    "Belize": "伯利兹",
    "Bermuda": "百慕大",
    "Bolivia": "玻利维亚",
    "Brazil": "巴西",
    "Barbados": "巴巴多斯",
    "Brunei": "文莱",
    "Bhutan": "不丹",
    "Botswana": "博茨瓦纳",
    "Central African Rep.": "中非共和国",
    "Canada": "加拿大",
    "Switzerland": "瑞士",
    "Chile": "智利",
    "China": "中国",
    "Côte d'Ivoire": "科特迪瓦",
    "Cameroon": "喀麦隆",
    "Dem. Rep. Congo": "刚果（金）",
    "Congo": "刚果",
    "Colombia": "哥伦比亚",
    "Cape Verde": "佛得角",
    "Costa Rica": "哥斯达黎加",
    "Cuba": "古巴",
    "N. Cyprus": "北塞浦路斯",
    "Cyprus": "塞浦路斯",
    "Czech Rep.": "捷克",
    "Germany": "德国",
    "Djibouti": "吉布提",
    "Denmark": "丹麦",
    "Dominican Rep.": "多米尼加",
    "Algeria": "阿尔及利亚",
    "Ecuador": "厄瓜多尔",
    "Egypt": "埃及",
    "Eritrea": "厄立特里亚",
    "Spain": "西班牙",
    "Estonia": "爱沙尼亚",
    "Ethiopia": "埃塞俄比亚",
    "Finland": "芬兰",
    "Fiji": "斐济",
    "France": "法国",
    "Gabon": "加蓬",
    "United Kingdom": "英国",
    "Georgia": "格鲁吉亚",
    "Ghana": "加纳",
    "Guinea": "几内亚",
    "Gambia": "冈比亚",
    "Guinea-Bissau": "几内亚比绍",
    "Eq. Guinea": "赤道几内亚",
    "Greece": "希腊",
    "Grenada": "格林纳达",
    "Greenland": "格陵兰",
    "Guatemala": "危地马拉",
    "Guam": "关岛",
    "Guyana": "圭亚那",
    "Honduras": "洪都拉斯",
    "Croatia": "克罗地亚",
    "Haiti": "海地",
    "Hungary": "匈牙利",
    "Indonesia": "印度尼西亚",
    "India": "印度",
    "Br. Indian Ocean Ter.": "英属印度洋领土",
    "Ireland": "爱尔兰",
    "Iran": "伊朗",
    "Iraq": "伊拉克",
    "Iceland": "冰岛",
    "Israel": "以色列",
    "Italy": "意大利",
    "Jamaica": "牙买加",
    "Jordan": "约旦",
    "Japan": "日本本土",
    "Siachen Glacier": "锡亚琴冰川",
    "Kazakhstan": "哈萨克斯坦",
    "Kenya": "肯尼亚",
    "Kyrgyzstan": "吉尔吉斯斯坦",
    "Cambodia": "柬埔寨",
    "Korea": "韩国",
    "Kuwait": "科威特",
    "Lao PDR": "老挝",
    "Lebanon": "黎巴嫩",
    "Liberia": "利比里亚",
    "Libya": "利比亚",
    "Sri Lanka": "斯里兰卡",
    "Lesotho": "莱索托",
    "Lithuania": "立陶宛",
    "Luxembourg": "卢森堡",
    "Latvia": "拉脱维亚",
    "Moldova": "摩尔多瓦",
    "Madagascar": "马达加斯加",
    "Mexico": "墨西哥",
    "Macedonia": "北马其顿",
    "Mali": "马里",
    "Malta": "马耳他",
    "Myanmar": "缅甸",
    "Montenegro": "黑山",
    "Mongolia": "蒙古",
    "Mozambique": "莫桑比克",
    "Mauritania": "毛里塔尼亚",
    "Mauritius": "毛里求斯",
    "Malawi": "马拉维",
    "Malaysia": "马来西亚",
    "Namibia": "纳米比亚",
    "New Caledonia": "新喀里多尼亚",
    "Niger": "尼日尔",
    "Nigeria": "尼日利亚",
    "Nicaragua": "尼加拉瓜",
    "Netherlands": "荷兰",
    "Norway": "挪威",
    "Nepal": "尼泊尔",
    "New Zealand": "新西兰",
    "Oman": "阿曼",
    "Pakistan": "巴基斯坦",
    "Panama": "巴拿马",
    "Peru": "秘鲁",
    "Philippines": "菲律宾",
    "Papua New Guinea": "巴布亚新几内亚",
    "Poland": "波兰",
    "Puerto Rico": "波多黎各",
    "Dem. Rep. Korea": "朝鲜",
    "Portugal": "葡萄牙",
    "Paraguay": "巴拉圭",
    "Palestine": "巴勒斯坦",
    "Qatar": "卡塔尔",
    "Romania": "罗马尼亚",
    "Russia": "俄罗斯",
    "Rwanda": "卢旺达",
    "Saudi Arabia": "沙特阿拉伯",
    "Sudan": "苏丹",
    "S. Sudan": "南苏丹",
    "Senegal": "塞内加尔",
    "Singapore": "新加坡",
    "Solomon Is.": "所罗门群岛",
    "Sierra Leone": "塞拉利昂",
    "El Salvador": "萨尔瓦多",
    "Suriname": "苏里南",
    "Slovakia": "斯洛伐克",
    "Slovenia": "斯洛文尼亚",
    "Sweden": "瑞典",
    "Swaziland": "斯威士兰",
    "Seychelles": "塞舌尔",
    "Syria": "叙利亚",
    "Chad": "乍得",
    "Togo": "多哥",
    "Thailand": "泰国",
    "Tajikistan": "塔吉克斯坦",
    "Turkmenistan": "土库曼斯坦",
    "Timor-Leste": "东帝汶",
    "Tonga": "汤加",
    "Trinidad and Tobago": "特立尼达和多巴哥",
    "Tunisia": "突尼斯",
    "Turkey": "土耳其",
    "Tanzania": "坦桑尼亚",
    "Uganda": "乌干达",
    "Ukraine": "乌克兰",
    "Uruguay": "乌拉圭",
    "United States": "美国",
    "Uzbekistan": "乌兹别克斯坦",
    "Venezuela": "委内瑞拉",
    "Vietnam": "越南",
    "Vanuatu": "瓦努阿图",
    "Yemen": "也门",
    "South Africa": "南非",
    "Zambia": "赞比亚",
    "Zimbabwe": "津巴布韦",
    "Aland": "奥兰群岛",
    "American Samoa": "美属萨摩亚",
    "Fr. S. Antarctic Lands": "南极洲",
    "Antigua and Barb.": "安提瓜和巴布达",
    "Comoros": "科摩罗",
    "Curaçao": "库拉索岛",
    "Cayman Is.": "开曼群岛",
    "Dominica": "多米尼加",
    "Falkland Is.": "马尔维纳斯群岛（福克兰）",
    "Faeroe Is.": "法罗群岛",
    "Micronesia": "密克罗尼西亚",
    "Heard I. and McDonald Is.": "赫德岛和麦克唐纳群岛",
    "Isle of Man": "曼岛",
    "Jersey": "泽西岛",
    "Kiribati": "基里巴斯",
    "Saint Lucia": "圣卢西亚",
    "N. Mariana Is.": "北马里亚纳群岛",
    "Montserrat": "蒙特塞拉特",
    "Niue": "纽埃",
    "Palau": "帕劳",
    "Fr. Polynesia": "法属波利尼西亚",
    "S. Geo. and S. Sandw. Is.": "南乔治亚岛和南桑威奇群岛",
    "Saint Helena": "圣赫勒拿",
    "St. Pierre and Miquelon": "圣皮埃尔和密克隆群岛",
    "São Tomé and Principe": "圣多美和普林西比民主共和国",
    "Turks and Caicos Is.": "特克斯和凯科斯群岛",
    "St. Vin. and Gren.": "圣文森特和格林纳丁斯",
    "U.S. Virgin Is.": "美属维尔京群岛",
    "Samoa": "萨摩亚",
    "ms Zaandam": "尚丹号"
}
new_dict = {v: k for k, v in namemap.items()}


# 死亡率全球(除中国)
# Mortality worldwide (except China)
def dealwithdeadrate():
    data = pd.read_csv("data.csv")
    data["deadrate"] = data["dead"] / data["confirm"]
    data.sort_values("deadrate",inplace=True)
    #print(data["dead"])
    # print(df.head())
    #print(deadrate2)
    #data["deadrate"] =
    #print(data)
    c = (
        Line()
            .add_xaxis(data["name"])
            .add_yaxis("治愈率", data["deadrate"], is_smooth=True)
            .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="死亡率"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
            datazoom_opts=opts.DataZoomOpts(),

        )
            .render("./运行结果/deadrate.html")
    )



# 死亡率五常
# Mortality rate(five country)
def dealwithdeadratefivecountry():
    data = pd.read_csv("data.csv")
    # print(data["dead"])
    # print(df.head())
    # print(d)

    data["deadrate"] = data["dead"] / data["confirm"]

    name = ["美国", "英国", "法国", "俄罗斯"]
    data.set_index("name", inplace=True)
    # print(data)
    e = []
    for i in name:
        e.append(data.loc[i]["deadrate"])
    # print(e)
    name.append("中国")
    # print(res.text)
    # print(data)
    # print(e)
    q_url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery35109761260732639327_1607523486527&_=1607523486528"
    res = requests.post(q_url)
    # print(res.text)
    res = res.text.replace("\\", "")
    # print(res)
    s1 = re.findall("confirm\":(\d+)", res)
    # print(s1)
    s2 = re.findall("dead\":(\d+)", res)
    # print(s2)
    e.append(int(s2[0]) / int(s1[0]))
    #print(e)
    d = pd.DataFrame({"name": name, "deadrate": e})
    d.sort_values("deadrate", ascending=False)

    c = (
        Line()
            .add_xaxis(name)
            .add_yaxis("死亡率", d["deadrate"], is_smooth=True)
            .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )

            .set_global_opts(
            title_opts=opts.TitleOpts(title="死亡率(五大国)"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
            datazoom_opts=opts.DataZoomOpts(),

        )
            .render("./运行结果/deadrate(fivecountry).html")
    )


# 治愈率降序全球（除中国）
# Cure rate in descending order worldwide (except China)
def dealwithhealrate():
    data = pd.read_csv("data.csv")
    # print(data["dead"])
    # print(df.head())
    # print(d)
    data["healrate"] = data["heal"] / data["confirm"]

    data.sort_values("healrate", ascending=False, inplace=True)
    rate = data["healrate"]
    name = list(data["name"])
    # print(d)
    # print(data.head())
    # print(n)
    c = (
        Line()
            .add_xaxis(name)
            .add_yaxis("治愈率", rate, is_smooth=True)
            .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="治愈率"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
            datazoom_opts=opts.DataZoomOpts(),

        )
            .render("./运行结果/healrate.html")
    )



# 治愈率降序五常
# Cure rate in descending order(five country)
def dealwithhealratefivecountry():
    data = pd.read_csv("data.csv")
    # print(data["dead"])
    # print(df.head())
    # print(d)

    data["healrate"] = data["heal"] / data["confirm"]

    name = ["美国", "英国", "法国", "俄罗斯"]
    data.set_index("name", inplace=True)
    # print(data)
    e = []
    for i in name:
        e.append(data.loc[i]["healrate"])
    # print(e)
    name.append("中国")
    # print(res.text)
    # print(data)
    q_url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery35109761260732639327_1607523486527&_=1607523486528"
    res = requests.post(q_url)
    # print(res.text)
    res = res.text.replace("\\", "")
    # print(res)
    s1 = re.findall("confirm\":(\d+)", res)
    # print(s1)
    s2 = re.findall("heal\":(\d+)", res)
    # print(s2)
    e.append(int(s2[0]) / int(s1[0]))
    # print(e)
    # res = res.replace("jQuery35109761260732639327_1607523486527(","")
    # print(res)
    # res = res.replace(")","")
    # print(res)
    # e.append(res["data"]["chinaTotal"]["heal"])
    # print(e)
    # print(res)
    # print(res["data"])
    # print(res["data"])
    d = pd.DataFrame({"name": name, "healrate": e})
    d.sort_values("healrate", ascending=False)
    # print(d)
    # print(data.head())
    # print(n)
    c = (
        Line()
            .add_xaxis(name)
            .add_yaxis("治愈率", d["healrate"], is_smooth=True)
            .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="治愈率(五大国)"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
            datazoom_opts=opts.DataZoomOpts(),

        )
            .render("./运行结果/healrate(fivecountry).html")
    )

# 中国城市每日新增
# Chinese cities daily data
def chinacity():
    q_url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,cityStatis,nowConfirmStatis,provinceCompare"
    res = requests.post(q_url)
    data = json.loads(res.content.decode())
    # print(data)
    data_i = pd.DataFrame(data["data"]["provinceCompare"])
    # print(data_i)
    cityname = [column for column in data_i]
    citynumber = list(data_i.loc[["confirmAdd"][0]])
    #print(citynumber)
    '''
    c = (
        Map()
            .add("中国城市每日新增", [list(z) for z in zip(cityname, citynumber)], "china")
            .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
            .render("./运行结果/map_base.html")
    )
    
    '''
    c = (
        Geo()
            .add_schema(maptype="china")
            .add(
            "geo",
            [list(z) for z in zip(cityname, citynumber)],
            type_=ChartType.HEATMAP,
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=10),
            title_opts=opts.TitleOpts(title="China_daily_confirm"),
        )
        .render("./运行结果/China_daily.html")
    )


# 浙江省城市关系
# Zhejiang province daily data
def chinacities():
    data = pd.read_csv("浙江省城市.csv")
    data_time = pd.DataFrame(data["date"])
    # print(data_time)
    data_time.date = pd.to_datetime(data_time.date)
    data["date"] = data_time.date
    # print(df.head())
    data.set_index("date", inplace=True)
    #df = df[41:72]
    #di = [14.00, 3.30, 1.46, 0.66, 0.67]
    dict = {"wenzhou":data["温州"],"taizhou":data["台州"],"hangzhou":data["杭州"],"ningbo":data["宁波"],"shaoxing":data["绍兴"],"jinhua":data["金华"],"zhoushan":data["舟山"],"lishui":data["丽水"],"quzhou":data["衢州"],"huzhuo":data["湖州"]}
    line = pd.DataFrame(dict)
    line.plot()
    plt.title("zhengjiangsheng")
    plt.show()





if __name__ == "__main__":
    #the following several functions are to get data
    #crawlsomecountry()
    #crawleverycontinent()
    #crawljapan()       #停止服务
    #crawlindian()      #停止服务
    #CrawlChinadata()


    #the following several functions are to deal with data
    dealcontinentdata()
    dealwithfivecountry()
    dealcontinentdatathree()
    dealwithfivecountrythree()
    #dealwithAsian()    #DO NOT USE! DUE TO LOSE OF JAPAN DATA
    run4()
    # dealwithdeadrate()
    dealwithhealrate()

    dealwithhealratefivecountry()
    dealwithdeadratefivecountry()

    chinacity()
    #chinacities()
