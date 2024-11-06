from uagents import Field
from ai_engine import UAgentResponse, UAgentResponseType
from helper_functions import create_chat
 
class QueryRequest(Model):
    query: str = Field(description="This is the query which user wants to send to fetch docs RAG.")
 
 
rag_query = Protocol("FETCH RAG QUERY")
 
 
@rag_query.on_message(model=QueryRequest, replies={UAgentResponse})
async def roll_dice(ctx: Context, sender: str, msg: QueryRequest):
    ctx.logger.info(f'User has asked query {msg.query}')
    chat_id, response = await create_chat(msg.query, ctx)
    ctx.logger.info(f'User has asked query {msg.query} and got response {response}')
    await ctx.send(
        sender, UAgentResponse(message=response, type=UAgentResponseType.FINAL)
    )
 
 
agent.include(rag_query, publish_manifest=True)
