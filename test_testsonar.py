from testsonar import main

# initial test
def test_init():
    assert (main()) == False


def test_input():
    assert (main(1)) == True
