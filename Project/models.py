import decimal
from dataclasses import dataclass


@dataclass
class Item:
    num: str
    name_804: str
    name_provider: str
    provider: str
    cost: decimal.Decimal
    article: str | None = None
    img: str | None = None
    size: str | None = None
    link: str | None = None
