from dataclasses import dataclass, field
from typing import Dict


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    any_attributes: Dict = field(
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
