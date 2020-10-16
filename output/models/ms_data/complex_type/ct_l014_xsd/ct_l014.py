from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar child_1:
    :ivar child_2:
    :ivar my_attr:
    """
    class Meta:
        name = "fooType"

    child_1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    child_2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_attr: Optional[int] = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
            "required": True,
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
