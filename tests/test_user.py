from sqlalchemy.exc import IntegrityError

def test_user_model(user, database):
    test_username = "student4"
    test_email = "student4@fylebe.com"

    test_user = user(username=test_username, email=test_email)
    database.session.add(test_user)
    database.session.commit()

    expected = "<User 'student4'>"

    assert test_user == user.get_by_email(test_email)
    assert repr(test_user) == expected

def test_author_no_email(user,database):
    test_username = "student4"
    test_email = "student4@fylebe.com"

    test_user = user(username=test_username, email=test_email)
    
    
    database.session.add(test_user)
    try:
        database.session.commit()
    except IntegrityError:
        database.session.rollback()
