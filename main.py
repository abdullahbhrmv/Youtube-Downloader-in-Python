import pytube         # pip install pytube

link = input("YouTube link: ")     # link kiriting
print("Yuklanmoqda...")    # yuklanmoqda degan xabar beradi
yt = pytube.YouTube(link)   # linkni yuklash

yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download()    # video yuklash
print("Yuklab olingan fayl: ", link)  # yuklab olingan fayl ko'rsatib beradi