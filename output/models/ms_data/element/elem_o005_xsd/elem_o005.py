from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    my_elem_1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElem_1",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    my_elem_2: Optional[int] = field(
        default=None,
        metadata={
            "name": "myElem_2",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    my_attr: Optional[str] = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        },
    )
