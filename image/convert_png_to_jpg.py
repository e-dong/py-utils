from PIL import Image
from pathlib import Path
from argparse import ArgumentParser


def main():
    """Entrypoint"""
    parser = ArgumentParser()
    parser.add_argument("image_files", type=Path, nargs="+")
    args = parser.parse_args()
    for image_file in args.image_files:
        jpg_file = image_file.stem + ".jpg"
        print(f"Converting {image_file} to {jpg_file}")
        image = Image.open(image_file)
        rgb_image = image.convert("RGB")
        rgb_image.save(jpg_file)


if __name__ == "__main__":
    main()

