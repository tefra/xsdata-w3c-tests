from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            length=5
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"