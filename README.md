# msteams-auto-attender

> :warning: **This is an experimental project** This might pose security issues, if exploited. Please use with caution. Any suggestions are welcome!

## Description:
A python bot which attends your online classes on MS Teams depending on your schedule.
Our target is to make sure that the attendee is seen as a present student, we will enable the bot to answer the question given by the prof in such a manner that it is the most common answer present in the chat section. Also we will try to make the bot respond to attendance calls.

## Evaluation Criteria:

- [ ] Presentation of a working output: We will record the working of the bot while it logs in the MS Teams and attend the class.
- [ ] Foolproof responses: Try to make the responses believable.
- [ ] Fetch class schedule from Google Calendar: The bot will join the class according to the schedule from the Google Calendar.
- [ ] Messages will be sent regarding the working of bot: The bot will send a message when it joins or leaves the call along with the timestamp.

## Optional Deliverables:
- [ ] Respond to attendance: The bot will respond to the attendance by sending a message in the chat section.
- [ ] Deploy on a Windows VM.

## Tech stack:
Selenium with python to access teams on the browser.
Tesseract (if we are unable to access the messages in the chat with selenium)
