import pytube

def download_video():
    try:
        video_url = input("Enter the video URL: ")
        yt = pytube.YouTube(video_url)
        available_streams = yt.streams

        print("Available video resolutions:")
        for i, stream in enumerate(available_streams):
            print(f"{i + 1}. {stream.resolution}")

        choice = int(input("Enter the number corresponding to the desired resolution: "))
        selected_stream = available_streams[choice - 1]

        print("Downloading video...")
        selected_stream.download()

        print("Video downloaded successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

download_video()
