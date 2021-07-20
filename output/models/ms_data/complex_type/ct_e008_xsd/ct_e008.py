from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    value: Optional[str] = field(
        default=None
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
