from dataclasses import dataclass, field
from typing import List, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

__NAMESPACE__ = "http://simple013.ly/"


@dataclass
class DocType:
    class Meta:
        name = "doc-type"

    chap: List[Union[XmlDate, XmlDateTime, XmlTime]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple013.ly/",
            "min_occurs": 1,
        }
    )


@dataclass
class SubDocType:
    class Meta:
        name = "sub-doc-type"

    chap: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple013.ly/",
            "min_occurs": 1,
        }
    )


@dataclass
class Doc(DocType):
    class Meta:
        name = "doc"
        namespace = "http://simple013.ly/"


@dataclass
class Subdoc(SubDocType):
    class Meta:
        name = "subdoc"
        namespace = "http://simple013.ly/"


@dataclass
class Book:
    class Meta:
        name = "book"
        namespace = "http://simple013.ly/"

    subdoc: List[Subdoc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    doc: List[Doc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )
