import re
import requests
import pandas as pd
import time
from tqdm import trange


# 视频页面点击“浏览器地址栏小锁-Cookie-bilibili.com-Cookie-SESSDATA”进行获取
SESSDATA = "2749a90a%2C1683961224%2C17ee4%2Ab1"
# 视频页面“按F12-Console-输入document.cookie”进行获取
cookie = "buvid3=015E7199-0DA9-E2B4-3E04-4A6056A569BE38236infoc; _uuid=1EFE110510-108DE-E58C-9FF5-D1D376E1AA3F42420infoc; CURRENT_BLACKGAP=0; blackside_state=0; buvid4=2D21BA65-658D-540E-3860-17DF6DDE700A46386-022072915-m5+JSBQVvF6BzdZMFwhpzQ==; buvid_fp_plain=undefined; DedeUserID=445319303; DedeUserID__ckMd5=d9980f95f98f81ff; buvid_fp=0cf08363df9891bb3e68e95d0890009a; i-wanna-go-back=-1; b_ut=5; hit-dyn-v2=1; fingerprint3=ec60e078bb086553e5735c0ffa8a3ecf; nostalgia_conf=-1; b_nut=100; fingerprint=a27adf4a626062e5c59b6eacc8e85a08; bsource=search_baidu; CURRENT_FNVAL=4048; b_lsid=D274DCCE_18474F067B9; SESSDATA=2749a90a,1683961224,17ee4*b1; bili_jct=d57cd1714312b1cdfc8abaf66321abe6; sid=5icwohgx; bp_video_offset_445319303=728208290721300600; innersign=1; PVID=2"
cookie += f";SESSDATA={SESSDATA}"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "cookie": cookie,
}


def get_info(vid):
    url = f"https://api.bilibili.com/x/web-interface/view/detail?bvid={vid}"
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    data = response.json()
    info = {}
    info["标题"] = data["data"]["View"]["title"]
    info["总弹幕数"] = data["data"]["View"]["stat"]["danmaku"]
    info["视频数量"] = data["data"]["View"]["videos"]
    info["cid"] = [dic["cid"] for dic in data["data"]["View"]["pages"]]
    if info["视频数量"] > 1:
        info["子标题"] = [dic["part"] for dic in data["data"]["View"]["pages"]]
    for k, v in info.items():
        print(k + ":", v)
    return info


def get_danmu(info, start, end):
    date_list = [i for i in pd.date_range(start, end).strftime("%Y-%m-%d")]
    all_dms = []
    for i, cid in enumerate(info["cid"]):
        dms = []
        for j in trange(len(date_list)):
            url = f"https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={cid}&date={date_list[j]}"
            response = requests.get(url, headers=headers)
            response.encoding = "utf-8"
            data = re.findall(r"[:](.*?)[@]", response.text)
            dms += [dm[1:] for dm in data]
            time.sleep(3)
        if info["视频数量"] > 1:
            print("cid:", cid, "弹幕数:", len(dms), "子标题:", info["子标题"][i])
        all_dms += dms
    print(f"共获取弹幕{len(all_dms)}条！")
    return all_dms


if __name__ == "__main__":
    vid = 'BV1H64y1e7rn'   # bili的话,手机端打开可看见BV开头的字符串
    info = get_info(vid)
    start = input("输入弹幕开始时间（年-月-日）: ")
    end = input("输入弹幕结束时间（年-月-日）: ")
    danmu = get_danmu(info, start, end)
    with open("danmu.txt", "w", encoding="utf-8") as fout:
        for dm in danmu:
            fout.write(dm + "\n")