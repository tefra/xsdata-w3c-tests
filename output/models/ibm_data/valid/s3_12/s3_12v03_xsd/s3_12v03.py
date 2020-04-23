from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xstest-tns"


@dataclass
class Root:
    """
    :ivar title:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    title: List[Union["Root.TypeText", "Root.TypeNumber", "Root.Id4"]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=5
        )
    )

    @dataclass
    class TypeText:
        """
        :ivar content:
        :ivar type:
        """
        content: Optional[object] = field(
            default=None,
            metadata=dict(
                type="Wildcard",
                namespace="##any"
            )
        )
        type: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )

    @dataclass
    class TypeNumber:
        """
        :ivar content:
        :ivar type:
        """
        content: Optional[object] = field(
            default=None,
            metadata=dict(
                type="Wildcard",
                namespace="##any"
            )
        )
        type: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )

    @dataclass
    class Id4:
        """
        :ivar content:
        :ivar type:
        """
        content: Optional[object] = field(
            default=None,
            metadata=dict(
                type="Wildcard",
                namespace="##any"
            )
        )
        type: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )


@dataclass
class TitleType:
    """
    :ivar content:
    :ivar type:
    """
    class Meta:
        name = "titleType"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
