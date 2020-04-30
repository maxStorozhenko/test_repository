def parse(query: str) -> dict:
    result = {}
    start = query.find('?')
    if start == -1 or query.endswith('?'):
        return result
    else:
        params = [i for i in query[start+1:].split('&')]
        for param in params:
            if param:
                temp = param.split('=')
                result[temp[0]] = temp[1]
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Max') == {'name': 'Max'}
    assert parse('') == {}
    assert parse('https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s&') == dict(v='some_id',
                                                                                                 list='some_list',
                                                                                                 index='6', t='0s')
    assert parse('https://www.youtube.com/watch?v=CWf6j3U9li4&list=RDCWf6j3U9li4&start_radio=1&t=1') == dict(
        v='CWf6j3U9li4', list='RDCWf6j3U9li4', start_radio='1', t='1')
    assert parse('https://www.google.com/search?q=hltv&client=ubuntu&sourceid=chrome&ie=UTF-8') == dict(q='hltv',
                                                                                                        client='ubuntu',
                                                                                                        sourceid='chrome',
                                                                                                        ie='UTF-8')
    assert parse('https://test.com.ua/?id=001&user=user1&login=user_1&client=ubuntu&') == dict(id='001', user='user1',
                                                                                               login='user_1',
                                                                                               client='ubuntu')
