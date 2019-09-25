from dhooks import Webhook, Embed

import requests


class FortnitePatchNotes(object):
    @classmethod
    def request(self, patch_notes_url):
        """

        Sends GET request to the specified URL, returns the response's status code

        """

        response = requests.get(
            patch_notes_url,
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
            }
        ).status_code

        return response

    @classmethod
    def webhook(self, patch_notes_url, discord_webhook):
        """

        Sends POST request to the specified webhook URL, posts in a neat fashion

        """

        hook = Webhook(discord_webhook)

        embed = Embed(
            description="Epic just released the new patch notes, check them out above!",
            color=0x1e0f3,
            timestamp="now"
            )

        embed.set_author(name="New Fortnite Patch Notes", url=patch_notes_url)
        embed.set_footer(text="Fortnite Patch Notes V1 | by @visuxls")

        hook.send(embed=embed)
