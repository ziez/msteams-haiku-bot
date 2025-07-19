"""Microsoft Teams bot that responds with haikus."""

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext

from .bot import handle_message


class TeamsHaikuBot(ActivityHandler):
    """Bot Framework handler that converts qualifying messages to haiku."""

    async def on_message_activity(self, turn_context: TurnContext) -> None:
        """Respond to a Teams message."""
        text = turn_context.activity.text or ""
        response = handle_message(text)
        await turn_context.send_activity(MessageFactory.text(response))
