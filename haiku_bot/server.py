"""Aiohttp server wiring the bot to Microsoft Teams."""

import os
from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity

from .teams_bot import TeamsHaikuBot


async def messages(request: web.Request) -> web.Response:
    if "application/json" not in request.headers.get("Content-Type", ""):
        return web.Response(status=415)

    body = await request.json()
    activity = Activity().deserialize(body)
    auth_header = request.headers.get("Authorization", "")
    response = await ADAPTER.process_activity(
        activity,
        auth_header,
        BOT.on_turn,
    )
    if response:
        return web.json_response(status=response.status)
    return web.json_response(status=201)


APP_ID = os.environ.get("MicrosoftAppId", "")
APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
SETTINGS = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)
BOT = TeamsHaikuBot()

APP = web.Application()
APP.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(APP, host="0.0.0.0", port=3978)
