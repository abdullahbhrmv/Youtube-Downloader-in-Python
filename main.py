import pytube

link = input("YouTube link: ")
print("Yuklanmoqda...")
yt = pytube.YouTube(link)

yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download()
print("Yuklab olingan fayl: ", link)