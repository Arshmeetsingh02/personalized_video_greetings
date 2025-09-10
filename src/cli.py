import csv
from pathlib import Path
from src.config import OUTPUT_DIR
from src.tts.coqui_client import generate_tts
from src.lip_sync.wav2lip_cpu import run_wav2lip

OUTPUT_DIR.mkdir(exist_ok=True)

with open("data/variables.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sentence = f"Namaste {row['name']}, your {row['room_type']} suite is confirmed from {row['from_date']} to {row['to_date']} for {row['guest_count']} guests."
        audio_file = OUTPUT_DIR / f"{row['name']}.wav"
        video_file = OUTPUT_DIR / f"{row['name']}.mp4"
        generate_tts(sentence, row['language'], audio_file)
        run_wav2lip(audio_file, video_file)