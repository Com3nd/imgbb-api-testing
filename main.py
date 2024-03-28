import requests
import os


def upload_image(api_key, image_path, name=None, expiration=None):
    url = "https://api.imgbb.com/1/upload"
    params = {
        "key": api_key,
        "name": name,
        "expiration": expiration
    }

    with open(image_path, "rb") as file:
        files = {"image": file}
        response = requests.post(url, params=params, files=files)

    if response.status_code == 200:
        data = response.json()
        if data["success"]:
            print("Image uploaded successfully!")
            print("Image URL:", data["data"]["display_url"])
            return data["data"]["display_url"]
        else:
            print("Failed to upload image. Error:", data["error"]["message"])
    else:
        print("Failed to upload image. Status code:", response.status_code)


def download_image(image_url):
    data = requests.get(image_url).content
    image_name = os.path.basename(image_url)
    # Save the image to a file
    with open(f"downloads/{image_name}", "wb") as f:
        f.write(data)


if __name__ == '__main__':
    # Example usage
    api_key = "dda75f66f424e265139e11ed77a95423"
    image_path = "python.jpg"
    url = upload_image(api_key, image_path)
    input("Download the image?...")
    download_image(url)
