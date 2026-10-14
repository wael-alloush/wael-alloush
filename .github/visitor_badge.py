import re
import urllib.request

URL = (
    "https://visitor-badge.laobi.icu/badge"
    "?page_id=wael-alloush.wael-alloush"
    "&left_text=Visitors"
    "&query_only=true"
)

svg = urllib.request.urlopen(URL, timeout=30).read().decode("utf-8", "replace")
count = re.findall(r">(\d+)</text>", svg)[-1]

label = "Visitors"
label_w = 54
value_w = max(28, 12 + len(count) * 7)
total = label_w + value_w
label_x = label_w / 2
value_x = label_w + value_w / 2

badge = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="20" role="img" aria-label="{label}: {count}">
  <title>{label}: {count}</title>
  <clipPath id="r"><rect width="{total}" height="20" rx="3"/></clipPath>
  <g clip-path="url(#r)">
    <rect width="{label_w}" height="20" fill="#0d3b34"/>
    <rect x="{label_w}" width="{value_w}" height="20" fill="#e3b341"/>
  </g>
  <g text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
    <text x="{label_x}" y="14" fill="#ffffff">{label}</text>
    <text x="{value_x}" y="14" fill="#0d3b34">{count}</text>
  </g>
</svg>
"""

with open("visitors.svg", "w", encoding="utf-8", newline="\n") as handle:
    handle.write(badge)
print(count)
