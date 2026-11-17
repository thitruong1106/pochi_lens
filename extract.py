import os, json, httpx
from pathlib import Path
from prompt import EXTRACTION_PROMPT
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

def extract_card(title):
    try:
        r = httpx.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": os.getenv("ANTHROPIC_API_KEY"),
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": "claude-sonnet-4-5",
                "max_tokens": 1000,
                "messages": [
                    {"role": "user", "content": EXTRACTION_PROMPT + "\n\nTitle: " + title}
                ],
            },
            timeout=30,
        )
        reply = r.json()["content"][0]["text"]
        if reply.startswith("```"):
            reply = reply.split("```")[1]
            if reply.startswith("json"):
                reply = reply[4:]
        reply = reply.strip()
        print("RAW REPLY:", repr(reply))          # ← add this
        return json.loads(reply)
    except json.JSONDecodeError:
        return None
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        return None