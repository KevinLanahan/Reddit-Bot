import praw
from urllib.parse import quote_plus

username = "AlphabeticalOrderBot"
password = "test"
client_id = "ERAWzCQMMX-6ozuDDU3VYg"
client_secret = "prPRsSGX8QqAHFy-2hhxlzHOMN0cJg"


def main():
##establish connection
    reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="test_bot"
    )
    subreddit = reddit.subreddit("testinggounrd4bots")
    for submission in subreddit.stream.submissions():
        process_submission(submission)



def process_submission(submission):
    
    words = submission.split()

    first_letters = [word[0].lower()for word in words if word]

    if(first_letters == sorted(first_letters)):
        reply_template = "[Your comment is in alphabetical order]"
        url_title = quote_plus(submission.title)
        reply_text = REPLY_TEMPLATE.format(url_title)
        print(f"Replying to: {submission.title}")
        submission.reply(reply_text)


if __name__ == "__main__":
    main()
