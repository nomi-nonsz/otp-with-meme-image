# OTP with meme image

Leisure project. A REST API that sends a one-time authentication code (a.k.a OTP) to email, but the code is in the text of a meme image.

## Usage

Setup:
- Create a new `.env` file
- Add your `EMAIL_SENDER` and `EMAIL_PASSWORD` in your `.env` file
- Create or use an API test app like Postman

Usage:
- Run `main.py`
- Send a request to http://localhost:5000/send-otp with your `email`  query as email recipient. E.g: http://localhost:5000/send-top?email=your@email.com.
- If successful then a response appears like this:
    ```json
    {
        "email": {
            "body": "Here's your email confirmation",
            "receiver": "your.receiver@email.com",
            "sender": "your.sender@email.com",
            "subject": "confirm your account"
        },
        "message": "Success sending email",
        "status": 200
    }
    ```
- Now if you look at the recipient's email, it will be the image that was sent:

    ![Example Outpus](./docs/example.png)

## Why this meme?

The meme used in this project is Shannon Smiling or better known as *The Guy Smiling And Wearing A Suit*, which is often paired with a negative text or _"My Reaction For That Information"_.

![Guy with suit](./docs/guy-with-suit.gif)

the reason why I chose this meme was inspired by a meme where a man screenshot the OTP sender's chat and he replied by sending a photo of himself posing cool. suddenly it gave me the idea to make an OTP system by sending pictures of people posing cool with the OTP code text.

Idk why I chose the photo of Shannon smiling, it's because I think with the meme photo of Shannon in addition to making a sense of humor but also as a sign of welcome and strengthens security.