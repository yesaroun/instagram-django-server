from django.db import models


class CommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:     # 다른 클래스에서 상속받을 수 있도록 처리
        abstract = True     # DB에 테이블을 추가힞 않겠다.
