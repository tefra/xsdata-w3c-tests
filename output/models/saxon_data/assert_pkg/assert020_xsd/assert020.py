from dataclasses import dataclass, field

from output.models.saxon_data.assert_pkg.assert020_xsd.assert020a import Temp

__NAMESPACE__ = "http://assert020.ns/"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://assert020.ns/"

    temp: list[Temp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
