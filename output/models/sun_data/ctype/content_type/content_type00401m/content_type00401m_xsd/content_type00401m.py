from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "contentType"


@dataclass
class A1:
    class Meta:
        name = "A"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "date",
                    "type": XmlDate,
                    "namespace": "",
                },
            ),
        },
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "contentType"
