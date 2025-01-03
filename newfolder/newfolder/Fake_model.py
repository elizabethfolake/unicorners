def fake_predict(userage):
    if userage >= 10:
        result = "survived"
    else:
        result = "Super survived"
    return result