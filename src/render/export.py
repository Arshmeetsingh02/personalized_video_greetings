import subprocess
from pathlib import Path

def merge_video_audio(video_path: Path, audio_path: Path, output_path: Path):
    subprocess.run([
        "ffmpeg", "-y", "-i", str(video_path), "-i", str(audio_path),
        "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental",
        str(output_path)
    ], check=True)