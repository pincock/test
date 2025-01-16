from yt_dlp import YoutubeDL

def download_youtube_video(url, output_path='.'):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Video downloaded successfully and saved to {output_path}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    youtube_url = input("Please enter the YouTube URL: ")
    save_path = input("Please enter the path where you want to save the video (default is current directory): ") or '.'
    result = download_youtube_video(youtube_url, save_path)
    print(result)
