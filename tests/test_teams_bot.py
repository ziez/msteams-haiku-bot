import pytest
from botbuilder.core.adapters.test_adapter import TestAdapter

from haiku_bot.teams_bot import TeamsHaikuBot


@pytest.mark.asyncio
async def test_teams_haiku_bot():
    bot = TeamsHaikuBot()
    adapter = TestAdapter(bot.on_turn)

    await adapter.test("short", "short")

    haiku = "An old silent pond a frog jumps into the pond splash silence again"
    expected = "An old silent pond\na frog jumps into the pond\nsplash silence again"
    await adapter.test(haiku, expected)
