from pytube import YouTube
print("Welcome to PyTDL V1.0")
print("------------------------")
try:
    link = input("Paste a youtube video link:")
    yt = YouTube(link)
    path = input("Enter a path for the video to download in:")
    dl = yt.streams.get_by_resolution(int(input("What resoultion you want to download?:")))
    dl.download(output_path=path)
except Exception:
    print("Sorry an error occured")