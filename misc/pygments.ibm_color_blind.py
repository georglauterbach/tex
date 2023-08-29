# Custom IBM Color Blind theme for usage with the Minted package.
#
# This file is parsed into out/_minted-main/*.pygstyle and based on a
# Pygments style in /usr/lib/python3/dist-packages/pygments/styles/*.

from pygments.style import Style
from pygments.token import \
  Keyword, Name, Comment, String, Error, \
  Number, Operator, Generic, Whitespace

class IBMColorBlindStyle(Style):
    default_style = ""

    styles = {
        Whitespace:                "#bbbbbb",

        Comment:                   "#888",
        Comment.Preproc:           "#FE6100",
        Comment.Special:           "bold #888",

        Keyword:                   "#648FFF",
        Keyword.Pseudo:            "#648FFF",
        Keyword.Type:              "#648FFF",

        Operator:                  "#DC267F",
        Operator.Word:             "bold #DC267F",

        Name.Builtin:              "#648FFF",
        Name.Function:             "#785EF0",
        Name.Class:                "bold #648FFF",
        Name.Namespace:            "bold #648FFF",
        Name.Exception:            "bold #648FFF",
        Name.Variable:             "#DC267F",
        Name.Variable.Instance:    "#DC267F",
        Name.Variable.Class:       "#369",
        Name.Variable.Global:      "bold #d70",
        Name.Constant:             "#648FFF",
        Name.Label:                "bold #970",
        Name.Entity:               "bold #800",
        Name.Attribute:            "#785EF0",
        Name.Tag:                  "#070",
        Name.Decorator:            "bold #555",

        String:                    "#FFB000",
        String.Char:               "#FFB000 bg:",
        String.Doc:                "#FFB000 bg:",
        String.Interpol:           "bg:#FFB000",
        String.Escape:             "bold #FFB000",
        String.Regex:              "bg:#FFB000 #000",
        String.Symbol:             "#FFB000 bg:",
        String.Other:              "#FFB000",

        Number:                    "#FFB000",
        Number.Integer:            "#FFB000",
        Number.Float:              "#FFB000",
        Number.Hex:                "#FFB000",
        Number.Oct:                "#FFB000",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#00A000",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #c65d09",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "#F00 bg:#FEE"
    }
