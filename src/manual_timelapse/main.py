import requests
import os
import datetime
import time

def start_taking_snapshots(output_directory):
    if os.path.exists(output_directory):
        raise Exception("Output directory already exists.")
    os.makedirs(output_directory)

    snapshot_url = "PUBLIC_OCTOPRINT_URL/webcam/?action=snapshot"
    image_number = 0

    while True:

        output_filename = os.path.join(output_directory, "%s.jpg" % image_number)
        r = requests.get(snapshot_url, stream=True)
        r.raise_for_status()

        with open(output_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

        image_number += 1
        time.sleep(2)




def main():
    start_taking_snapshots(datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S"))


if __name__ == "__main__":
    main()
