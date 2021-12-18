from borisov_dmitrii import dates


def test_is_date():
    assert dates.is_date("20200101") == True, "is_date != True for '20200101'"
    assert dates.is_date("20201313") == False, "is_date != False for '20201313'"
    assert dates.is_date("20200229") == True, "is_date != True for '20200229'"
    assert dates.is_date("20210229") == False, "is_date != False for '20210229'"


def test_add_days():
    assert dates.add_days("20200401", 5) == "20200406", "add_days('20200401', 5) != '20200406'"
    assert dates.add_days("20200401", 0) == "20200401", "add_days('20200401', 0) != '20200401'"
    assert dates.add_days("20200401", -2) == "20200330", "add_days('20200401', -2) != '20200330'"
    assert dates.add_days("20200401", 365 * 2) == "20220401", "add_days('20200401', 365*2) != '20220401'"
    assert dates.add_days("20200401", -365 * 2) == "20180402", "add_days('20200401', -365 * 2) != '20180402'"


def test_tomorrow():
    assert dates.tomorrow("20200401") == "20200402", "tomorrow('20200401') != '20200402'"
    assert dates.tomorrow("20200331") == "20200401", "tomorrow('20200331') != '20200401'"
    assert dates.tomorrow("20201231") == "20210101", "tomorrow('20201231') != '20210101'"
    assert dates.tomorrow("20200228") == "20200229", "tomorrow('20200228') != '20200229'"
    assert dates.tomorrow("20200229") == "20200301", "tomorrow('20200229') != '20200301'"


def test_yesterday():
    assert dates.yesterday("20200402") == "20200401", "yesterday('20200402') != '20200401'"
    assert dates.yesterday("20200401") == "20200331", "yesterday('20200401') != '20200331'"
    assert dates.yesterday("20210101") == "20201231", "yesterday('20210101') != '20201231'"
    assert dates.yesterday("20200229") == "20200228", "yesterday('20200229') != '20200228'"
    assert dates.yesterday("20200301") == "20200229", "yesterday('20200301') != '20200229'"


def test_add_weeks():
    assert dates.add_weeks("20200401", 3) == "20200422", "add_weeks('20200401') != '20200422'"
    assert dates.add_weeks("20200401", 0) == "20200401", "add_weeks('20200401') != '20200401'"
    assert dates.add_weeks("20200401", -5) == "20200226", "add_weeks('20200401', -5) != '20200226'"
    assert dates.add_weeks("20200401", 52) == "20210331", "add_weeks('20200401', 52) != '20210331'"
    assert dates.add_weeks("20200401", -53) == "20190327", "add_weeks('20200401', -53) != '20190327'"


def test_add_months():
    cases = (
        ("20200401", 1, "20200501"),
        ("20200401", 0, "20200401"),
        ("20200401", -1, "20200301"),
        ("20200428", -3, "20200128"),
        ("20200128", 3, "20200428"),
        ("20200131", 1, "20200229"),
        ("20190228", 12, "20200228"),
        ("20210228", -12, "20200228"),
        ("20200229", 12, "20210228"),
        ("20200229", -12, "20190228"),
        ("20200229", 48, "20240229"),
        ("20200229", -48, "20160229"),
    )
    for case in cases:
        assert dates.add_months(case[0], case[1]) == case[2], f"add_months('{case[0]}', {case[1]}) != '{case[2]}'"


def test_add_years():
    cases = (
        ("20200401", 1, "20210401"),
        ("20200401", 0, "20200401"),
        ("20200401", -1, "20190401"),
        ("19990401", 2, "20010401"),
        ("20000401", -3, "19970401"),
        ("20200229", 1, "20210228"),
        ("20200229", -1, "20190228"),
        ("20190228", 1, "20200228"),
        ("20210228", -1, "20200228"),
    )
    for case in cases:
        assert dates.add_years(case[0], case[1]) == case[2], f"add_months('{case[0]}', {case[1]}) != '{case[2]}'"


test_is_date()
test_yesterday()
test_tomorrow()
test_add_days()
test_add_weeks()
test_add_months()
test_add_years()