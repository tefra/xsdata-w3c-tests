from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "name"


@dataclass
class Test1:
    class Meta:
        name = "Test"

    abc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Test(Test1):
    class Meta:
        name = "test"
        namespace = "name"
