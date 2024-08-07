from database.models import Main
import models


class ItemsRepository:

    @classmethod
    def create(cls, item: models.Item):
        Main.objects.create(
            num=item.num,
            name_804=item.name_804,
            name_provider=item.name_provider,
            provider=item.provider,
            cost=item.cost,
            article=item.article,
            img=item.img,
            size=item.size,
            link=item.link,
        )

    @classmethod
    def delete_provider(cls, provider: str):
        Main.objects.filter(provider=provider).delete()
