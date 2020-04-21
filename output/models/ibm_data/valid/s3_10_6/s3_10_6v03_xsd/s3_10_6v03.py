from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional

__NAMESPACE__ = "a"


@dataclass
class T:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "t"

    e1: Optional["T.E1"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="a",
            required=True
        )
    )
    e2: Optional["T.E2"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="a",
            required=True
        )
    )

    @dataclass
    class E1:
        """
        :ivar any_attributes:
        """
        any_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##any"
            )
        )

    @dataclass
    class E2:
        """
        :ivar any_attributes:
        """
        any_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##any"
            )
        )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
