from PIL import Image

# Wczytaj obrazek z folderu 'obrazki'
img = Image.open("obrazki/custom-nike-air-force-1-high.jpeg")  # zamien 'obrazek.jpg' na nazwę Twojego pliku

# Zmień rozdzielczość na 120x120
img_resized = img.resize((60, 60))
img_resized2 = img.resize((60, 60), resample=Image.Resampling.LANCZOS)

# Zapisz zmieniony obrazek (np. do folderu 'obrazki' z nową nazwą)
img_resized.save("obrazki/obrazek_25x25.jpg")
img_resized2.save("obrazki/obrazek_25x25_L.jpg")


