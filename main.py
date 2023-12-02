from dotenv import load_dotenv
from openai import AsyncOpenAI
import asyncio, os
import pandas as pd


def write_to_file(text):
    with open("EXAMPLE.txt", 'a', encoding="utf-8") as file:
        file.write(text + "\n" + "-" * 100 + " // divider \n")


async def generate(message) -> str:
    chat_completion = await client.chat.completions.create(
        messages=[
            message
        ],
        
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


async def generate_concurently(messages):
    tasks = [generate(message) for message in messages]
    tasks = await asyncio.gather(*tasks)
    return tasks


def get_messages(df: pd.DataFrame, context: str, role: str="system", num_countent: int=5) -> list:
    random_sample = df.sample(n=num_countent, ignore_index=True)
    random_sample = random_sample.to_dict('records')
    messages = []
    for house in random_sample:
        prompt = context + f"Hosue price: {house['price']}$. Area: {house['area']}. The number of bedrooms: {house['bedrooms']}. The number of bathrooms: {house['bathrooms']}. Stories: {house['stories']}. Main road: {house['mainroad']}. Guestroom: {house['guestroom']}. Basement: {house['basement']}. Hot water heating: {house['hotwaterheating']}. Air conditioning: {house['airconditioning']}. The number of parking: {house['parking']}. Prefarea: {house['prefarea']}. Furnishing status: {house['furnishingstatus']}. Put the price towards the end."
        message = {
            "role": role,
            "content": prompt
        }
        messages.append(message)
    return messages



if __name__ == "__main__":
    # Read data
    data = pd.read_csv("Housing.csv")

    # Load params from .env file
    load_dotenv()

    client = AsyncOpenAI(
        api_key=os.getenv("API_KEY"),
    )

    context = "You are the one who creates content on Instagram for the sale of real estate in various price categories; the description of the houses should be interesting and engaging. Here are the characteristics of the house,"
    messages = get_messages(data, context)
    print("Generating content on randomly selected houses")
    contents = asyncio.run(generate_concurently(messages))
    print("Saving generated contents in EXAMPLE.txt file")

    # Use list() to consume the iterator and execute the write_to_file function for each element
    list(map(write_to_file, contents))
    print("Done!")
    
    # print(contents)

