from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime


@dataclass(kw_only=True)
class Appendix:
    class Meta:
        name = "appendix"

    value: XmlDate | XmlDateTime | XmlTime = field(
        metadata={
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Chap:
    class Meta:
        name = "chap"

    value: XmlDate | XmlDateTime | XmlTime = field(
        metadata={
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    appendix_or_chap: list[Appendix | Chap] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "appendix",
                    "type": Appendix,
                },
                {
                    "name": "chap",
                    "type": Chap,
                },
            ),
        },
    )
