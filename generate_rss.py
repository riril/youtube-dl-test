from pathlib import Path
import ujson

from jinja2 import Template


template_text = (Path(".") / "templates" / "rss.xml.jinja2").read_text(encoding="utf-8")


def operation(enclosure_url_prefix="downloads/", generate_rss_filename="rss.xml"):
    is_first_episode = True
    result = {"items": []}

    download_path = Path(".") / "downloads"
    for item in download_path.iterdir():
        if item.suffix == ".m4a":
            name = item.stem
            info_path = download_path / f"{name}.info.json"
            if info_path.exists():
                data = ujson.loads(info_path.read_text(encoding="utf-8"))
                if is_first_episode:
                    result["title"] = data.get("playlist_title")
                    # if data.categories and isinstance(data.categories, list):
                    #     result["categories"] = data.categories[0]
                    result["playlist"] = data.get("playlist")
                    result["link"] = data.get("webpage_url")
                    result["description"] = data.get("playlist_title")
                    result["itunes_author"] = data.get("uploader")
                    result["image"] = data.get("thumbnail")
                    is_first_episode = False
                item_content = {}
                item_content["title"] = data.get("title")
                item_content["description"] = data.get("description")
                item_content["pubDate"] = data.get("upload_date")
                item_content["link"] = data.get("webpage_url")
                item_content["itunes_item_image"] = data.get("thumbnail")
                item_content["enclosure_url"] = f"{enclosure_url_prefix}{item.name}"
                item_content["enclosure_length"] = int(data.get("duration", 0))
                item_content["enclosure_type"] = "audio/x-m4a"
                m, s = divmod(data.get("duration", 0), 60)
                item_content["itunes_duration"] = "{:02d}:{:02d}".format(int(m), int(s))
                item_content["category"] = data.get("categories")
                result["items"].append(item_content)
    template = Template(template_text)
    rss = template.render(**result)
    with open(
        generate_rss_filename,
        "w",
        encoding="utf-8",
    ) as f:
        f.write(str(rss))


if __name__ == "__main__":
    operation()
