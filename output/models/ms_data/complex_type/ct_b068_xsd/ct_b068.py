from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    my_element_or_my_ele2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "myElement",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "myEle2",
                    "type": str,
                    "namespace": "",
                },
            ),
        }
    )
    attr_test: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        }
    )
    attr_test2: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest2",
            "type": "Attribute",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
