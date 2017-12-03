prompt = '\nTell me something, and I will repeat it back to you: '
prompt += '\nEnter "q" or "Q" to end the program. '
message = ' '#没有可供比较的值时程序无法运行，因此需要给message赋一个初值，
#且这个初值是空格，符合执行while循环的条件
while message != 'q' and message != 'Q':
    message = input(prompt)
    if message != 'q' and message != 'Q':
        print('\n' + message)
