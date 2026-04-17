import time


class SportClient:
    def StandUp(self):
        print("[ROBOT] Se para...")
        time.sleep(0.3)

    def StandDown(self):
        print("[ROBOT] Se sienta...")
        time.sleep(0.3)

    def Move(self, vx: float = 0.0, vy: float = 0.0, vyaw: float = 0.0):
        print(f"[ROBOT] Move vx={vx} vy={vy} vyaw={vyaw}")
        time.sleep(0.3)

    def Wave(self):
        print("[ROBOT] Saluda con la mano 👋")
        time.sleep(0.5)
