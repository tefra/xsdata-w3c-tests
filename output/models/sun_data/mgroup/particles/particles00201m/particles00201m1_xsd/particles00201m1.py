from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "particles"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    date_or_marked: Optional[Union[XmlDate, bool]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "date",
                    "type": XmlDate,
                    "namespace": "",
                },
                {
                    "name": "marked",
                    "type": bool,
                    "namespace": "",
                },
            ),
        },
    )
