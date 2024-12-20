from dataclasses import dataclass, field

from output.models.saxon_data.open.open045_xsd.open045x import Alpha


@dataclass
class Beta:
    class Meta:
        name = "beta"

    w3_org_xml_1998_namespace_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    w3_org_xml_1998_namespace_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Alpha,
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": Beta,
                    "namespace": "",
                },
            ),
        },
    )
