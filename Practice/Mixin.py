import json

#Mixin - це клас
class JsonSerializerMixin():
    import json
    def to_json(self):
        return json.dumps(self.__dict__, default=str, ensure_ascii=False)


class TimeMixin:
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        from datetime import datetime
        self.created_at = datetime.now()

class User(JsonSerializerMixin, TimeMixin):
    def __init__(self, username, email, password: str):
        super().__init__()
        self.username = username
        self.email = email
        self.password = password

u = User(username="Олександр")
print(u.to_json())