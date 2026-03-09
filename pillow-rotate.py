from PIL import Image
from pathlib import Path

path = Path("G:\\Rezler\\") # source and destination path are the same
start_image_number = 192
end_image_number = 284
for i in range(start_image_number, end_image_number):
    if i % 2 != 0:
        im = Image.open(path.joinpath(f"{i:03d}.jpg"))
        im.rotate(180).save(path.joinpath(f"{i:03d}.jpg"))

