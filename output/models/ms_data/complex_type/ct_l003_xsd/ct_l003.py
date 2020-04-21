from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooTest:
    """
    :ivar value:
    :ivar my_attr:
    """
    class Meta:
        name = "fooTest"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            white_space="collapse"
        )
    )
    my_attr: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myAttr",
            type="Attribute"
        )
    )


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
