from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Xmlns:
    """
    :ivar value:
    :ivar attr_test:
    """
    class Meta:
        name = "xmlns"

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
class Root(Xmlns):
    class Meta:
        name = "root"
