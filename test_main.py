from main import *


def test_shortenurl1():
    assert (
        shortenurl(
            "https://infosystems.utdallas.edu/ms-information-technology/online-masters/"
        )
        == 1
    )


def test_shortenurl2():
    assert shortenurl("asdksadjkksjd393284jdasjds") == 0
