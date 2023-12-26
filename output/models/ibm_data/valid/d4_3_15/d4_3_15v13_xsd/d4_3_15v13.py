from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class RootType:
    class Meta:
        name = "rootType"

    date_ele: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dateEle",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
