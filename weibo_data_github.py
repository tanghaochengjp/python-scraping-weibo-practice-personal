import csv
import json
import subprocess
import time
from urllib.parse import quote

topic = quote("#杭州亚运会志愿者#")
MAX_PAGES = 7
OUTPUT_FILE = "weibo_mydata_time_2023-2025.csv"

SET_URL = """
on run argv
    tell application "Google Chrome"
        set URL of active tab of front window to item 1 of argv
    end tell
end run
"""

RUN_JS = """
on run argv
    tell application "Google Chrome"
        return execute active tab of front window javascript (item 1 of argv)
    end tell
end run
"""

EXTRACT_JS = """
var rows = [];
var cards = document.querySelectorAll("div.card-wrap");

for (var i = 0; i < cards.length; i++) {

    var card = cards[i];

    var textNode = card.querySelector(
        'p.txt[node-type="feed_list_content_full"]'
    );

    if (!textNode) {
        textNode = card.querySelector(
            'p.txt[node-type="feed_list_content"]'
        );
    }

    if (!textNode) {
        textNode = card.querySelector("p.txt");
    }

    var fromNode = card.querySelector("p.from");

    if (!fromNode) {
        fromNode = card.querySelector("div.from");
    }

    if (textNode && fromNode) {

        var a = fromNode.querySelector("a");

        if (a) {

            var postTime = a.getAttribute("title");

            if (!postTime) {
                postTime = a.textContent.trim();
            }

            var text = textNode.textContent.trim();
            var link = a.href;

            var item = {
                time: postTime,
                text: text,
                link: link
            };

            rows.push(item);
        }
    }
}

if (rows.length > 0) {
    JSON.stringify(rows);
} else {
    "wait";
}
"""

def open_page(url):

    result = subprocess.run(
        ["osascript", "-e", SET_URL, url],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True

    return False

def read_page():

    for i in range(10):

        time.sleep(1)

        result = subprocess.run(
            ["osascript", "-e", RUN_JS, EXTRACT_JS],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return None

        data = result.stdout.strip()

        if data != "" and data != "wait":
            return data

    return None

rows = []

for page in range(1, MAX_PAGES + 1):

    print("正在读取第", page, "页...")

    url = f"https://s.weibo.com/weibo/{topic}?timescope=custom:2023-01-01:2025-12-31&nodup=1&page={page}"

    if open_page(url) == False:
        print("出现问题，请重新检查")
        break

    result = read_page()

    if result is None:
        print("出现问题，请重新检查")
        break

    try:
        items = json.loads(result)
    except:
        print("出现问题，请重新检查")
        break

    for item in items:

        post_time = item.get("time", "").strip()
        text = " ".join(item.get("text", "").split())
        link = item.get("link", "").strip()

        if (
            post_time.startswith("2023")
            or post_time.startswith("2024")
            or post_time.startswith("2025")
        ):
            rows.append([post_time, text, link])

    if page < MAX_PAGES:
        time.sleep(7)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as f:

    writer = csv.writer(f)
    writer.writerow(["发布时间", "原文正文", "原文链接"])
    writer.writerows(rows)

print("共保存", len(rows), "条微博。")
