import os
import requests
import zipfile

outdir = "test_data"
csv_dir = "csv"

count = 0
with open('data/masterfilelist.txt', 'r') as txt:
    contents = txt.read().split("\n")
    for row in contents:
        count +=1
        try:
            filename = row.split(" ")[2]
            outname = os.path.split(filename)[1]
            int_zip_file = os.path.join(outdir, outname)
            if "export" in filename:
                if outname.startswith("201504") or outname.startswith("201505") or outname.startswith("201506") or outname.startswith("201507") or outname.startswith("201508") or outname.startswith("201509") or outname.startswith("201510") or outname.startswith("201511") or outname.startswith("201512"):
                print(filename)
                headers = {
                    'Accept': "*/*",
                    'Cache-Control': "no-cache",
                    'Host': "data.gdeltproject.org",
                    'Accept-Encoding': "gzip, deflate",
                    'Connection': "keep-alive",
                    'cache-control': "no-cache"
                    }

                response = requests.request("GET", filename, headers=headers)
                open(int_zip_file, 'wb').write(response.content)
                print(response.status_code)

                with zipfile.ZipFile(int_zip_file, 'r') as zip_ref:
                    zip_ref.extractall(csv_dir)

        except Exception as e:
            print(e)
            continue
