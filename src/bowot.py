import discord
import logging
from owoify import owoify

logger = logging.getLogger("Bowot")


class Bowot(discord.Client):
    def __init__(self, id, permissions):
        super().__init__()
        self.id = id
        self.permissions = permissions

    def invite_link(self):
        return "https://discord.com/api/oauth2/authorize?client_id={0}&permissions={1}&scope=bot".format(self.id, self.permissions)

    async def on_ready(self):
        logger.info("Started running Bowot as {0}".format(self.user))
        logger.info("Invite to server using {0}".format(self.invite_link()))

    async def on_message(self, message):
        if not message.content.startswith("!owo"):
            return

        input_text = None

        if message.reference and message.reference.resolved is not None:
            input_text = message.reference.resolved.content
        elif len(message.content[5:].strip()) == 0:
            messages = await message.channel.history(limit=1, before=message).flatten()
            if len(messages) == 1:
                input_text = messages[0].content
        else:
            input_text = message.content[5:]

        if input_text is None:
            await message.reply("OwOh nyo! sumfin's bwoken...")
            return

        reply = owoify(input_text)

        if len(reply) > 1900:
            await message.reply("No. :(")
        else:
            await message.reply(reply)
