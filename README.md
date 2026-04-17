# Booth Assistant — Unitree G1

Asistente conversacional para stand de feria. Detecta intenciones del visitante y controla el robot G1 (TTS, LEDs, gestos).

## Requisitos

```bash
pip install unitree_sdk2py  # solo para hardware real
```

## Uso

```bash
# Modo mock (sin robot físico)
python assistant.py

# Modo real (con robot G1 en red)
# Editar config.py: USE_MOCK = False
python assistant.py
```

## Configuración (`config.py`)

| Variable | Default | Descripción |
|---|---|---|
| `USE_MOCK` | `True` | Usar mocks en lugar del SDK real |
| `ROBOT_IP` | `192.168.123.18` | IP del robot en la red |
| `PRODUCT_NAME` | `"Vitamar Colombia"` | Nombre del producto/empresa |

## Intenciones soportadas

- **Saludo** → robot saluda con la mano, LED verde
- **Info producto** → responde sobre Vitamar Colombia, LED azul
- **Captura de lead** → flujo multi-turno para registrar contacto
- **Chiste** → cuenta un chiste, LED amarillo
- **Despedida** → cierra conversación, LED naranja

## Estructura

```
booth_assistant/
├── assistant.py        # Punto de entrada
├── config.py           # Feature flags y configuración
├── intents/
│   ├── handler.py      # Detección y ruteo de intenciones
│   └── responses.py    # Plantillas de respuesta
└── mock/
    ├── audio_client.py # Mock AudioClient (TTS, LED)
    └── loco_client.py  # Mock LocoClient (movimiento)
```
