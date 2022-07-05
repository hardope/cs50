from seasons import check_date

def test_check():
     assert check_date('2022-03-04') == ('2022', '03', '04')
     assert check_date('2022-03-03') == ('2022','03','03')
     assert check_date('2022-051-21') == None
     assert check_date('June 3, 2309') == None