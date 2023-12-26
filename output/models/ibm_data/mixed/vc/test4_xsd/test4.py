from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TestV2:
    class Meta:
        name = "TEST_V2"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    v2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Test(TestV2):
    class Meta:
        name = "test"
