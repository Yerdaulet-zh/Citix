from PIL import Image 
from io import BytesIO
from config import client, image_client, image_params, context

import asyncio, openai, base64, retrying
import pandas as pd


# Save generated content with params
def write_to_file(houses: list, contents: list) -> None:
    for i in range(len(houses)):
        house = houses[i]
        content = contents[i]
        
        text = f"price={house['price']}\nArea={house['area']}\nThe number of bedrooms={house['bedrooms']}\nparking={house['parking']}\n"
        if house['mainroad'] == "yes":
            text += f"mainroad={house['mainroad']}\n"
        if house['guestroom'] == "yes":
            text += f"guestroom={house['guestroom']}\n"
        if house['basement'] == "yes":
            text += f"basement={house['basement']}\n"
        if house['hotwaterheating'] == "yes":
            text += f"hotwaterheating={house['hotwaterheating']}\n"
        if house['airconditioning'] == "yes":
            text += f"airconditioning={house['airconditioning']}\n"
        if house['prefarea'] == "yes":
            text += f"prefarea={house['prefarea']}\n"
        if house['furnishingstatus'] == "yes":
            text += f"furnishingstatus={house['furnishingstatus']}\n"
        text += f"{content}\n" + "-" * 100 + "// divider \n"
        
        with open("EXAMPLE.txt", 'a', encoding="utf-8") as file:
            file.write(text)


# Randomly selects and prepares the prompt
def get_messages(df: pd.DataFrame, num_content: int=5) -> list:
    random_sample = df.sample(n=num_content, ignore_index=True)
    random_sample = random_sample.to_dict('records')
    messages = []
    
    for house in random_sample:
        prompt = context + f"Hosue price: {house['price']}$. Area: {house['area']}. The number of bedrooms: {house['bedrooms']}. The number of bathrooms: {house['bathrooms']}. Stories: {house['stories']}. The number of parking: {house['parking']}."
        
        if house['mainroad'] == "yes":
            prompt += f" Main road: {house['mainroad']}."
        if house['guestroom'] == "yes":
            prompt += f" Guestroom: {house['guestroom']}."
        if house['basement'] == "yes":
            prompt += f" Basement: {house['basement']}."
        if house['hotwaterheating'] == "yes":
            prompt += f" Hot water heating: {house['hotwaterheating']}."
        if house['airconditioning'] == "yes":
            prompt += f" Air conditioning: {house['airconditioning']}."
        if house['prefarea'] == "yes":
            prompt += f" Prefarea: {house['prefarea']}."
        if house['furnishingstatus'] == "yes":
            prompt += f" Furnishing status: {house['furnishingstatus']}."
        prompt += " Put the price towards the end."
        message = {
            "role": "system",
            "content": prompt
        }
        messages.append(message)
    return random_sample, messages


# Save generated images on the folder and all prompts
def save_images_configs(prompts: list, results: list) -> None: 
    revised_prompts = []
    
    for i, result in enumerate(results):
        result = result.data[0]
        image = Image.open(BytesIO(base64.b64decode(result.b64_json)))
        image.save("images/" + str(i) + ".png")
        revised_prompts.append(result.revised_prompt)

    pd.DataFrame({
        "prompts": prompts,
        "revised_prompts": revised_prompts, 
        "generated_image": range(0, len(results))
    }).to_csv("Dalle3.csv", index=False)


# Text generation
@retrying.retry(wait_fixed=1000, stop_max_attempt_number=5)
async def generate(message: str) -> str:
    chat_completion = await client.chat.completions.create(
        messages=[
            message
        ],
        model="gpt-3.5-turbo",
        temperature=0.7,
        top_p=0.7, 
    )
    return chat_completion.choices[0].message.content


# Creates tasks for asynchronous text generation
async def generate_concurently(messages: list) -> list:
    tasks = [generate(message) for message in messages]
    tasks = await asyncio.gather(*tasks)
    return tasks


# Image Generation according to the prompt and params
@retrying.retry(wait_fixed=1000, stop_max_attempt_number=5)
async def image_generate(prompt: str) -> list:
        image_params["prompt"] = prompt
        try:
            images_response = await image_client.images.generate(**image_params)
        except openai.APIConnectionError as e:
            print("Server connection error: {e.__cause__}")  # from httpx.
            raise
        except openai.RateLimitError as e:
            print(f"OpenAI RATE LIMIT error {e.status_code}: (e.response)")
            raise
        except openai.APIStatusError as e:
            print(f"OpenAI STATUS error {e.status_code}: (e.response)")
            raise
        except openai.BadRequestError as e:
            print(f"OpenAI BAD REQUEST error {e.status_code}: (e.response)")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise
        return images_response


# Creates tasks for asynchronous image generation
async def generate_images_concurently(prompts: list) -> list:
    tasks = [image_generate(prompt) for prompt in prompts]
    tasks = await asyncio.gather(*tasks)
    return tasks

