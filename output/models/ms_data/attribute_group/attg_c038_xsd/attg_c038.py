from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar ext_foo:
    """
    class Meta:
        name = "test"

    ext_foo: Optional[int] = field(
        default=None,
        metadata=dict(
            name="extFoo",
            type="Attribute"
        )
    )


@dataclass
class Doc(Test):
    class Meta:
        name = "doc"
