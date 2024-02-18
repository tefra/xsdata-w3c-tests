from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "baseTD"


@dataclass
class Test2:
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Test(Test2):
    pass


@dataclass
class Root(Test):
    class Meta:
        name = "root"
        namespace = "baseTD"
