from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

__NAMESPACE__ = "http://simple012.ly/"


@dataclass(kw_only=True)
class DocType:
    class Meta:
        name = "doc-type"

    chap: list[XmlDate | XmlDateTime | XmlTime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple012.ly/",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Doc(DocType):
    class Meta:
        name = "doc"
        namespace = "http://simple012.ly/"


@dataclass(kw_only=True)
class SubDocType(DocType):
    class Meta:
        name = "sub-doc-type"


@dataclass(kw_only=True)
class Subdoc(SubDocType):
    class Meta:
        name = "subdoc"
        namespace = "http://simple012.ly/"


@dataclass(kw_only=True)
class Book:
    class Meta:
        name = "book"
        namespace = "http://simple012.ly/"

    subdoc_or_doc: list[Subdoc | Doc] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "subdoc",
                    "type": Subdoc,
                },
                {
                    "name": "doc",
                    "type": Doc,
                },
            ),
        },
    )
