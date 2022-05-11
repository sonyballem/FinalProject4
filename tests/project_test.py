'''
1. Login successful
2. Invalid email entry login
3. Wrong email entry login
4. Wrong password entry login
5. SignUp successful
6. SignUp Invalid email entry
7. SignUp passwords doesn't match
8. SignUp password Invalid
9. Missing email SignUp
10. Missing password SignUp
11. Missing email signin
12. Missing password signin
13. Dashboard page loading successful user authentication
14. Dashbaard User email entry.
15. Manage profile -> About -> post successful
16. Manage profile -> About -> edit sucessful
17. Manage Account -> Password change successful
18. Manage Account -> Email chnage successful
19. Manage profile loading successful user authentication
20. Manage Account loading successful user authentication
21. Manage Account -> Passwords doesnt match
22. Manage Account -> Password not valid
23. Manage Account -> Email not valid
24. Sudoku -> User input successful
25. Sudoku -> Solve Successful
26. Sudoku -> Authentication error
27.
'''


def test_signup(client):
   response = client.get('/register')
   assert response.status_code == 200


def test_signin(client):
   response  = client.get('/login')
   assert response.status_code == 200


def test_successful_registration(client):
    response = client.post('/register', data={'email': 'test@test.com',
                                              'password': 'Testing@1',
                                              'confirm': 'Testing@1'}, follow_redirects=True)

    assert response.status_code == 200
    assert 'Congratulations, you are now a registered user!'.encode('utf-8') in response.data


def test_check_registration(client):
     response = client.post('/register', data={'email': 'test@test.com',
                                            'password': 'Testing@1',
                                             'confirm' : 'Testing@1'}, follow_redirects=True)
     assert b'href="/register"' in response.data


def test_successful_login(client):
    response = client.post('/login', data={'email': 'test@test.com',
                                           'password': 'Testing@1'}, follow_redirects=True)
    assert response.status_code == 200
    assert 'Welcome'.encode('utf-8') in response.data


def test_bad_email_login(client):
     response = client.post('/login', data={'email': 'test@fake.com',
                                            'password': 'Testing'}, follow_redirects=True)
     assert response.status_code == 200
     assert b'href="/login"' in response.data


def test_bad_password_login(client):
     response = client.post('/login', data={'email': 'test@test.com',
                                            'password': 'odfsdfmsdl'}, follow_redirects=True)
     assert response.status_code == 200
     assert b'href="/login"' in response.data


def test_short_password_login(client):
     response = client.post('/login', data={'email': 'test@test.com',
                                            'password': 'otp'}, follow_redirects=True)
     assert response.status_code == 200
     assert 'Field must be between 6 and 35 characters'.encode('utf-8') in response.data


def test_password_match_registration(client):
     response = client.post('/register', data={'email': 'xyz@gmail.com',
                                            'password': 'Testing',
                                             'confirm' : 'random'}, follow_redirects=True)
     assert 'Passwords must match'.encode('utf-8') in response.data


def test_email_criteria_registration(client):
    response = client.post('/register', data={'email': 'xyz',
                                           'password': 'Testing@1',
                                            'confirm' : 'Testing@1'})
    assert b'href="/login"' in response.data


def test_dashboard_allow_access(client):
    response = client.post('/login', data={'email': 'test@test.com',
                                           'password': 'Testing@1'}, follow_redirects=True)
    assert 'Welcome'.encode('utf-8') in response.data


def test_dashboard_deny_access(client):

    response = client.get('/dashboard', follow_redirects=True)
    assert ' Please log in to access this page.'.encode('utf-8') in response.data

def test_profile_allow_access(client):
    response = client.post('/profile', data={'email': 'test@test.com',
                                           'password': 'Testing@1'}, follow_redirects=True)
    assert b'href="/login"' in response.data


def test_account_allow_access(client):
    response = client.post('/account', data={'email': 'test@test.com',
                                           'password': 'Testing@1'}, follow_redirects=True)
    assert b'href="/login"' in response.data