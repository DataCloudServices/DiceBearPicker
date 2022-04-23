"""
Micah style
===========

Micah style enumerations.

AUTHOR
    rafidini@GitHub

CREATED AT
    Sat. 23 Apr. 2022 14:40
"""
# External packages
from enum import Enum, auto
import typing

# Constants
NAME: str = 'micah'

# Utility
class InterfaceEnum:
    @classmethod
    def get_label(cls):
        name_enum: str = cls.__name__
        return name_enum[0].lower() + name_enum[1:]

# Style options
class Mouth(InterfaceEnum, Enum):
    null: str = auto()
    surprised: str = auto()
    laughing: str = auto()
    nervous: str = auto()
    smile: str = auto()
    sad: str = auto()
    pucker: str = auto()
    frown: str = auto()
    smirk: str = auto()

class Eyebrows(InterfaceEnum, Enum):
    null: str = auto()
    up: str = auto()
    down: str = auto()
    eyelashesUp: str = auto()
    eyelashesDown: str = auto()

class Hair(InterfaceEnum, Enum):
    null: str = auto()
    fonze: str = auto()
    mrT: str = auto()
    dougFunny: str = auto()
    mrClean: str = auto()
    dannyPhantom: str = auto()
    full: str = auto()
    turban: str = auto()
    pixie: str = auto()

class Eyes(InterfaceEnum, Enum):
    null: str = auto()
    eyes: str = auto()
    round: str = auto()
    eyesShadow: str = auto()
    smiling: str = auto()

class Nose(InterfaceEnum, Enum):
    null: str = auto()
    curve: str = auto()
    pointed: str = auto()
    tound: str = auto()

class Ears(InterfaceEnum, Enum):
    null: str = auto()
    attached: str = auto()
    detached: str = auto()

class Shirt(InterfaceEnum, Enum):
    null: str = auto()
    open: str = auto()
    crew: str = auto()
    collared: str = auto()

class Earrings(InterfaceEnum, Enum):
    null: str = auto()
    hoop: str = auto()
    stud: str = auto()

class Glasses(InterfaceEnum, Enum):
    null: str = auto()
    round: str = auto()
    square: str = auto()

class FacialHair(InterfaceEnum, Enum):
    null: str = auto()
    beard: str = auto()
    scruff: str = auto()

class BaseColor(InterfaceEnum, Enum):
    null: str = auto()
    apricot: str = auto()
    coast: str = auto()
    topaz: str = auto()
    lavender: str = auto()
    sky: str = auto()
    salmon: str = auto()
    canary: str = auto()
    calm: str = auto()
    azure: str = auto()
    seashell: str = auto()
    mellow: str = auto()
    black: str = auto()
    white: str = auto()

class EarringColor(InterfaceEnum, Enum):
    null: str = auto()
    apricot: str = auto()
    coast: str = auto()
    topaz: str = auto()
    lavender: str = auto()
    sky: str = auto()
    salmon: str = auto()
    canary: str = auto()
    calm: str = auto()
    azure: str = auto()
    seashell: str = auto()
    mellow: str = auto()
    black: str = auto()
    white: str = auto()

class EyeShadowColor(InterfaceEnum, Enum):
    null: str = auto()
    apricot: str = auto()
    coast: str = auto()
    topaz: str = auto()
    lavender: str = auto()
    sky: str = auto()
    salmon: str = auto()
    canary: str = auto()
    calm: str = auto()
    azure: str = auto()
    seashell: str = auto()
    mellow: str = auto()
    black: str = auto()
    white: str = auto()

class EyebrowColor(InterfaceEnum, Enum):
    null: str = auto()
    apricot: str = auto()
    coast: str = auto()
    topaz: str = auto()
    lavender: str = auto()
    sky: str = auto()
    salmon: str = auto()
    canary: str = auto()
    calm: str = auto()
    azure: str = auto()
    seashell: str = auto()
    mellow: str = auto()
    black: str = auto()
    white: str = auto()

class FacialHairColor(InterfaceEnum, Enum):
    null: str = auto()
    apricot: str = auto()
    coast: str = auto()
    topaz: str = auto()
    lavender: str = auto()
    sky: str = auto()
    salmon: str = auto()
    canary: str = auto()
    calm: str = auto()
    azure: str = auto()
    seashell: str = auto()
    mellow: str = auto()
    black: str = auto()
    white: str = auto()

class GlassesColor(InterfaceEnum, Enum):
    null: str = auto()
    apricot: str = auto()
    coast: str = auto()
    topaz: str = auto()
    lavender: str = auto()
    sky: str = auto()
    salmon: str = auto()
    canary: str = auto()
    calm: str = auto()
    azure: str = auto()
    seashell: str = auto()
    mellow: str = auto()
    black: str = auto()
    white: str = auto()

class HairColor(InterfaceEnum, Enum):
    null: str = auto()
    apricot: str = auto()
    coast: str = auto()
    topaz: str = auto()
    lavender: str = auto()
    sky: str = auto()
    salmon: str = auto()
    canary: str = auto()
    calm: str = auto()
    azure: str = auto()
    seashell: str = auto()
    mellow: str = auto()
    black: str = auto()
    white: str = auto()

class ShirtColor(InterfaceEnum, Enum):
    null: str = auto()
    apricot: str = auto()
    coast: str = auto()
    topaz: str = auto()
    lavender: str = auto()
    sky: str = auto()
    salmon: str = auto()
    canary: str = auto()
    calm: str = auto()
    azure: str = auto()
    seashell: str = auto()
    mellow: str = auto()
    black: str = auto()
    white: str = auto()

STYLE_OPTIONS: typing.Iterable[Enum] = [
    Mouth, Eyebrows, Hair, Eyes, Nose, Ears,
    Shirt, Earrings, Glasses, FacialHair, BaseColor,
    EarringColor, EyeShadowColor, EyebrowColor,
    FacialHairColor, GlassesColor, HairColor, ShirtColor
]
