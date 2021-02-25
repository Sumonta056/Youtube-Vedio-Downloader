import pytube
link = input("Enter the youtube link : ")
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
