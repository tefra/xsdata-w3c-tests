from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "MGroupDef/annotation"


@dataclass
class A:
    c: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "MGroupDef/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
