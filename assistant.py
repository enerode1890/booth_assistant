import sys

import config
from intents.handler import IntentHandler

if config.USE_MOCK:
    from mock.audio_client import AudioClient
    from mock.loco_client import LocoClient
else:
    from unitree_sdk2py.g1.audio.g1_audio_client import AudioClient  # type: ignore
    from unitree_sdk2py.g1.loco.g1_loco_client import LocoClient  # type: ignore


BANNER = """
╔══════════════════════════════════════════╗
║   Asistente de Feria — Vitamar Colombia  ║
║        Robot Unitree G1  [MOCK]          ║
╚══════════════════════════════════════════╝
"""

VISITOR_PROMPT = "\n[SISTEMA] Presiona Enter para recibir al siguiente visitante (o escribe 'salir' para terminar)...\n"


def build_clients():
    if not config.USE_MOCK:
        from unitree_sdk2py.core.channel import ChannelFactoryInitialize  # type: ignore
        ChannelFactoryInitialize(0, config.ROBOT_NETWORK_INTERFACE)
    audio = AudioClient()
    loco = LocoClient()
    if not config.USE_MOCK:
        audio.SetTimeout(10.0)
        audio.Init()
        loco.SetTimeout(10.0)
        loco.Init()
    return audio, loco


def visitor_loop(handler: IntentHandler):
    print("─" * 44)
    print("  ¡Nuevo visitante! Di algo para empezar.")
    print("─" * 44)

    while True:
        try:
            user_input = input("👤 Tú: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[Sistema] Interrumpido.")
            sys.exit(0)

        if not user_input:
            continue

        end_conversation = handler.handle(user_input)
        if end_conversation:
            break


def main():
    print(BANNER)
    audio, loco = build_clients()
    audio.SetVolume(80)
    loco.Start()

    try:
        while True:
            handler = IntentHandler(audio, loco)
            visitor_loop(handler)

            try:
                cmd = input(VISITOR_PROMPT).strip().lower()
            except (EOFError, KeyboardInterrupt):
                break

            if cmd == "salir":
                break

    finally:
        loco.Damp()
        print("\n[Sistema] Asistente detenido. ¡Hasta pronto!")


if __name__ == "__main__":
    main()
