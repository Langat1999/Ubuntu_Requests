import requests
import os
import hashlib
from urllib.parse import urlparse
import filetype
import sys

def get_image_extension_from_content(content):
    """Guess image extension from binary content."""
    guess = filetype.guess(content)
    ext = guess.extension if guess else None
    return f".{ext}" if ext else ".jpg"

def get_filename_from_url(url, content):
    """Extract filename from URL or generate from content hash."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename or '.' not in filename:
        # If filename is missing or doesn't contain an extension
        file_hash = hashlib.md5(content).hexdigest()
        filename = file_hash + get_image_extension_from_content(content)

    return filename

def is_duplicate(content, save_dir):
    """Check if a file with the same hash already exists."""
    new_file_hash = hashlib.md5(content).hexdigest()
    for existing_file in os.listdir(save_dir):
        existing_path = os.path.join(save_dir, existing_file)
        if os.path.isfile(existing_path):
            with open(existing_path, 'rb') as f:
                existing_hash = hashlib.md5(f.read()).hexdigest()
                if new_file_hash == existing_hash:
                    return True
    return False

def fetch_and_save_image(url, save_dir="Fetched_Images"):
    try:
        headers = {
            "User-Agent": "UbuntuImageFetcher/1.0"
        }

        # 🌍 Community: Fetch from the web
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # 🛡 Precaution: Check for valid content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"Skipped (Not an image): {url}")
            return "skipped"

        # 📁 Sharing: Create save directory
        os.makedirs(save_dir, exist_ok=True)

        # Generate filename
        filename = get_filename_from_url(url, response.content)
        filepath = os.path.join(save_dir, filename)

        # 🤝 Respect: Skip if duplicate
        if is_duplicate(response.content, save_dir):
            print(f"Duplicate skipped: {filename}")
            return "skipped"

        # 💾 Save image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return "fetched"

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
        return "skipped"
    except Exception as e:
        print(f"✗ An error occurred: {e}")
        return "skipped"

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # URLs from CLI or prompt
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        urls = input("Please enter image URLs (comma-separated): ").split(",")

    fetched_count = 0
    skipped_count = 0

    for url in urls:
        clean_url = url.strip()
        if clean_url:
            result = fetch_and_save_image(clean_url)
            if result == "fetched":
                fetched_count += 1
            else:
                skipped_count += 1

    print("\n✅ Summary:")
    print(f"   📥 Fetched: {fetched_count}")
    print(f"   ⏭ Skipped: {skipped_count}")
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
