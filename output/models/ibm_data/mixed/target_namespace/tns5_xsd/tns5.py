from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class TestType:
    class Meta:
        name = "TEST_TYPE"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class X(TestType):
    class Meta:
        name = "x"

    any_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    a: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://test1",
        },
    )
