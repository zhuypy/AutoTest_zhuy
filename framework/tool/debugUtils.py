import traceback
def getTracebackInfo():
    return traceback.format_exc()

if __name__ == '__main__':
    try:
        assert 1==2
    except AssertionError:
        print(getTracebackInfo())