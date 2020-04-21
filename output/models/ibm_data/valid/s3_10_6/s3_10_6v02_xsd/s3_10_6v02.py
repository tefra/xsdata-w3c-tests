from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional

__NAMESPACE__ = "a"


@dataclass
class T:
    """
    :ivar e1:
    :ivar e2:
    :ivar e3:
    :ivar e4:
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
    e3: Optional["T.E3"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="a",
            required=True
        )
    )
    e4: Optional["T.E4"] = field(
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
        :ivar other_attributes:
        """
        other_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##other"
            )
        )

    @dataclass
    class E2:
        """
        :ivar target_namespace_attributes:
        """
        target_namespace_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##targetNamespace"
            )
        )

    @dataclass
    class E3:
        """
        :ivar local_attributes:
        """
        local_attributes: Dict[QName, str] = field(
            default_factory=dict,
            metadata=dict(
                type="Attributes",
                namespace="##local"
            )
        )

    @dataclass
    class E4:
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
