from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = DATA_DIR / "outputs"

VIDEO_TEMPLATE = ASSETS_DIR / "scene2_blank.mp4"
TTS_MODEL_EN = "tts_models/en/ljspeech/tacotron2-DDC"
TTS_MODEL_HI = "tts_models/multilingual/multi-dataset/your_tts"
WAV2LIP_MODEL_PATH = BASE_DIR / "models" / "wav2lip.pth"