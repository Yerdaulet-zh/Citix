from utils import get_messages, generate_concurently, write_to_file, generate_images_concurently, save_images_configs
from config import image_prompts
import asyncio, os, time
import pandas as pd



def main() -> None:
    # Create images folder to save generated images, if exists do not recreate!
    os.makedirs("images", exist_ok=True)

    # Read the data
    data = pd.read_csv("Housing.csv")
    random_sample, messages = get_messages(data, num_content=20)   
    
    print("Generating content for randomly selected houses")
    
    start = time.time()
    contents = asyncio.run(generate_concurently(messages))
    end = time.time() - start
    
    print(f"All generated texts of {len(random_sample)} houses were received in {end:.2f}\nSaving the generated content in the EXAMPLE.txt file")

    # Write all generated contents
    write_to_file(random_sample, contents)
    
    print("Done!\nImage generation part has started\nAsyncronically generating images according to prompts")
    
    start = time.time()
    dalle_results = asyncio.run(generate_images_concurently(image_prompts))
    end = time.time() - start
    
    print(f"{len(image_prompts)} Done in {end:.2f}")
    print("Saving the generated images in the images folder\nSaving the Prompts, Corrected tooltips, and the images' paths in the Dalle3.csv file")
    
    save_images_configs(image_prompts, dalle_results)
    print("Done!")



if __name__ == "__main__":
    # Run the main loop
    main()
