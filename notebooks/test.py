import requests

HEADERS = {"User-Agent": "chicago-airport-transport"}
ENDPOINTS = [
    ("Chicago Data Portal", "https://data.cityofchicago.org/resource/wrvz-psew.json?$limit=1", True),
    ("BTS TranStats", "https://www.transtats.bts.gov/", True),
    ("NOAA NCEI", "https://www.ncei.noaa.gov/", True),
    ("NOAA CPC", "https://www.cpc.ncep.noaa.gov/", True),
    ("AWS S3", "https://s3.amazonaws.com/", False),
    ("NWS api.weather.gov", "https://api.weather.gov/", False),
    ("PyPI", "https://pypi.org/simple/", False)
]
VOLUME = '/Volumes/airpot/bronze/landing'
test_dir = f"{VOLUME}_healthcheck"
test_file = f"{test_dir}/write_test.txt"

def check(url, timeout=15):
    '''Return (status, detail)'''
    try:
        # stream=True: Only need the status line, not the whole body
        resp = requests.get(url, headers=HEADERS, timeout=timeout, stream=True)
        resp.close()
        return "REACHABLE", f"HTTP {resp.status_code}"
    except requests.exceptions.RequestException as exc:
        return "BLOCKED", type(exc).__name__ 

results = []
for label, url, required in ENDPOINTS:
    status, detail = check(url)
    results.append((label, "required" if required else "optional", status, detail))

#display(spark.createDataFrame(results, ["source", "need", 'status', 'detail']))

blocked_required = [r[0] for r in results if r[1] == "required" and r[2] == 'BLOCKED']

if not blocked_required:
    print("All required sources reachable.")
else:
    print("Blocked required sources:")
    for name in blocked_required:
        print(f"-{name}")