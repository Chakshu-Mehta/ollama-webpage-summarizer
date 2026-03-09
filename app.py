import ollama
from scraper import fetch_website_contents


SYSTEM_PROMPT = """
You are a helpful assistant that summarizes webpage content clearly and concisely.
Focus on the main content and ignore navigation-heavy text.
Return the summary in markdown.
"""

USER_PROMPT_PREFIX = """
Here are the contents of a website.

Provide a short summary of this website.

Website content:
"""


def messages_for(website_text):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT_PREFIX + website_text},
    ]


def summarize(url):
    website_text = fetch_website_contents(url)

    response = ollama.chat(
        model="llama3.2",
        messages=messages_for(website_text)
    )

    return response["message"]["content"]


def main():
    url = input("Enter webpage URL: ").strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        print("Please enter a valid URL starting with http:// or https://")
        return

    try:
        summary = summarize(url)
        print("\n------ SUMMARY ------\n")
        print(summary)
    except Exception as e:
        print(f"\nError: {e}")
        print("This website may be blocking automated requests. Try another URL.")


if __name__ == "__main__":
    main()