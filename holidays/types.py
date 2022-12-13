from dataclasses import dataclass
from typing import Optional


@dataclass
class RichText:
    """TODO."""
    text: Optional[str]
    html: Optional[str]
    markdown: Optional[str]


@dataclass
class AlternateName:
    name: str
    first_year: Optional[int]
    last_year: Optional[int]


@dataclass
class ImageInfo:
    small: str
    medium: str
    large: str


@dataclass
class Pattern:
    first_year: Optional[int]
    last_year: Optional[int]
    observed: str
    observed_html: str
    observed_markdown: str
    length: int


@dataclass
class FounderInfo:
    name: str
    url: Optional[str]
    date: Optional[str]


@dataclass
class Occurrence:
    date: str
    length: int


@dataclass
class EventSummary:
    """TODO."""
    id: str
    name: str
    url: str


@dataclass
class EventInfo(EventSummary):
    """TODO."""
    adult: bool
    alternate_names: list[AlternateName]
    hashtags: Optional[list[str]]
    image: Optional[ImageInfo]
    sources: Optional[list[str]]
    description: Optional[RichText]
    how_to_observe: Optional[RichText]
    patterns: Optional[list[Pattern]]
    occurrences: Optional[list[Occurrence]]
    founders: Optional[list[FounderInfo]]


@dataclass
class RateLimit:
    """TODO."""
    limitMonth: int
    remainingMonth: int


@dataclass
class StandardResponse:
    """TODO."""
    rateLimit: RateLimit


@dataclass
class GetEventsResponse(StandardResponse):
    """TODO."""
    adult: bool
    date: str
    timezone: str
    """TODO 2"""
    events: list[EventSummary]
    multiday_starting: Optional[list[EventSummary]]
    multiday_ongoing: Optional[list[EventSummary]]


@dataclass
class GetEventInfoResponse(StandardResponse):
    """TODO."""
    event: EventInfo


@dataclass
class SearchResponse(StandardResponse):
    """TODO."""
    query: str
    """TODO 2"""
    adult: bool
    events: list[EventSummary]