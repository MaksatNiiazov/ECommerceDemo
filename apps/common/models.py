import os
from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models


class ImageModel(models.Model):

    def process_and_save_image(self, image_field, max_width=800, max_height=800, format='WEBP', quality=85):
        """
        Resizes and converts the given image field to .webp format.
        """
        if not hasattr(self, image_field):
            raise ValueError(f"The model does not contain a field '{image_field}'.")

        image_file = getattr(self, image_field)
        if not image_file or image_file.name.endswith('.webp'):
            return  # Skip processing if no file or already in .webp format

        old_path = image_file.path if hasattr(image_file, 'path') else None

        try:
            # Open the image file
            image = Image.open(image_file)
            original_width, original_height = image.size
            ratio = min(max_width / original_width, max_height / original_height)
            new_width = int(original_width * ratio)
            new_height = int(original_height * ratio)
            resized_image = image.resize((new_width, new_height), Image.LANCZOS)

            # Save as .webp in memory
            image_io = BytesIO()
            resized_image.save(image_io, format=format, quality=quality)
            new_name = f"{image_file.name.rsplit('.', 1)[0]}.webp"

            # Save the new file to the field
            image_file.save(new_name, ContentFile(image_io.getvalue()), save=False)

            # Delete the old file if it exists and has been replaced
            if old_path and old_path != image_file.path:
                if os.path.isfile(old_path):
                    os.remove(old_path)

        except Exception as e:
            raise RuntimeError(f"Error processing image {image_field}: {e}")

    def save(self, *args, **kwargs):
        self.process_and_save_image('image')
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class BasicModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True