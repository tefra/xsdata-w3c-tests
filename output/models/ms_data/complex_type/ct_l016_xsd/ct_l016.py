from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional


@dataclass
class FooType:
    """
    :ivar child_1:
    :ivar child_2:
    :ivar other_attributes:
    """
    class Meta:
        name = "fooType"

    child_1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    child_2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    other_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
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
        metadata=dict(
            name="fooTest",
            type="Element",
            required=True
        )
    )
