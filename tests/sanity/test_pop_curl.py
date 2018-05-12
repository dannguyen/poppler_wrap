from poppler_wrap.pop import Pop


def test_pop_curl():
    url = 'https://compciv.github.io/stash/hi.txt'
    dp = Pop('curl', '-s', '-A', "'webkitfoo'", url)
    assert dp.statement() == """curl -s -A 'webkitfoo' {}""".format(url)

    dp.run()
    assert dp.text == 'hi'
