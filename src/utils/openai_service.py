import asyncio


async def ask_openai(prompt):
    loop = asyncio.get_event_loop()

    def sync_request():
        return 'Answer from openai'
    
    return await loop.run_in_executor(None, sync_request)