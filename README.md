# 下载 youtube 播放列表并生成 podcast

在 `playlists.txt` 文件中填写播放列表的地址（目前只支持一个）。

首先下载播放列表：

```bash
youtube-dl --config-location . --batch-file='./playlists.txt'

# 如果你是私密播放列表的话 可以加上自己的 cookies.txt，这个文件可以通过插件来生成

youtube-dl --config-location . --batch-file='./playlists.txt' --cookies ".\youtube.com_cookies.txt" 
```

生成 `cookies.txt` 的插件：[Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid)


安装好依赖，然后执行 `generate_rss.py` 即可

依赖见 `pyproject.toml` > `[tool.poetry.dependencies]`


然后就会生成一个文件 `1.xml`，然后你就可以把 1.xml 和生成的 downloads 文件夹移动到公网可见的服务器上。你就可以订阅 podcast 了。
