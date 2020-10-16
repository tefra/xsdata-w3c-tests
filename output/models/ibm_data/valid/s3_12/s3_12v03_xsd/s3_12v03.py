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
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )

    @dataclass
    class TypeText:
        """
        :ivar content:
        :ivar type:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class TypeNumber:
        """
        :ivar content:
        :ivar type:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Id4:
        """
        :ivar content:
        :ivar type:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[object] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class TitleType:
    """
    :ivar content:
    :ivar type:
    """
    class Meta:
        name = "titleType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
