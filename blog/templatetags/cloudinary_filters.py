from django import template
from cloudinary.utils import cloudinary_url

register = template.Library()

@register.filter
def cloudinary_optimized(image_field):
    if not image_field:
        return ""
    url, _ = cloudinary_url(
        image_field.name,
        width=1200,
        crop="scale",
        quality="auto",
        fetch_format="auto"
    )
    return url
