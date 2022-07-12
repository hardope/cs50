from twttr import shorten

def test_shorten():
     assert shorten('twitter') == 'twttr'
     assert shorten('perfection') == 'prfctn'
     assert shorten('CS50') == 'CS50'
     assert shorten('PERFECTION') == 'PRFCTN'
     assert shorten(',.;') == ',.;'