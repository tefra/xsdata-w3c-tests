from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.publishing.org"


@dataclass
class B:
    """
    :ivar b:
    :ivar id:
    """
    class Meta:
        name = "b"
        namespace = "http://www.publishing.org"

    b: Optional["B"] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar keys:
    :ivar keyref:
    """
    class Meta:
        name = "root"
        namespace = "http://www.publishing.org"

    keys: Optional["Root.Keys"] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    keyref: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Keys:
        """
        :ivar any_element:
        """
        any_element: List[object] = field(
            default_factory=list,
            metadata=dict(
                type="Wildcard",
                namespace="##any",
                min_occurs=1,
                max_occurs=9223372036854775807
            )
        )
