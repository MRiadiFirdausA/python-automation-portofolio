from pathlib import Path

folder = Path("files")

for index, file in enumerate(folder.iterdir(), start=1):
    if file.is_file():
        new_name = f"document_{index}{file.suffix}"
        file.rename(folder / new_name)

print("Rename selesai!")
