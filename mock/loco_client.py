import time


class LocoClient:
    def Start(self):
        print("[ROBOT] Se para...")
        time.sleep(0.3)

    def Damp(self):
        print("[ROBOT] Se sienta...")
        time.sleep(0.3)

    def Move(self, vx: float = 0.0, vy: float = 0.0, vyaw: float = 0.0, continous_move: bool = False):
        print(f"[ROBOT] Move vx={vx} vy={vy} vyaw={vyaw}")
        time.sleep(0.3)

    def WaveHand(self, turn_flag: bool = False):
        print("[ROBOT] Saluda con la mano")
        time.sleep(0.5)
