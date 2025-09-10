import subprocess
from pathlib import Path
from src.config import VIDEO_TEMPLATE, WAV2LIP_MODEL_PATH, OUTPUT_DIR

def run_wav2lip(audio_path: Path, output_path: Path):
    subprocess.run([
        "python", "Wav2Lip/inference.py",
        "--checkpoint_path", str(WAV2LIP_MODEL_PATH),
        "--face", str(VIDEO_TEMPLATE),
        "--audio", str(audio_path),
        "--outfile", str(output_path)
    ], check=True)