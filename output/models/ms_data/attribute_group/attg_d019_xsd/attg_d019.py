from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttgRef:
    """
    :ivar att1:
    :ivar any_attributes: testing
    """

    class Meta:
        name = "attgRef"

    att1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: list[AttgRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
