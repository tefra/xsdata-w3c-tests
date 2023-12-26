from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "compositor"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "compositor"

    date_or_time: Optional[Union[XmlDate, XmlTime]] = field(
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
                    "name": "time",
                    "type": XmlTime,
                    "namespace": "",
                },
            ),
        },
    )
