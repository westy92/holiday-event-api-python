from dataclasses import dataclass
from typing import List, Optional


@dataclass
class RichText:
    """Formatted Text"""
    text: Optional[str]
    """Formatted as plain text"""
    html: Optional[str]
    """Formatted as HTML"""
    markdown: Optional[str]
    """Formatted as Markdown"""


@dataclass
class AlternateName:
    """Information about an Event's Alternate Name"""
    name: str
    """An Event's Alternate Name"""
    first_year: Optional[int]
    """The first year this Alternate Name was in effect (None implies none or unknown)"""
    last_year: Optional[int]
    """The last year this Alternate Name was in effect (None implies none or unknown)"""


@dataclass
class ImageInfo:
    """Information about an Event image"""
    small: str
    """A small image"""
    medium: str
    """A medium image"""
    large: str
    """A large image"""


@dataclass
class Pattern:
    """Information about an Event's Pattern"""
    first_year: Optional[int]
    """The first year this event is observed (None implies none or unknown)"""
    last_year: Optional[int]
    """The last year this event is observed (None implies none or unknown)"""
    observed: str
    """A description of how this event is observed (formatted as plain text)"""
    observed_html: str
    """A description of how this event is observed (formatted as HTML)"""
    observed_markdown: str
    """A description of how this event is observed (formatted as Markdown)"""
    length: int
    """For how many days this event is celebrated"""


@dataclass
class FounderInfo:
    """Information about an Event Founder"""
    name: str
    """The Founder's name"""
    url: Optional[str]
    """A link to the Founder"""
    date: Optional[str]
    """The date the Event was founded"""


@dataclass
class Occurrence:
    """Information about an Event's Occurrence"""
    date: str
    """The date or timestamp the Event occurs"""
    length: int
    """The length (in days) of the Event occurrence"""


@dataclass
class EventSummary:
    """A summary of an Event"""
    id: str
    """The Event Id"""
    name: str
    """The Event Name"""
    url: str
    """The Event URL"""


@dataclass
class EventInfo(EventSummary):
    """Information about an Event"""
    adult: bool
    """Whether this Event is unsafe for children or viewing at work"""
    alternate_names: List[AlternateName]
    """The Event's Alternate Names"""
    hashtags: Optional[List[str]]
    """The Event's hashtags"""
    image: Optional[ImageInfo]
    """The Event's images"""
    sources: Optional[List[str]]
    """The Event's sources"""
    description: Optional[RichText]
    """The Event's description"""
    how_to_observe: Optional[RichText]
    """How to observe the Event"""
    patterns: Optional[List[Pattern]]
    """Patterns defining when the Event is observed"""
    occurrences: Optional[List[Occurrence]]
    """The Event Occurrences (when it occurs)"""
    founders: Optional[List[FounderInfo]]
    """The Event's founders"""


@dataclass
class RateLimit:
    """Your API plan's current Rate Limit and status. Upgrade to increase these limits."""
    limitMonth: int
    """The amount of requests allowed this month"""
    remainingMonth: int
    """The amount of requests remaining this month"""


@dataclass
class StandardResponse:
    """The API's standard response"""
    rateLimit: RateLimit
    """The API plan's current rate limit and status"""


@dataclass
class GetEventsResponse(StandardResponse):
    """The Response returned by getEvents"""
    adult: bool
    """Whether Adult entries can be included"""
    date: str
    """The Date string"""
    timezone: str
    """The Timezone used to calculate the Date's Events"""
    events: List[EventSummary]
    """The Date's Events"""
    multiday_starting: Optional[List[EventSummary]]
    """Multi-day Events that start on Date"""
    multiday_ongoing: Optional[List[EventSummary]]
    """Multi-day Events that are continuing their observance on Date"""


@dataclass
class GetEventInfoResponse(StandardResponse):
    """The Response returned by getEventInfo"""
    event: EventInfo
    """The Event Info"""


@dataclass
class SearchResponse(StandardResponse):
    """The Response returned by search"""
    query: str
    """The search query"""
    adult: bool
    """Whether Adult entries can be included"""
    events: List[EventSummary]
    """The found Events"""
