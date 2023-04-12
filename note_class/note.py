"""Note stuff"""

POSITIONS = {
    "A" :  0,
    "A#":  1,
    "Bb":  1,
    "B" :  2,
    "C" :  3,
    "C#":  4,
    "Db":  4,
    "D" :  5,
    "D#":  6,
    "Eb":  6,
    "E" :  7,
    "F" :  8,
    "F#":  9,
    "Gb":  9,
    "G" : 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0:  ["A"],
    1:  ["A#", "Bb"],
    2:  ["B"],
    3:  ["C"],
    4:  ["C#", "Db"],
    5:  ["D"],
    6:  ["D#", "Eb"],
    7:  ["E"],
    8:  ["F"],
    9:  ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


class Note:
    """A note in the 12-tone chromatic scale.
    
    Attributes:
        position (int): a value between 0 and 11.
        perspective (str or None): "#" if we're viewing the note from a sharp
            perspective, "b" if we're viewing the note from a flat perspective,
            or None if we are being perspective-agnostic.
    """
    def __init__(self, position, perspective=None):
        self.perspective = perspective
        if isinstance(position, int):
            self.position = position
        else:
            self.position = POSITIONS[position]
            if len(position) == 2 and perspective is None:
                self.perspective = position[1]
    
    def __invert__(self):
        note = Note(self.position, self.perspective)
        if note.perspective == None:
            return note
        else:
            if note.perspective == "#":
                note.perspective = "b"
            else:
                note.perspective = "#"
            return note
    
    def __add__(self, value):
        return Note((self.position + value) % 12, self.perspective)
    
    def __sub__(self, value):
        return self + (-value)
    
    def __rshift__(self, other):
        return (self.position - other.position) % 12
    
    def __lshift__(self, other):
        return other >> self
    
    def __repr__(self):
        return f"Note({self.position}, {self.perspective!r})"
    
    def __str__(self):
        names = PITCHES[self.position]
        if len(names) == 1:
            return names[0]
        if self.perspective == "#":
            return names[0]
        elif self.perspective == "b":
            return names[1]
        else:
            return "/".join(names)
