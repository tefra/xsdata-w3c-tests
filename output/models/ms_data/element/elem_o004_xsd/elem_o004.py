from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar my_elem_1:
    :ivar my_elem_2:
    :ivar my_attr:
    """
    class Meta:
        name = "fooType"

    my_elem_1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElem_1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_elem_2: Optional[int] = field(
        default=None,
        metadata={
            "name": "myElem_2",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_attr: Optional[str] = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        }
    )


@dataclass
class FooTest(FooType):
    class Meta:
        name = "fooTest"


@dataclass
class Root:
    """
    :ivar foo_test:
    """
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        }
    )
