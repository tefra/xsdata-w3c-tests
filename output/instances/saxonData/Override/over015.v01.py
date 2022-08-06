from output.models.saxon_data.override.over015_xsd.mod import Doc
from output.models.saxon_data.override.over015_xsd.mod import NotaFooBar
from output.models.saxon_data.override.over015_xsd.mod import StructuredDate


obj = Doc(
    para_or_bezzle=[
        StructuredDate(
            year="2010",
            month="05",
            day="11",
            nota=NotaFooBar.FOO
        ),
        StructuredDate(
            year="2011",
            month="05",
            day="11",
            nota=NotaFooBar.BEZ
        ),
    ]
)
