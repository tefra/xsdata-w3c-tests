from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class AttgRef:
    """
    :ivar att1:
    :ivar any_attributes: testing
    """

    class Meta:
        name = "attgRef"

    att1: None | int = field(
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


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: list[AttgRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 10,
        },
    )
