import os
from dotenv import load_dotenv
from openai import AsyncOpenAI


# Load params from .env file
load_dotenv()

# Get an acccess to our asyncronic client 
client = AsyncOpenAI(
    api_key=os.getenv("API_KEY"),
)
image_client = AsyncOpenAI(
    api_key=os.getenv("API_KEY"),
)

# Context for text generation
context = "You are the one who creates content on Instagram for the sale of real estate in various price categories; the description of the houses should be interesting and engaging; Use emotions wisely; Here are the characteristics of the house: "

image_params = {
    "model": "dall-e-3",  # Defaults to dall-e-2
    "size": "1024x1024",  # 256x256, 512x512 only for DALL-E 2 - not much cheaper
    # "prompt": prompt,     # DALL-E 3: max 4000 characters, DALL-E 2: max 1000
    "response_format": "b64_json", # Do not return in url format
}

image_prompts = [
    "Generate a cozy modern house with large windows, a fireplace, and a minimalist interior. Do not put any text.", 
    "Create vibrant and heartwarming house scenes inspired by the enchanting atmosphere of the 'Home Alone' movie. Infuse the scenes with the nostalgic charm of a festive home, complete with twinkling lights, classic holiday decorations, and the cozy warmth that defines the beloved film. Let the spirit of 'Home Alone' shine through in each generated image. Do not put any text.",
    "Picture a charming and nostalgic house inspired by the magical world of 'Harry Potter' The scene exudes warmth and welcomes you with open arms. Think of cozy fireplaces, flickering candlelight, and magical elements that evoke the enchanting atmosphere of the wizarding world. The ambiance is inviting and filled with a sense of nostalgia, transporting you to a place that feels like home in the wizarding realm. Do not put any text.",
    "Kazakh Yurt in a yurt, Do not put any text.",
]
