from modules.utils import FortnitePatchNotes

import json
import time


def main(patch_notes_url, discord_webhook, sleep):
    """

    Calls the required functions from /modules/utils.py

    """

    while True:
        response = FortnitePatchNotes.request(patch_notes_url)
        print("Status Code: {}".format(response))
        if response == 200:
            print("Patch notes up!")
            FortnitePatchNotes.webhook(patch_notes_url, discord_webhook)
            break

        time.sleep(sleep)


if __name__ == "__main__":
    with open("settings/config.json", "r") as f:
        data = json.load(f)

    patch_notes_url = data["patch_notes_url"]
    discord_webhook = data["discord_webhook"]
    sleep = data["sleep"]

    main(patch_notes_url, discord_webhook, sleep)
