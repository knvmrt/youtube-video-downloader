from pytube import YouTube

link = input("Enter the video URL: ")

try:
    yt = YouTube(link)
    print(f"Downloading '{yt.title}'...")

    video = yt.streams.filter(progressive=True, 
    file_extension='mp4').order_by('resolution').desc().first()
    video.download()

    print("Video downloaded!")
except Exception as e:
    print(f"Error occurred!: {e}")
