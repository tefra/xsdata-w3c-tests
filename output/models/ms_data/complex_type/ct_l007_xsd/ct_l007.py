from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar elem1:
    :ivar elem2:
    """
    class Meta:
        name = "fooType"

    elem1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    elem2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
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
