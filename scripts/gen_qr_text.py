import os
from datetime import datetime

URL = "https://github.com/Gigahawk/clickwheel_breakout_4th_gen/tree"

print("Generating QR text")

date = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")

hash_full = os.environ["GITHUB_SHA"]
hash_short = hash_full[:7]

ref_type = os.environ.get("GITHUB_REF_TYPE")
if ref_type == "tag":
    tag = os.environ.get("GITHUB_REF_NAME")
else:
    tag = None

msg = f"""Date: {date}
Link: {URL}/{hash_short}"""

if tag != None:
    msg += f"\nTag: {tag}"

print("#############")
print(msg)
with open("_QR_TEXT.txt", "w") as f:
    f.write(msg)






