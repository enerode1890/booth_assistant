import json
import os
import re
from datetime import datetime
from typing import Optional

import config
from intents import responses


_KEYWORDS = {
    "saludo": [
        r"\bhola\b", r"\bbuenas\b", r"\bey\b", r"\bhi\b", r"\bbuenos días\b",
        r"\bbuenas tardes\b", r"\bbuenas noches\b", r"\bqué tal\b", r"\bqué hubo\b",
    ],
    "despedida": [
        r"\badiós\b", r"\bchao\b", r"\bhasta luego\b", r"\bnos vemos\b",
        r"\bhasta pronto\b", r"\bme voy\b", r"\bchau\b",
    ],
    "info_producto": [
        r"\bproducto\b", r"\bcerdo\b", r"\bcarne\b", r"\bvitamar\b", r"\busda\b",
        r"\bcertificad\b", r"\bimportad\b", r"\bqué venden\b", r"\bqué ofrecen\b",
        r"\bcuéntame\b", r"\binfo\b", r"\binformación\b",
    ],
    "captura_lead": [
        r"\bme interesa\b", r"\bquiero saber más\b", r"\bcómo consigo\b",
        r"\bcómo compro\b", r"\bdónde compro\b", r"\bcontacto\b",
        r"\bdéjame tus datos\b", r"\bquiero más info\b", r"\bprecio\b",
    ],
    "chiste": [
        r"\bchiste\b", r"\bcuéntame algo\b", r"\bhazme reír\b",
        r"\bbroma\b", r"\balgo gracioso\b", r"\bdi un chiste\b",
    ],
}


def detect_intent(text: str) -> str:
    normalized = text.lower().strip()
    for intent, patterns in _KEYWORDS.items():
        for pattern in patterns:
            if re.search(pattern, normalized):
                return intent
    return "fallback"


class IntentHandler:
    def __init__(self, audio_client, loco_client):
        self.audio = audio_client
        self.loco = loco_client
        self._lead_state: Optional[dict] = None  # tracks mid-flow lead capture

    def handle(self, text: str) -> bool:
        """Process user input. Returns True if the conversation should end."""
        if self._lead_state is not None:
            return self._continue_lead_capture(text)

        intent = detect_intent(text)
        handler = {
            "saludo": self._saludo,
            "despedida": self._despedida,
            "info_producto": self._info_producto,
            "captura_lead": self._captura_lead,
            "chiste": self._chiste,
            "fallback": self._fallback,
        }.get(intent, self._fallback)

        return handler()

    # --- intent handlers ---

    def _saludo(self) -> bool:
        self.loco.WaveHand()
        self.audio.LedControl(0, 255, 100)
        self._say(responses.saludo())
        return False

    def _despedida(self) -> bool:
        self.audio.LedControl(255, 165, 0)
        self._say(responses.despedida())
        return True

    def _info_producto(self) -> bool:
        self.audio.LedControl(0, 100, 255)
        self._say(responses.info_producto(config.PRODUCT_NAME, config.DISTRIBUTOR))
        return False

    def _captura_lead(self) -> bool:
        self._lead_state = {"step": "nombre"}
        self._say(responses.solicitar_lead())
        return False

    def _chiste(self) -> bool:
        self.audio.LedControl(255, 200, 0)
        self._say(responses.chiste())
        return False

    def _fallback(self) -> bool:
        self._say(responses.fallback())
        return False

    # --- lead capture flow ---

    def _continue_lead_capture(self, text: str) -> bool:
        step = self._lead_state.get("step")

        if step == "nombre":
            self._lead_state["nombre"] = text.strip().title()
            self._lead_state["step"] = "contacto"
            self._say("¿Y tu correo o número de WhatsApp?")
            return False

        if step == "contacto":
            lead = {
                "nombre": self._lead_state["nombre"],
                "contacto": text.strip(),
                "timestamp": datetime.now().isoformat(),
            }
            self._save_lead(lead)
            nombre = lead["nombre"]
            self._lead_state = None
            self.audio.LedControl(0, 255, 0)
            self._say(responses.confirmar_lead(nombre))
            return False

        self._lead_state = None
        return False

    # --- helpers ---

    def _say(self, text: str):
        print(f"\n🤖 G1: {text}\n")
        self.audio.TtsMaker(text, 0)

    @staticmethod
    def _save_lead(lead: dict):
        path = config.LEADS_FILE
        leads = []
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    leads = json.load(f)
                except json.JSONDecodeError:
                    leads = []
        leads.append(lead)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(leads, f, ensure_ascii=False, indent=2)
        print(f"[LEAD] Guardado: {lead['nombre']} → {lead['contacto']}")
