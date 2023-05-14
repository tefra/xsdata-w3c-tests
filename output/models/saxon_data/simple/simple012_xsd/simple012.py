from dataclasses import dataclass, field
from typing import List, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

__NAMESPACE__ = "http://simple012.ly/"


@dataclass
class DocType:
    class Meta:
        name = "doc-type"

    chap: List[Union[XmlDate, XmlDateTime, XmlTime]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple012.ly/",
            "min_occurs": 1,
        }
    )


@dataclass
class Doc(DocType):
    class Meta:
        name = "doc"
        namespace = "http://simple012.ly/"


@dataclass
class SubDocType(DocType):
    class Meta:
        name = "sub-doc-type"


@dataclass
class Subdoc(SubDocType):
    class Meta:
        name = "subdoc"
        namespace = "http://simple012.ly/"


@dataclass
class Book:
    class Meta:
        name = "book"
        namespace = "http://simple012.ly/"

    subdoc_or_doc: List[object] = field(
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
        }
    )
