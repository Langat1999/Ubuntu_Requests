# Ubuntu Image Fetcher
![how-to-install-jellyfin-media-server-on-ubuntu-1024x647](https://github.com/user-attachments/assets/ce1d3ef0-27a8-49e9-b1e7-35fffc5298a3)

A Python script for mindfully collecting images from the web. This tool fetches images from provided URLs, saves them to a local directory, and includes features like duplicate detection and automatic filename generation.

## Features

- **Image Fetching**: Downloads images from specified URLs
- **Duplicate Detection**: Skips downloading images that already exist in the save directory based on content hash
- **Automatic Filename Generation**: Generates unique filenames using content hash and detected extension
- **Content Type Validation**: Ensures only image files are downloaded
- **Error Handling**: Gracefully handles network errors, invalid URLs, and non-image content
- **Flexible Input**: Accepts URLs via command line arguments or interactive prompt

## Installation

1. Ensure you have Python 3.6 or higher installed
2. Install the required dependencies:
   ```bash
   pip install requests filetype
   ```

## Usage

### Command Line
```bash
python ubuntu_image_fetcher.py <url1> <url2> <url3> ...
```

### Interactive Mode
```bash
python ubuntu_image_fetcher.py
```
When run without arguments, the script will prompt you to enter URLs separated by commas.

## Examples

### Single Image
```bash
python ubuntu_image_fetcher.py https://picsum.photos/200/300
```

### Multiple Images
```bash
python ubuntu_image_fetcher.py https://picsum.photos/200/300 https://picsum.photos/400/600
```

### Interactive Mode
```bash
python ubuntu_image_fetcher.py
# Then enter: https://picsum.photos/200/300, https://picsum.photos/400/600
```

## Output

Images are saved to the `Fetched_Images/` directory. The script provides feedback on:
- Successfully fetched images
- Skipped duplicates
- Non-image URLs
- Connection errors

## Requirements

- Python 3.6+
- requests
- filetype

## License

This project is open source and available under the MIT License.
