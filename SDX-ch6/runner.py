import time

def sign(value):
    if value < 0:
        return -1
    else:
        return 1

def test_sign_negative():
    assert sign(-3) == -1

def test_sign_positive():
    assert sign(19) == 1

def test_sign_zero():
    assert sign(0) == 0

def test_sign_error():
    assert sgn(1) == 1

# [run]
def run_tests():
    startAll = endAll = startOne = endOne = None
    results = {"pass": [], "fail": [], "error": []}
    startAll = time.time()
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            if 'setup' in globals(): setup()
            startOne = time.time()
            test()
            results["pass"].append(test, time)
        except AssertionError:
            results["fail"].append(test)
        except Exception:
            results["error"].append(test)
        finally:
            endOne = time.time()
            print(endOne-startOne, test.__name__)
            if 'teardown' in globals(): teardown()
    
    print("-----------")           
    endAll = time.time()        
    print(endAll-startAll, "total time")
    print("-----------")       
    for key in ["pass", "fail","error"]:
        print(len(results[key]), key)
        for test in results[key]:
            print ("   ", test.__name__)
# [/run]

run_tests()
