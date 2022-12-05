# generated by datamodel-codegen:
#   filename:  iscc-all.yaml

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import Field
from iscc_schema.fields import AnyUrl
from iscc_schema.base import BaseModel


class Chain(Enum):
    """
    The blockchain on which an ISCC-CODE is declared.
    """

    PRIVATE = "PRIVATE"
    BITCOIN = "BITCOIN"
    ETHEREUM = "ETHEREUM"
    POLYGON = "POLYGON"


class IsccDeclaration(BaseModel):
    """
    Field relevant in context with public ISCC declerations
    """

    original: Optional[bool] = Field(
        None,
        description=(
            "The signee of the declaring transaction claims to be the original creator of the work"
            " manifested by the identified digital content."
        ),
        example=True,
        x_iscc_context="http://purl.org/iscc/terms/#original",
    )
    redirect: Optional[AnyUrl] = Field(
        None,
        description=(
            "URL to which an ISCC resolver should redirect the ISCC-ID. **Supports URI template"
            " `(iscc-id)`**"
        ),
        example="https://example.com/land-here-when-resolving-iscc-id",
        x_iscc_context="http://purl.org/iscc/terms/#redirect",
    )
    chain: Optional[Chain] = Field(
        None,
        description="The blockchain on which an ISCC-CODE is declared.",
        example="ETHEREUM",
        x_iscc_context="http://purl.org/iscc/terms/#chain",
    )
    wallet: Optional[str] = Field(
        None,
        description="The wallet-address that signs an ISCC declaration.",
        example="0xb794f5ea0ba39494ce839613fffba74279579268",
        x_iscc_context="http://purl.org/iscc/terms/#wallet",
    )
    verifications: Optional[List[Dict[str, Any]]] = Field(
        None,
        description=(
            "A list of self-verifications. Self-verifications are public URLs under the"
            " account/authority of the signee. The verification URL must respond to a GET request"
            " with text that contains a multihash of the ISCC declaration signees wallet address in"
            " the format of `verify:<multihash-of-wallet-address>:verify`."
        ),
        example=[{"url": "https://twitter.com/titusz/status/1490104312051257347"}],
        max_items=128,
        x_iscc_context="http://purl.org/iscc/terms/#verifications",
    )


class IsccCrypto(BaseModel):
    """
    Cryptography related ISCC Metadata
    """

    tophash: Optional[str] = Field(
        None,
        description=(
            "A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of"
            " metahash and datahash (default blake3)."
        ),
        example="bdyqnosmb56tqudeibogyygmf2b25xs7wpg4zux4zcts2v6llqmnj4ja",
        min_length=40,
        x_iscc_context="http://purl.org/iscc/terms/#tophash",
    )
    metahash: Optional[str] = Field(
        None,
        description=(
            "A [Multiformats](https://multiformats.io) multihash or IPFS CIDv1 of the supplied"
            " metadata. The hash is created from `name` and `description` fields or `meta` if"
            " supplied."
        ),
        example="f01551220b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9",
        min_length=40,
        x_iscc_context="http://purl.org/iscc/terms/#metahash",
    )
    datahash: Optional[str] = Field(
        None,
        description=(
            "A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default"
            " blake3)."
        ),
        example="bdyqk6e2jxh27tingubae32rw3teutg6lexe23qisw7gjve6k4qpteyq",
        min_length=40,
        x_iscc_context="http://purl.org/iscc/terms/#datahash",
    )


class IsccNft(BaseModel):
    """
    Metadata for NFT Marketplaces
    """

    external_url: Optional[AnyUrl] = Field(
        None,
        description=(
            "This is the URL that will appear below the asset's image on some NFT Marketplaces and"
            " will allow users to leave the site and view the item on your site. **Supports URI"
            " template `(iscc-id)`**."
        ),
        x_iscc_context="http://purl.org/iscc/terms/#external_url",
    )
    animation_url: Optional[AnyUrl] = Field(
        None,
        description="A URL to a multi-media attachment for the item.",
        x_iscc_context="http://purl.org/iscc/terms/#animation_url",
    )
    properties: Optional[Dict[str, Any]] = Field(
        None,
        description=(
            "Arbitrary properties. Values may be strings, numbers, object or arrays. Properties"
            " defined here may show up on NFT marketplaces. See"
            " [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155#metadata)"
        ),
        example={
            "simple_property": "example value",
            "rich_property": {
                "name": "Name",
                "value": "123",
                "display_value": "123 Example Value",
                "class": "emphasis",
                "css": {"color": "#ffffff", "font-weight": "bold", "text-decoration": "underline"},
            },
            "array_property": {"name": "Name", "value": [1, 2, 3, 4], "class": "emphasis"},
        },
        x_iscc_context="http://purl.org/iscc/terms/#properties",
    )
    attributes: Optional[List[Dict[str, Any]]] = Field(
        None,
        description=(
            "Similar to `properties` but as an array of objects. These attributes will show up on"
            " some NFT marketplaces."
        ),
        example=[
            {"trait_type": "METAL", "value": "SILVER"},
            {"display_type": "number", "trait_type": "GENERATION", "value": 1},
        ],
        x_iscc_context="http://purl.org/iscc/terms/#attributes",
    )
    nft: Optional[AnyUrl] = Field(
        None,
        description=(
            "A unique URI for a non-fungible token of the identified content. The URI must contain"
            " references to the blockchain, smart-contract and token. The recommended schemes are"
            " [CAIP-22](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-22.md) and"
            " [CAIP-29](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-29.md)."
        ),
        example="eip155:1/erc721:0x06012c8cf97BEaD5deAe237070F9587f8E7A266d/771769",
        x_iscc_context="http://purl.org/iscc/terms/#nft",
    )


class Mode(Enum):
    """
    The perceptual mode used to create the ISCC-CODE.
    """

    text = "text"
    image = "image"
    audio = "audio"
    video = "video"
    mixed = "mixed"


class IsccTechnical(BaseModel):
    """
    Technical ISCC Metadata automaticaly inferred from the *digital content* by an ISCC Processor
    """

    mode: Optional[Mode] = Field(
        None, description="The perceptual mode used to create the ISCC-CODE.", example="video"
    )
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
    language: Optional[Union[str, List[str]]] = Field(
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
    generator: Optional[str] = Field(
        None,
        description="Name and version of the software that generated the ISCC",
        x_iscc_context="http://purl.org/iscc/terms/#generator",
    )
    thumbnail: Optional[AnyUrl] = Field(
        None,
        description=(
            "URI an autogenerated user-presentable thumbnail-image that serves as a preview of the"
            " digital content. The URI may be a Data-URL RFC2397."
        ),
        example="https://picsum.photos/200/300.jpg",
        x_iscc_context="http://schema.org/thumbnailUrl",
    )


class IsccExtended(BaseModel):
    """
    Extended ISCC Metadata
    """

    media_id: Optional[str] = Field(
        None,
        description="Vendor specific (internal) identifier for the source media file.",
        example="05VQ3BGTGFCJA",
        x_iscc_context="http://schema.org/identifier",
    )
    iscc_id: Optional[str] = Field(
        None,
        description="The **ISCC-ID** of the digital content in canonical representation.",
        example="ISCC:MAACAJINXFXA2SQX",
        max_length=73,
        min_length=15,
        regex="^ISCC:[A-Z2-7]{10,73}$",
        x_iscc_context="http://schema.org/identifier",
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
    identifier: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "Other identifier(s) referencing the work, product or other abstraction of which the"
            " referenced **digital content** is a full or partial manifestation."
        ),
        x_iscc_context="http://schema.org/identifier",
    )
    content: Optional[AnyUrl] = Field(
        None,
        description="URI of the *digital content* that was used to create this ISCC.",
        x_iscc_context="http://schema.org/contentUrl",
    )
    keywords: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "Keywords or tags used to describe this content. Either a list of keywords or a sting"
            " with comma separated keywords."
        ),
        x_iscc_context="http://schema.org/keywords",
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


class IsccEmbeddable(BaseModel):
    """
    Metadata intended to be embedded into the media asset.
    """

    creator: Optional[Union[str, List[str]]] = Field(
        None,
        description="An entity primarily responsible for making the resource.",
        example="Joanne K. Rowling",
        x_iscc_context="http://schema.org/creator",
    )
    license: Optional[AnyUrl] = Field(
        None,
        description="URI of license for the identified *digital content*.",
        example="https://example.com/license-terms-for-this-item",
        x_iscc_context="http://schema.org/license",
    )
    acquire: Optional[AnyUrl] = Field(
        None,
        description=(
            "This field must contain a valid URL referring to a page showing information about how"
            " one can acquire a license for the item. This may be a page of a web shop or NFT"
            " marketplace ready for providing a license."
        ),
        example="https://example.com/buy-license-for-item-here",
        x_iscc_context="http://schema.org/acquireLicensePage",
    )
    credit: Optional[str] = Field(
        None,
        description=(
            "A line of text that you expect users of the image (such as Google Images) to display"
            " alongside the image."
        ),
        example="Frank Farian - Getty Images",
        x_iscc_context="http://schema.org/creditText",
    )
    rights: Optional[str] = Field(
        None,
        description=(
            "Contains any necessary copyright notice and should identify the current owner of the"
            " copyright of this work with associated intellectual property rights."
        ),
        example="© Copyright 2022 ISCC Foundation - www.iscc.codes",
        x_iscc_context="http://schema.org/copyrightNotice",
    )


class IsccBasic(BaseModel):
    """
    Basic user presentable ISCC Metadata essential for Meta-Code and Meta-Hash generation.
    """

    name: Optional[str] = Field(
        None,
        description=(
            "The title or name of the intangible creation manifested by the identified *digital"
            " content*. **Used as input for ISCC Meta-Code generation**."
        ),
        example="The Never Ending Story",
        max_length=128,
        x_iscc_context="http://schema.org/name",
    )
    description: Optional[str] = Field(
        None,
        description=(
            "Description of the *digital content* identified by the **ISCC**. **Used as input for"
            " ISCC Meta-Code generation**. Any user presentable text string (including Markdown"
            " text) indicative of the identity  of the referent may be used."
        ),
        example="a 1984 fantasy film co-written and directed by *Wolfgang Petersen*",
        max_length=4096,
        x_iscc_context="http://schema.org/disambiguatingDescription",
    )
    meta: Optional[str] = Field(
        None,
        description="Subject, industry, or use-case specific metadata encoded as Data-URL.",
        example="data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0=",
        max_length=16384,
        x_iscc_context="http://purl.org/iscc/terms/#meta",
    )


class IsccMinimal(BaseModel):
    """
    Minimal required ISCC Metadata
    """

    iscc: Optional[str] = Field(
        None,
        description=(
            "An **ISCC-CODE** in canonical representation. This is the minimal required field for a"
            " valid ISCC Metadata object."
        ),
        example="ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
        max_length=73,
        min_length=15,
        regex="^ISCC:[A-Z2-7]{10,73}$",
    )


class Type(Enum):
    """
    The type of digital content according to schema.org classes (TextDigitalDocument, ImageObject, AudioObject, VideoObject).
    """

    CreativeWork = "CreativeWork"
    TextDigitalDocument = "TextDigitalDocument"
    ImageObject = "ImageObject"
    AudioObject = "AudioObject"
    VideoObject = "VideoObject"


class IsccJsonld(BaseModel):
    """
    The ISCC [JSON-LD](https://json-ld.org/) Context and [JSON Schema](https://json-schema.org/) reference
    """

    context_: Optional[AnyUrl] = Field(
        "http://purl.org/iscc/context/0.4.1.jsonld",
        alias="@context",
        description="The [JSON-LD](https://json-ld.org/) Context URI for ISCC metadata.",
    )
    type_: Optional[Type] = Field(
        "CreativeWork",
        alias="@type",
        description=(
            "The type of digital content according to schema.org classes (TextDigitalDocument,"
            " ImageObject, AudioObject, VideoObject)."
        ),
    )
    schema_: Optional[AnyUrl] = Field(
        "http://purl.org/iscc/schema/0.4.1.json",
        alias="$schema",
        description="The [JSON Schema](https://json-schema.org/) URI for ISCC metadata.",
        x_iscc_context="http://purl.org/iscc/terms/#$schema",
    )


class IsccMeta(
    IsccDeclaration,
    IsccCrypto,
    IsccNft,
    IsccTechnical,
    IsccExtended,
    IsccEmbeddable,
    IsccBasic,
    IsccMinimal,
    IsccJsonld,
):
    """
    ISCC Metadata Schema
    """

    pass
