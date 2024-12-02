from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v06"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v06"

    el_duration: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elDuration",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
