from PIL import Image
import os, shutil

script_dir = r'd:\Desktop\py-script\TRAE1'
ico_path = os.path.join(script_dir, 'favicon.ico')
backup_path = ico_path + '.bak'

img = Image.open(ico_path)

if img.mode == 'P':
    img = img.convert('RGBA')
elif img.mode != 'RGBA':
    img = img.convert('RGBA')

needed_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

if not os.path.exists(backup_path):
    shutil.copy2(ico_path, backup_path)

icon_images = []
for size in needed_sizes:
    resized = img.resize(size, Image.LANCZOS)
    icon_images.append(resized)

icon_images[0].save(
    ico_path,
    format='ICO',
    sizes=needed_sizes,
    append_images=icon_images[1:]
)

verify = Image.open(ico_path)
with open(os.path.join(script_dir, 'ico_result.txt'), 'w') as f:
    f.write('OK - sizes: ' + str(verify.info.get('sizes', 'N/A')) + '\n')
