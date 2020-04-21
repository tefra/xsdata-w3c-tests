from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar value:
    :ivar attr_test:
    """
    class Meta:
        name = "fooType"

    value: Optional[str] = field(
        default=None,
    )
    attr_test: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest",
            type="Attribute"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
