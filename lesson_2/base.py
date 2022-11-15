base = {
    "login": "Test_login",
    "password": "Yurec1989",
    "retype": "Yurec1989",
    "accept": True,
    "avatar": "banana",
    "address": "asqdrrrr",
    "birthday": "1989-01-10",
    "city": "sdaddqddd",
    "country": "FI",
    "currency": "EUR",
    "email": "WERTYrU@ASDFffqaffrfff",
    "gdpr_data": True,
    "gdpr_marketing": True,
    "gender": "M",
    "name": "sdfghffaffrff",
    "phone": 380529876025,
    "postcode": 12345643245,
    "product": "test",
    "surname": "uoieccccccccac",
    "trigger_codes": "casino-welcome-bonus",
    "qa": {},
    "birth_country": "DE",
    "nationality": "DE",
    "birth_name": "dasdasda",
    "birth_place": "Bavaria",
    "loss_limit": {"amount": 1000, "period": "week"},
}

v = base.get("login"), base.get("avatar"), base.get("gdpr_data"), base.get("loss_limit").get("amount")
list_v1 = list(v)

print(list_v1)

v3 = {"login": "Test_login",
       "avatar": "banana",
       "email": "WERTYrU@ASDFffqaffrfff",
       "phone": 380529876025,
       "gdpr_data": True,
       "loss_limit_amount": 1000}
v4 = dict(v3)

print(v4)

# for key, value in v3.items():
#       print(key, ':', value)

