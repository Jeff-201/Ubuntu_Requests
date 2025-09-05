import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_images():
    # Prompt the user for multiple image URLs
    print("Enter image URLs (separated by commas or newlines).")
    print("Press ENTER twice when done:\n")

    # Collect multiple lines until blank input
    urls = []
    while True:
        line = input().strip()
        if not line:
            break
        urls.extend([u.strip() for u in line.split(",") if u.strip()])

    # Directory to save images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    success_count = 0
    fail_count = 0
    failed_urls = []

    for i, url in enumerate(urls, start=1):
        try:
            print(f"\n🌐 Fetching: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            # If no filename, set default
            if not filename or "." not in filename:
                filename = "downloaded_image.jpg"

            # Split name and extension
            name, ext = os.path.splitext(filename)

            # Add timestamp to avoid overwriting
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            unique_filename = f"{name}_{timestamp}{ext}"

            save_path = os.path.join(save_dir, unique_filename)

            # Save the image in binary mode
            with open(save_path, "wb") as f:
                f.write(response.content)

            success_count += 1
            print(f"✅ Saved: {save_path}")

        except requests.exceptions.MissingSchema:
            print(f"❌ Invalid URL format: {url}")
            fail_count += 1
            failed_urls.append(url)
        except requests.exceptions.HTTPError as http_err:
            print(f"❌ HTTP error for {url}: {http_err}")
            fail_count += 1
            failed_urls.append(url)
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection failed for {url}")
            fail_count += 1
            failed_urls.append(url)
        except requests.exceptions.Timeout:
            print(f"❌ Timeout fetching {url}")
            fail_count += 1
            failed_urls.append(url)
        except Exception as e:
            print(f"❌ Unexpected error for {url}: {e}")
            fail_count += 1
            failed_urls.append(url)

    # --- Print summary ---
    print("\n📊 Download Summary:")
    print(f"   ✅ Successful: {success_count}")
    print(f"   ❌ Failed: {fail_count}")

    if failed_urls:
        print("\n⚠️ Failed URLs:")
        for u in failed_urls:
            print(f"   - {u}")

if __name__ == "__main__":
    fetch_images()
