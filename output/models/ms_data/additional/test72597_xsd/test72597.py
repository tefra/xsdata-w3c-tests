from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class A:
    """
    :ivar part:
    """
    part: List["A.Part"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="foo",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Part:
        """
        :ivar value:
        :ivar number:
        :ivar number2:
        """
        value: Optional[str] = field(
            default=None,
        )
        number: Optional[int] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )
        number2: Optional[int] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )


@dataclass
class Root:
    """
    :ivar a:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    a: Optional[A] = field(
        default=None,
        metadata=dict(
            name="A",
            type="Element",
            required=True
        )
    )
