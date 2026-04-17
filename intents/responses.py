import random

SALUDOS = [
    "¡Hola! Bienvenido al stand de Vitamar. Soy G1, tu asistente robótico. ¿En qué te puedo ayudar?",
    "¡Qué bueno verte! Soy G1, el robot de Vitamar Colombia. ¿Quieres saber sobre nuestro producto estrella?",
    "¡Hey, hola! Bienvenido. Soy G1 y estoy aquí para contarte todo sobre el mejor cerdo del mercado.",
]

DESPEDIDAS = [
    "¡Fue un placer conocerte! Recuerda: Vitamar Colombia, el sabor que te cambia la vida. ¡Hasta pronto!",
    "¡Chao chao! Espero verte de nuevo. No olvides preguntarle a tu distribuidor por el cerdo Vitamar.",
    "¡Hasta la próxima! Si tienes preguntas, aquí estaré. ¡Que te vaya súper bien!",
]

INFO_PRODUCTO = (
    "Te cuento: manejamos {product}, distribuido en Colombia por {distributor}. "
    "Es carne con certificación USDA, lo que significa control de calidad en cada etapa, "
    "desde la granja hasta tu mesa. Trazabilidad total, sabor increíble y los mejores cortes. "
    "¿Te interesa saber cómo conseguirlo?"
)

CHISTES = [
    "¿Por qué el cerdo no usa computador? ¡Porque le da miedo el virus porcino! 🐷",
    "¿Qué le dijo un cerdo a otro? ¡Somos cerdos hermano, no nos bañamos pero nos certificamos! 🐖",
    "¿Cómo se llama un cerdo en el espacio? ¡Astro-chancho! 🚀🐷",
    "¿Por qué los cerdos son buenos en matemáticas? Porque siempre suman… ¡al sabor! 😄",
]

CAPTURA_SOLICITUD = (
    "¡Genial! Me alegra que te interese. Para enviarte más info y conectarte con nuestro equipo, "
    "¿me puedes dar tu nombre y tu correo o WhatsApp?"
)

CAPTURA_CONFIRMACION = (
    "¡Perfecto, {nombre}! Ya quedaste en nuestra lista. El equipo de Vitamar te contactará pronto. "
    "¡Gracias por tu interés!"
)

FALLBACK = [
    "Hmm, no estoy seguro de entenderte bien. ¿Me repites eso?",
    "Perdona, ¿puedes decirlo de otra forma? No quiero darte info incorrecta.",
    "No caché bien eso. ¿Puedes intentarlo de nuevo?",
]


def saludo() -> str:
    return random.choice(SALUDOS)


def despedida() -> str:
    return random.choice(DESPEDIDAS)


def info_producto(product: str, distributor: str) -> str:
    return INFO_PRODUCTO.format(product=product, distributor=distributor)


def chiste() -> str:
    return random.choice(CHISTES)


def solicitar_lead() -> str:
    return CAPTURA_SOLICITUD


def confirmar_lead(nombre: str) -> str:
    return CAPTURA_CONFIRMACION.format(nombre=nombre)


def fallback() -> str:
    return random.choice(FALLBACK)
