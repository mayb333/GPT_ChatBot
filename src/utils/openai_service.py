import asyncio
import openai
from loguru import logger


async def ask_openai(prompt):
    loop = asyncio.get_event_loop()

    def sync_request():
        logger.info("Sending request to OpenAI")
        try:
            response = openai.ChatCompletion.create(
                model='gpt-4',
                messages=prompt
            )
            logger.info("Succesfully received response from OpenAI")
            return response.choices[0]['message']['content'], response['usage']['completion_tokens']
        except Exception as exp:
            logger.info(f"Error OpenAI:\n{exp}")
            return "Error from OpenAI", 0
    
    return await loop.run_in_executor(None, sync_request)