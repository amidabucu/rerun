# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/components/text.fbs".

# You can extend this class by creating a "TextExt" class in "text_ext.py".

from __future__ import annotations

from .. import datatypes
from .._baseclasses import (
    BaseDelegatingExtensionArray,
    BaseDelegatingExtensionType,
)

__all__ = ["Text", "TextArray", "TextType"]


class Text(datatypes.Utf8):
    """A string of text, e.g. for labels and text documents."""

    # You can define your own __init__ function as a member of TextExt in text_ext.py

    # Note: there are no fields here because Text delegates to datatypes.Utf8
    pass


class TextType(BaseDelegatingExtensionType):
    _TYPE_NAME = "rerun.components.Text"
    _DELEGATED_EXTENSION_TYPE = datatypes.Utf8Type


class TextArray(BaseDelegatingExtensionArray[datatypes.Utf8ArrayLike]):
    _EXTENSION_NAME = "rerun.components.Text"
    _EXTENSION_TYPE = TextType
    _DELEGATED_ARRAY_TYPE = datatypes.Utf8Array


TextType._ARRAY_TYPE = TextArray

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(TextType())
