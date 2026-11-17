import anthropic, json, os
from pathlib import Path
from prompt import EXTRACTION_PROMPT
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env", override=True)
print(os.getenv("ANTHROPIC_API_KEY")[:12])     # now after loading

client = anthropic.Anthropic()

def extract_card(title):
    try:  
        message = client.messages.create(
            model = 'claude-sonnet-4-5',
            max_tokens=1000, 
            messages = [
                {
                    'role': 'user',
                    'content': EXTRACTION_PROMPT + "\n\nTitle: " + title
                }
            ]
        )

        reply = message.content[0].text

        #parse response with json load 
        return json.loads(reply)
    except json.JSONDecodeError as e: 
        return None 
    except Exception as e: 
        print(f"Error loading API: {e}")
        return None

