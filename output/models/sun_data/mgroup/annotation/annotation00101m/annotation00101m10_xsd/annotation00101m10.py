from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "MGroup/annotation"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "MGroup/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TheType:
    class Meta:
        name = "theType"

    c_or_date: Optional[Union[int, XmlDate]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "date",
                    "type": XmlDate,
                    "namespace": "",
                },
            ),
        },
    )
