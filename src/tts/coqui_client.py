from TTS.api import TTS
from src.config import TTS_MODEL_EN, TTS_MODEL_HI, OUTPUT_DIR
import soundfile as sf

def generate_tts(text: str, lang: str, out_path):
    model = TTS(TTS_MODEL_EN if lang == "en" else TTS_MODEL_HI)
    wav = model.tts(text)
    sf.write(out_path, wav, 22050)
    return out_path