def check_if_in_db(data: str, db):
    return True if data.lower() in [i.lower() for i in db] else False
