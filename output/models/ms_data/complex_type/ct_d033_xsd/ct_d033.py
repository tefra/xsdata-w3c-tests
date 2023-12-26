from dataclasses import dataclass, field
from typing import Dict


@dataclass
class MyType:
    class Meta:
        name = "myType"

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
class FooType(MyType):
    class Meta:
        name = "fooType"

    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
