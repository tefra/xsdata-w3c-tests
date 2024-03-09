from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime


@dataclass
class Appendix:
    class Meta:
        name = "appendix"

    value: Optional[Union[XmlDate, XmlDateTime, XmlTime]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class Chap:
    class Meta:
        name = "chap"

    value: Optional[Union[XmlDate, XmlDateTime, XmlTime]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    appendix_or_chap: List[Union[Appendix, Chap]] = field(
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
