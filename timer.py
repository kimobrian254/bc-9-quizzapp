import signal, sys

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def nonBlockingRawInput(choices, prompt='', timeout=5):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        print(prompt)
        for choice, ans in choices.iteritems():
            print(choice+" : "+ans)
        text = raw_input("Answer: ")
        signal.alarm(0)
        return text
    except AlarmException:
        sys.stdout.write('\a')
        sys.stdout.flush()
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return "0"