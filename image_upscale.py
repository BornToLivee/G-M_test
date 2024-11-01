from PIL import Image


img = Image.open("profile_photo.png")
img = img.resize((img.width * 3, img.height * 3), Image.LANCZOS)
img.save("profile_photo_upscaled.png")
