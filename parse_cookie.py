def parse_cookie(query):
    result = {}
    if not query:
        return result
    else:
        cookies = [i for i in query.split(';')]
        for cookie in cookies:
            if cookie:
                divider = cookie.find('=')
                result[cookie[:divider]] = cookie[divider+1:]
        return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=value;expires=date;path=path;domain=domain_name;') == dict(name='value', expires='date',
                                                                                         path='path',
                                                                                         domain='domain_name')
    assert parse_cookie('CUSTOMER=WILE_E_COYOTE;PART_NUMBER=ROCKET_LAUNCHER_0001') == dict(CUSTOMER='WILE_E_COYOTE',
                                                                                           PART_NUMBER='ROCKET_LAUNCHER_0001')
    assert parse_cookie('user=John;path=/;expires=Tue;') == {'user': 'John', 'path': '/', 'expires': 'Tue'}
    assert parse_cookie('name=h_city;value=dp;domain=.ithillel.ua') == dict(name='h_city', value='dp',
                                                                            domain='.ithillel.ua')
    assert parse_cookie('name=dotcom_user;value=maxStorozhenko') == {'name': 'dotcom_user', 'value': 'maxStorozhenko'}
    assert parse_cookie('name=_gat;value=1;domain=.codewars.com') == dict(name='_gat', value='1',
                                                                          domain='.codewars.com')
