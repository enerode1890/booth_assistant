class AudioClient:
    def TtsMaker(self, text: str, speaker_id: int = 0, volume: float = 1.0):
        print(f"[TTS] 🔊 {text}")

    def LedControl(self, r: int, g: int, b: int):
        print(f"[LED] RGB({r}, {g}, {b})")

    def SetVolume(self, level: float):
        print(f"[AUDIO] Volumen → {level}")
