from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Regex:
    att: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: list[Regex] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
