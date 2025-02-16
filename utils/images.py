from pathlib import Path
from PIL import Image
from django.conf import settings

def resize_image(image_django, new_width=800, optimize=True, quality=60):
    # Altere a maneira como você resolve o caminho para um Path corretamente
    image_path = Path(settings.MEDIA_ROOT) / image_django.name
    image_pillow = Image.open(image_path)
    
    original_width, original_height = image_pillow.size
    if original_width <= new_width:
        image_pillow.close()
        return image_pillow
    
    new_height = round(new_width * original_height / original_width)
    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)
    
    # Salve o arquivo no caminho correto
    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )
    
    return new_image
