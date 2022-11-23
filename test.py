import os
import requests
import re
import yaml

URL = "https://onepiecechapters.com"
DATA_FILE = "data.yaml"


def read_yaml():
    with open(DATA_FILE, "r") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        data = yaml.safe_load(file)

        return data


def get_saved_chapter():
    return read_yaml()["latest"]


def write_saved_chapter(num: int):
    data = read_yaml()
    with open(DATA_FILE, "w") as file:
        data["latest"] = num
        yaml.dump(data, file)


def get_latest_chapter():

    r = requests.get(URL)
    text = r.text
    text = text.splitlines()

    tag = ""
    for t in text:
        if "One Piece Chapter " in t:
            tag = t
            break

    chapter_num = re.search('One Piece Chapter (.+?)" ', tag).group(1)
    chapter_path = re.search('href="(.+?)">', tag).group(1)
    chapter_url = URL + chapter_path

    return {"num": chapter_num, "url": chapter_url}


def download_chapter(chapter: dict):
    num = chapter["num"]
    url = chapter["url"]
    folder = f"Chapter {num}"
    r = requests.get(url)
    os.mkdir(folder)
    text = r.text
    text = text.splitlines()

    num = 1

    for t in text:
        if "cdn.onepiecechapters.com" in t:
            aux = re.search('src="(.+?)" ', t).group(1)
            img = requests.get(aux).content
            with open(f"{folder}/page{num}.png", "wb") as handler:
                handler.write(img)
            num += 1


latest_chapter = get_latest_chapter()
download_chapter(latest_chapter)

""" if get_saved_chapter() == latest_chapter["num"]:
    print("No new update")
else:
    write_saved_chapter(latest_chapter["num"])
    print("New chapter")

    print(latest_chapter["url"])
 """
