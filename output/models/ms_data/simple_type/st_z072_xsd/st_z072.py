from dataclasses import dataclass, field
from enum import Enum


class Mylist(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Mylist = field(
        default=Mylist.VALUE_1
    )
