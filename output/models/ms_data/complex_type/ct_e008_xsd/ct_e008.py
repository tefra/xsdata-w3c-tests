from dataclasses import dataclass, field
from typing import Dict


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
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
