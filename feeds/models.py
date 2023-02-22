from django.db import models
from common.models import CommonModel
from users.models import User


# caption: 게시글 내용
# contentImg: 게시글 이미지
# likesNum: 좋아요 갯수
# reviewsNum: 댓글 갯수

# USER - foreign key
class Feed(CommonModel):
    caption = models.CharField(max_length=1000, default="")
    contentImg = models.URLField(blank=True)
    likesNum = models.PositiveIntegerField(default=0)
    reviewsNum = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.caption

    # 1:N (User:Feed), N이 ForeignKey를 가진다.
    user = models.ForeignKey(
        "users.User",
        # user가 지워졌을 때
        on_delete=models.CASCADE,  # 유저 삭제시 -> 게시글 삭제됨.
        # on_delete=models.SET_NULL, # 유저 삭제시 -> Null 이된다.
        related_name="feeds",  # revers accessor 불러올 이름(users.feed_set.all() 이거 인데 users.feeds.all() 로 바꿔서 작성할 수 있도록 처리)
    )
