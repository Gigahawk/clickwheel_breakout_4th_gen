import os
from datetime import datetime
import yaml

URL = "https://github.com/Gigahawk/clickwheel_breakout_4th_gen/tree"

config_path = os.environ["KIBOT_QR_CONFIG"]

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
print("#############")

print("Writing KiBot config to generate QR code")
config = {
    "kibot": {
        "version": 1
    },
    "global": {
        "filters": [
            {
                # Supress warning about extra spaces
                "number": 37,
            }
        ]
    },
    "preflight": {
        "update_qr": True
    },
    "outputs": [
        {
            "name": "QR Data Output",
            "type": "qr_lib",
            "dir": "QR_libs",
            "options": {
                "use_sch_dir": False,
                "output": "QR.%x",
                "qrs": [
                    {
                        "name": "QR_data",
                        "correction_level": "low",
                        "size_pcb": 10,
                        "size_sch": 20,
                        "size_units": "millimeters",
                        "text": msg,
                    }
                ]
            }
        }
    ]
}

output = yaml.dump(config)
print("#############")
print(output)
print("#############")

with open(config_path, "w") as f:
    f.write(output)








