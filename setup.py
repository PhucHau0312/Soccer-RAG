import threading
try:
    from SoccerNet.Downloader import SoccerNetDownloader
except ImportError:
    print("SoccerNet package not found. Please install it by running 'pip install soccernet'")
    exit(1)

from src.database import process_json_files, fill_Augmented_Team, fill_Augmented_League


mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="data/SoccerNet")

def download_labels(file_name):
    try:
        mySoccerNetDownloader.downloadGames(files=[file_name], split=["train", "valid", "test"])
    except Exception as e:
        print(f"Error downloading {file_name}: {e}")


thread_v2 = threading.Thread(target=download_labels, args=("Labels-v2.json",))
thread_caption = threading.Thread(target=download_labels, args=("Labels-caption.json",))

thread_v2.start()
thread_caption.start()

thread_v2.join()
thread_caption.join()

print("All files downloaded successfully!")
print("Creating database..")

process_json_files("data/SoccerNet/")
fill_Augmented_Team("data/augmented_teams.csv")
fill_Augmented_League("data/augmented_leagues.csv")