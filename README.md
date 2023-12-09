# Citix

#### Questions:
- How to mimic the style of successful Instagram posts?
- What prompt engineering techniques can improve quality?
- How to ensure the model doesn't invent extra features?


### Answers to the questions
##### How to imitate the style of successful Instagram posts?

Firstly, what is success?
Success is my understanding in the case of an Instagram account based on real estate. This constantly live, active audience contributes to the growth of coverage of likes, comments, and sharing.

The content strategy and type may differ for certain people based on characteristics: Age, profitability, etc.

In general, Instagram has different types of content:

1. <bold>__Photos__</bold>: Single or multiple images capture moments, events, or artistic compositions;
2. <bold>__Videos__</bold>: Short or long-form videos, from Stories to IGTV, entertaining or informative;
3. <bold>__Stories__</bold>: Temporary posts that last 24 hours, often used for more casual or spontaneous sharing;
4. <bold>__IGTV__</bold>: Longer videos hosted on a separate section of the app for more extended content;
5. <bold>__Reels__</bold>: Short, entertaining videos set to music, similar to TikTok;
6. <bold>__Live Streams__</bold>: Real-time broadcasts allowing interaction with followers;
7. <bold>__Captions and Comments__</bold>: Text-based content accompanying posts, fostering engagement and conversation.

When making a video like the storytelling of the house about the features of the layout, how the house was built in general, what materials were used, the reasons for the sale, and so on.

It seems to me that the caption should be as informative as possible, indicating factual data, indicating the price if necessary.

Sometimes some data can turn off the attractiveness of customers, which leads to a decrease in interest, and most importantly, their changes can influence the decisions of potential buyers, so you don’t have to indicate what to avoid, or you can write pragmatically what plus we can get in return.

The advantages that the AI indicated do not always suit the lifestyle of local people, and the weather may not be suitable, so it is worth paying attention to this.

The Caption usually should not be large, if the whole essence is superimposed in the video (meaning storytelling, emotions, comments), there is no need to present it to people in writing again, it is better to have factual data after the first paragraph (optional).




##### What operational design techniques can improve quality?
##### How to ensure that the model does not invent additional functions?

1. Clear and specific <bold>__requirements and tips__</bold>. It is advisable to describe what follows from the model without grammatical errors. Include relevant details, context, or specific instructions for operating the model. For example, do not use different emotions separately, clearly and indicate the parameters of the house that should be in the text, etc.;
2. The <bold>__structure and format__</bold> of the generated text, which may indicate the order of verification information;
3. The <bold>__emotional state__</bold> of the text, which can be indicated, should be pragmatic, and cheerful;
4. Give an <bold>__example of the text__</bold> so that the model matches the style and type to get
nicely generated text;
5. You can <bold>__poke and tweak parameters__</bold> like temperature, max_tokens, or top_p to influence the output style, length, or variety of generated text.

Common parameters to fine-tune:
- Temperature. Lower temperatures produce more conservative and safer reactions. Higher temperatures produce more varied and creative results;
- Maximum number of tokens: affects the length of the generated text. Lower values produce shorter responses, and higher values produce longer responses;
- Top-p: Affects the variety and range of options the model has when generating text. Lower values make the model more conservative, while higher values make it more diverse.



##### Thoughts on using DALL-E for an Instagram real estate account

Generating images for Instagram content is a great idea because it arouses the interest of those watching, sometimes this creates an incentive to leave a comment, like, or even share with loved ones, which contributes to the large reach of the account and post.

In general, we cannot blindly submit a certain prompt and wait for the “desired” result; of course, we will need to change some parts of the generated image, add some objects, and try to regenerate according to the prompt.

I decided to write certain pre-prepared routines for holidays, so that when the script is launched, asynchronously sends requests to the server, and saves the resulting images in a folder called “generated”, this folder is automatically created if the node does not have one.

It is very important to understand and follow the trend (this does not need to be observed in all cases, but mostly yes).



#### Evaluation criteria:
- Working code, only needing .env file addition for evaluation;
- Code clarity and readability;
- Quality of generated ad descriptions.


