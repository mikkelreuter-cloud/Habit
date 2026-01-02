#!/usr/bin/env python3
"""
Generate PNG icons for the Momentum PWA
Requires: pip install pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename):
    """Create a simple icon for the app"""
    # Create image with cream background
    img = Image.new('RGB', (size, size), '#f4f1ea')
    draw = ImageDraw.Draw(img)

    # Draw circle (clock face)
    margin = size // 8
    circle_bbox = [margin, margin, size - margin, size - margin]
    draw.ellipse(circle_bbox, outline='#2d2d2d', width=size // 64)

    # Draw clock hands
    center = size // 2
    # Hour hand
    draw.line([(center, center), (center, margin + size // 8)], fill='#2d2d2d', width=size // 42)
    # Minute hand
    draw.line([(center, center), (size - margin - size // 8, center)], fill='#2d2d2d', width=size // 42)

    # Draw center dot
    dot_radius = size // 42
    draw.ellipse([center - dot_radius, center - dot_radius,
                  center + dot_radius, center + dot_radius], fill='#2d2d2d')

    # Draw "M" letter
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", size // 7)
    except:
        font = ImageFont.load_default()

    text = "M"
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = (size - text_width) // 2
    text_y = size - margin - text_height - size // 16

    draw.text((text_x, text_y), text, fill='#2d2d2d', font=font)

    # Save
    img.save(filename, 'PNG')
    print(f"Created {filename} ({size}x{size})")

if __name__ == '__main__':
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create icons
    create_icon(192, os.path.join(script_dir, 'icon-192.png'))
    create_icon(512, os.path.join(script_dir, 'icon-512.png'))

    print("\n✓ Icons generated successfully!")
    print("You can now use the PWA on your phone.")
