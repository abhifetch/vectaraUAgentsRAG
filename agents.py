import json
import re
from ai_engine.chitchat import ChitChatDialogue
from ai_engine.messages import DialogueMessage,BaseMessage
from uagents import Agent, Context, Model
from helper_functions import create_chat, add_turn

# define dialogue messages; each transition needs a separate message
class InitiateChitChatDialogue(Model):
    pass


class AcceptChitChatDialogue(BaseMessage):
    type: str = "agent_message"

    # user messages, this is the text that the user wants to send to the agent
    agent_message: str


class ChitChatDialogueMessage(DialogueMessage):
    pass


class ConcludeChitChatDialogue(Model):
    """I conclude ChitChat dialogue request"""

    pass


class RejectChitChatDialogue(Model):
    """I reject ChitChat dialogue request"""

    pass

# instantiate the dialogues
chitchat_dialogue = ChitChatDialogue(
    version="0.11",
    storage=agent.storage,
)

@chitchat_dialogue.on_initiate_session(InitiateChitChatDialogue)
async def start_chitchat(
    ctx: Context,
    sender: str,
    msg: InitiateChitChatDialogue,
):
    ctx.logger.info(f"Received init message from {sender} Session: {ctx.session}")
    initial_query = 'I want to learn more about uagents'
    chat_id, initial_response = await create_chat(initial_query, ctx)
    ctx.storage.set('chat_id', chat_id)
    # do something when the dialogue is initiated
    await ctx.send(sender, AcceptChitChatDialogue(agent_message=initial_response))


@chitchat_dialogue.on_start_dialogue(AcceptChitChatDialogue)
async def accepted_chitchat(
    ctx: Context,
    sender: str,
    _msg: AcceptChitChatDialogue,
):
    ctx.logger.info(f"Received accept message from the agent.")


@chitchat_dialogue.on_reject_session(RejectChitChatDialogue)
async def reject_chitchat(
    ctx: Context,
    sender: str,
    _msg: RejectChitChatDialogue,
):
    # do something when the dialogue is rejected and nothing has been sent yet
    ctx.logger.info(f"Received conclude message from: {sender}")


@chitchat_dialogue.on_continue_dialogue(ChitChatDialogueMessage)
async def continue_chitchat(
    ctx: Context,
    sender: str,
    msg: ChitChatDialogueMessage,
):
    ctx.logger.info(f'User wants to send message {msg.user_message}')
    chat_id = ctx.storage.get('chat_id')
    ctx.logger.info(f'Chat id is {chat_id}')
    if chat_id:
        new_query = msg.user_message
        if new_query.lower() != 'exit':
            response = await add_turn(chat_id, new_query,ctx)
            ctx.logger.info(f'Reply from the agent {response}')
            cleaned_response = re.sub(r'\[\d+\]', '', response)
        else :
            await ctx.send(sender, ConcludeChitChatDialogue())
    try:
        await ctx.send(
            sender,
            ChitChatDialogueMessage(
                type="agent_message",
                agent_message=cleaned_response
            ),
        )
    except EOFError:
        await ctx.send(sender, ConcludeChitChatDialogue())


@chitchat_dialogue.on_end_session(ConcludeChitChatDialogue)
async def conclude_chitchat(
    ctx: Context,
    sender: str,
    _msg: ConcludeChitChatDialogue,
):
    # do something when the dialogue is concluded after messages have been exchanged
    ctx.logger.info(f"Received conclude message from: {sender}; accessing history:")
    ctx.logger.info(ctx.dialogue)


agent.include(chitchat_dialogue, publish_manifest=True)
agent.run()
