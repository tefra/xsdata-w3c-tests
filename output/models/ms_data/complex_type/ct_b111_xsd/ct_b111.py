from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    attr_test1: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrTest1",
            "type": "Attribute",
        }
    )
    attr_test2: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrTest2",
            "type": "Attribute",
        }
    )
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
