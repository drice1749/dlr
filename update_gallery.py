import os

# Path to the folder containing your images
image_folder = 'mywork'
# Path to your work.html file
work_html = 'work.html'

# Supported image extensions
image_exts = ['.jpg', '.jpeg', '.png', '.gif', '.webp']

# Get all image filenames in the folder
images = [f for f in os.listdir(image_folder) if os.path.splitext(f)[1].lower() in image_exts]
images.sort()

gallery_html = '\n'.join([
    f'        <img src="{image_folder}/{img}" alt="My work: {img}">' for img in images
])

# Read the work.html file
with open(work_html, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the gallery div content
import re
html = re.sub(
    r'(<div class="gallery" id="gallery">)(.*?)(</div>)',
    f'\\1\n{gallery_html}\n    \\3',
    html,
    flags=re.DOTALL
)

# Remove the dynamic JS block if present
html = re.sub(r'<script>.*?</script>\s*</body>', '</body>', html, flags=re.DOTALL)

# Write the updated HTML back
with open(work_html, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Gallery updated with {len(images)} images.")
