# generated by datamodel-codegen:
#   filename:  iscc-all.yaml
#   timestamp: 2022-01-05T15:46:55+00:00

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field


class IsccCrypto(BaseModel):
    """
    Cryptography related ISCC Metadata
    """

    datahash: Optional[str] = Field(
        None,
        description=(
            "A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default"
            " blake3)."
        ),
        x_iscc_context="http://purl.org/iscc/terms/#datahash",
    )
    metahash: Optional[str] = Field(
        None,
        description=(
            "A [Multihash](https://multiformats.io/multihash/) of the supplied metadata (default"
            " blake3). For deterministic results [JSC"
            " RFC5452](https://datatracker.ietf.org/doc/html/rfc8785) canonicalization is applied"
            " before hashing."
        ),
        x_iscc_context="http://purl.org/iscc/terms/#metahash",
    )
    tophash: Optional[str] = Field(
        None,
        description=(
            "A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of"
            " metahash and datahash (default blake3)."
        ),
        x_iscc_context="http://purl.org/iscc/terms/#tophash",
    )


class IsccTechnical(BaseModel):
    """
    Technical ISCC Metadata automaticaly inferred from the *digital content* by an ISCC Processor
    """

    created: Optional[datetime] = Field(
        None,
        description="Datetime the ISCC was created for the item.",
        x_iscc_context="http://schema.org/dateCreated",
    )
    filename: Optional[str] = Field(
        None,
        description=(
            "Filename of the referenced **digital content** (automatically used as fallback if the"
            " `name` field was not specified for ISCC processing)"
        ),
        x_iscc_context="http://purl.org/iscc/terms/#filename",
    )
    filesize: Optional[int] = Field(
        None,
        description="File size of media asset in number of bytes.",
        x_iscc_context="http://schema.org/fileSize",
    )
    mediatype: Optional[str] = Field(
        None,
        description=(
            "An [IANA Media Type](https://www.iana.org/assignments/media-types/media-types.xhtml)"
            " (MIME type)"
        ),
        example="image/png",
        x_iscc_context="http://schema.org/encodingFormat",
    )
    duration: Optional[int] = Field(
        None,
        description="Duration of audio-visual media in secondes.",
        x_iscc_context="http://schema.org/duration",
    )
    fps: Optional[float] = Field(
        None,
        description="Frames per second of video assets.",
        example=24,
        ge=1.0,
        x_iscc_context="http://purl.org/iscc/terms/#fps",
    )
    width: Optional[int] = Field(
        None,
        description="Width of visual media in number of pixels.",
        example=640,
        x_iscc_context="http://purl.org/iscc/terms/#width",
    )
    height: Optional[int] = Field(
        None,
        description="Height of visual media in number of pixels.",
        example=480,
        ge=1.0,
        x_iscc_context="http://purl.org/iscc/terms/#height",
    )
    characters: Optional[int] = Field(
        None,
        description="Number of text characters (code points after Unicode normalization)",
        example=55689,
        x_iscc_context="http://purl.org/iscc/terms/#characters",
    )
    pages: Optional[int] = Field(
        None,
        description="Number of pages (for paged documents only)",
        example=77,
        x_iscc_context="http://schema.org/numberOfPages",
    )
    language: Optional[List[str]] = Field(
        None,
        description="Language(s) of content [BCP 47](https://tools.ietf.org/search/bcp47).",
        example="en-US",
        x_iscc_context="http://schema.org/inLanguage",
    )
    parts: Optional[List[str]] = Field(
        None,
        description=(
            "Indicates items that are part of this item via Content-Codes (inverse-property"
            " belongs)."
        ),
        x_iscc_context="http://purl.org/iscc/terms/#parts",
    )
    part_of: Optional[List[str]] = Field(
        None,
        description="Indicates that this item is part of other items via their Content-Code.",
        x_iscc_context="http://purl.org/iscc/terms/#part_of",
    )
    features: Optional[List[Dict[str, Any]]] = Field(
        None,
        description="Granular features of the *digital content*.",
        x_iscc_context="http://purl.org/iscc/terms/#features",
    )


class IsccProperties(BaseModel):
    """
    Arbitrary properties. Values may be strings, numbers, object or arrays. Should be used for industry specific structured metadata.
    """

    properties: Optional[Dict[str, Any]] = Field(
        None,
        description=(
            "JSON or JSON-LD formated values about the identified *digital content*. Compatible"
            " with [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155)."
        ),
        x_iscc_context="http://purl.org/iscc/terms/#properties",
    )


class IsccExtended(BaseModel):
    """
    Extended ISCC Metadata
    """

    content: Optional[AnyUrl] = Field(
        None,
        description="URI of the *digital content* that was used to create this ISCC.",
        x_iscc_context="http://schema.org/contentUrl",
    )
    creator: Optional[List[str]] = Field(
        None,
        description="An entity primarily responsible for making the resource.",
        x_iscc_context="http://schema.org/creator",
    )
    keywords: Optional[str] = Field(
        None,
        description=(
            "Keywords or tags used to describe this content. Multiple entries in a keywords list"
            " are typically delimited by commas."
        ),
        x_iscc_context="http://schema.org/keywords",
    )
    identifier: Optional[List[AnyUrl]] = Field(
        None,
        description=(
            "Other identifier(s) referencing the work, product or other abstraction of which the"
            " referenced **digital content** is a full or partial manifestation."
        ),
        x_iscc_context="http://schema.org/identifier",
    )
    license: Optional[AnyUrl] = Field(
        None,
        description="URI of license for the identified *digital content*.",
        x_iscc_context="http://schema.org/license",
    )
    redirect: Optional[AnyUrl] = Field(
        None,
        description=(
            "URL to which a resolver should redirect an ISCC-ID that has been minted from a"
            " declartion that includes the IPFS-hash of this metadata instance."
        ),
        x_iscc_context="http://purl.org/iscc/terms/#redirect",
    )
    previous: Optional[str] = Field(
        None,
        description="ISCC of the preceding version of this item.",
        x_iscc_context="http://purl.org/iscc/terms/#previous",
    )
    version: Optional[Union[int, str]] = Field(
        None,
        description="The version of the CreativeWork embodied by a specified resource.",
        x_iscc_context="http://schema.org/version",
    )


class IsccBasic(BaseModel):
    """
    Basic user presentable ISCC Metadata conformant with [ERC721](https://eips.ethereum.org/EIPS/eip-721)
    """

    name: Optional[str] = Field(
        None,
        description=(
            "The name or title of the intangible creation manifested by the idendified *digital"
            " content*."
        ),
        example="The Never Ending Story",
        max_length=128,
        min_length=1,
        x_iscc_context="http://schema.org/name",
    )
    description: Optional[str] = Field(
        None,
        description=(
            "Description of the *digital content* identified by the **ISCC** (used as input for"
            " Meta-Code generation). Any user presentable text string (including Markdown text)"
            " indicative of the identity  of the referent may be used."
        ),
        example="a 1984 fantasy film co-written and directed by *Wolfgang Petersen*",
        max_length=1024,
        min_length=1,
        x_iscc_context="http://schema.org/disambiguatingDescription",
    )
    image: Optional[AnyUrl] = Field(
        None,
        description=(
            "URI for a user-presentable image that serves as a preview of the *digital content*."
            " The URI may be a Data-URL [RFC2397](https://datatracker.ietf.org/doc/html/rfc2397)."
            " If **ISCC** metadata is used as NFT metadata according to"
            " [ERC-721](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) or"
            " [ERC-1155](https://ethereum.org/en/developers/docs/standards/tokens/erc-1155/) the"
            " URI should reference the actual digital content represented by the NFT."
        ),
        example="https://picsum.photos/200/300.jpg",
        x_iscc_context="http://schema.org/image",
    )


class IsccMinimal(BaseModel):
    """
    Minimal ISCC Metadata
    """

    iscc: str = Field(
        ...,
        description=(
            "An **ISCC-CODE** in canonical representation. This is the minimal required field for a"
            " valid ISCC Metadata object."
        ),
        example="ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
        max_length=60,
        min_length=15,
        regex="^ISCC:[A-Z2-7]{10,60}$",
        x_iscc_context="http://purl.org/iscc/terms/#iscc",
    )


class IsccJsonld(BaseModel):
    """
    The ISCC [JSON-LD](https://json-ld.org/) Context and [JSON Schema](https://json-schema.org/) reference
    """

    context_: Optional[AnyUrl] = Field(
        "https://purl.org/iscc/terms/",
        alias="@context",
        description="The [JSON-LD](https://json-ld.org/) Context URI for ISCC metadata.",
    )
    schema_: Optional[AnyUrl] = Field(
        "https://purl.org/iscc/schema/",
        alias="$schema",
        description="The [JSON Schema](https://json-schema.org/) URI for ISCC metadata.",
    )


class ISCC(
    IsccCrypto, IsccTechnical, IsccProperties, IsccExtended, IsccBasic, IsccMinimal, IsccJsonld
):
    """
    ISCC Metadata Schema
    """

    pass
