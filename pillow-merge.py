from PIL import Image
from pathlib import Path

def vertical_merge(im1, im2):
    width = max(im1.size[0], im2.size[0])
    height = im1.size[1] + im2.size[1]
    im = Image.new('RGB', (width, height))
    im.paste(im1, (0, 0))
    im.paste(im2, (0, im1.size[1]))
    return im

source_path = Path("G:\\Rozwadowski\\")
destination_path = Path("G:\\Rozwadowski\\") / "stud-version"
start_image = 24
end_image = 25
for i in range(start_image, end_image):
    im1 = Image.open(source_path.joinpath((f"{i:03d}a.jpg")))
    im2 = Image.open(source_path / f"{i:03d}b.jpg")
    im = vertical_merge(im1, im2)
    im.save(destination_path / f"{i:03d}.jpg", quality=99, dpi=(150,150))

