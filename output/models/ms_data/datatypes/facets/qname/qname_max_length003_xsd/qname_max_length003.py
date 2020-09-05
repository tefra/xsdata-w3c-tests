from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName


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
            max_length=6
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
