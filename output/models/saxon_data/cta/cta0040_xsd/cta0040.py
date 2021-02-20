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
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Chap:
    class Meta:
        name = "chap"

    value: Optional[Union[XmlDate, XmlDateTime, XmlTime]] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    appendix: List[Appendix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    chap: List[Chap] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
