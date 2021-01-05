from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import XmlPeriod


@dataclass
class Doc:
    class Meta:
        name = "doc"

    root: Optional[Union[XmlPeriod, str, int]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[XmlPeriod, str, int] = field(
        init=False,
        default="a",
    )
