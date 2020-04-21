from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://foo.com"


@dataclass
class Root:
    """
    :ivar child:
    """
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    child: List["Root.Child"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=3,
            max_occurs=7
        )
    )

    @dataclass
    class Child:
        """
        :ivar value:
        :ivar attr:
        """
        value: Optional[str] = field(
            default=None,
            metadata=dict(
                min_length=3.0,
                max_length=10.0
            )
        )
        attr: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                min_length=5.0,
                max_length=10.0
            )
        )
