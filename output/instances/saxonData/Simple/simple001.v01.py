from output.models.saxon_data.simple.simple002_xsd.simple002 import Chap
from output.models.saxon_data.simple.simple002_xsd.simple002 import Doc
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    chap_or_appx=[
        Chap(
            section=[
                Chap.Section(
                    value="",
                    nr=1.0
                ),
                Chap.Section(
                    value="",
                    nr=2.0
                ),
                Chap.Section(
                    value="",
                    nr=float("inf")
                ),
                Chap.Section(
                    value="",
                    nr=float("inf")
                ),
            ]
        ),
        DerivedElement(
            qname="{http://simple001.ly/}appx",
            value=Chap(
                section=[
                    Chap.Section(
                        value="",
                        nr=1.0
                    ),
                    Chap.Section(
                        value="",
                        nr=2.0
                    ),
                    Chap.Section(
                        value="",
                        nr=float("inf")
                    ),
                    Chap.Section(
                        value="",
                        nr=float("inf")
                    ),
                ]
            ),
            type=None
        ),
    ]
)
