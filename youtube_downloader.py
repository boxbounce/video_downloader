
# @boxbounce 2022.1.27
# https://github.com/boxbounce/video_downloader
import sys
import os
import subprocess

# 添加当前路径至模块搜索的目录列表中
path_exe = os.path.dirname(os.path.realpath(sys.argv[0]))
print(path_exe)
subprocess.check_call(
    'dir', shell=True, cwd=path_exe)
max_v = input(
    '\n输入下载视频的最大分辨率，推荐输入 1080 (表示下载的视频最大码率为1080p,若视频分辨率最高不超过1080p，则下载低于1080p的码率中最高的码率视频),\n请输入后 单击Enter键确认:\n')

try:
    max_v = int(max_v)
except Exception as e:
    print(f"请输入正整数！例如 720 1080 1440（2k） 2160（4k） \n输入无效:>>> {max_v} <<<")
    print(f'本次默认执行最大分辨率 1080p\n')
    max_v = 1080

print('\nCtrl+V链接到本程序中进行下载')


def youtube_cmd(url_v):
    global max_v
    # 此方法使用多进程多线程概率性无法调用youtube-dl  os.system同样如此
    # 如果要用多进程同时下载多个视频，自己再开一个窗口即可
    try:
        print(f"当前执行最大分辨率 {max_v} 尝试使用16个线程下载")
        subprocess.check_call(
            f'youtube-dl -f "bestvideo[height<=?{max_v}]+bestaudio/best" {url_v} --external-downloader aria2c --external-downloader-args "-x 16 -k 1M --file-allocation=none"', shell=True, cwd=path_exe)
    except Exception as e:
        print(e)
        return

while True:
    print('\n>>>进行新的下载！')
    url_v = input(
        '使用Ctrl+V粘贴需要下载的视频链接 再单击Enter键确认 \n请输入视频网址链接:')
    if not 'http' in url_v:
        print('>>>视频链接有误，请查证！<<<')
        continue
    youtube_cmd(url_v)
