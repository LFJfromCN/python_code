prompt = '\nTell me something, and I will repeat it back to you,'
prompt += '\nEnter "q" or "Q" to end the program. '

active = True
while active:
    message = input(prompt)

    if message == 'q' or message == 'Q':
        active = False
    else:
        print(message)
