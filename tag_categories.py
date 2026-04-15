"""
Danbooru/E621 Tag Categories
Semantic groupings for common tag patterns
"""

# Common color names used in tags
COLORS = [
    "red", "blue", "green", "brown", "black", "white", "blonde", "pink",
    "purple", "orange", "yellow", "grey", "gray", "silver", "aqua", "cyan",
    "gold", "golden", "multicolored", "two-tone", "rainbow", "gradient",
    "light_blue", "dark_blue", "light_brown", "dark_brown", "light_green",
    "dark_green", "blonde", "platinum_blonde", "ash_blonde", "strawberry_blonde"
]

# Hair length tags
HAIR_LENGTHS = [
    "bald", "very_short_hair", "short_hair", "medium_hair",
    "long_hair", "very_long_hair", "absurdly_long_hair"
]

# Hair style tags
HAIR_STYLES = [
    "ponytail", "twin_tails", "twintails", "side_ponytail", "high_ponytail",
    "braid", "braided_hair", "single_braid", "twin_braids", "french_braid",
    "bob_cut", "wavy_hair", "curly_hair", "straight_hair", "messy_hair",
    "spiked_hair", "afro", "buzz_cut", "pixie_cut", "hime_cut",
    "drill_hair", "ringlets", "bun", "double_bun", "hair_bun",
    "mohawk", "undercut", "dreadlocks", "cornrows"
]

# Emotion/Expression tags (emotional state, not physical mouth pose)
EMOTIONS = [
    # Positive emotions
    "smile", "smiling", "happy", "joyful", "cheerful", "laughing", "giggling",
    # Negative emotions
    "sad", "sadness", "crying", "tears", "teary_eyes", "streaming_tears",
    "tearing_up", "sobbing", "t_t",
    "angry", "anger", "annoyed", "frustrated", "rage",
    # Embarrassment/shyness
    "blush", "blushing", "embarrassed", "shy", "nervous", "flustered",
    "nosebleed", "light_blush", "full-face_blush",
    # Surprise/shock
    "surprised", "shock", "shocked", "astonished", "startled",
    "wide-eyed",
    # Fear/worry
    "scared", "frightened", "terrified", "fear", "worried", "anxious",
    "trembling", "shaking", "nervous_smile", "cold_sweat",
    # Confusion
    "confused", "confusion", "puzzled", "thinking",
    # Other emotional states
    "serious", "stern", "expressionless", "blank_stare", "deadpan",
    "sleepy", "tired", "exhausted", "yawning", "drowsy",
    "drunk", "dizzy", "dazed",
    "smug", "seductive_smile", "bedroom_eyes",
    "crazy", "insane", "crazy_smile", "crazy_grin",
    "ahegao", "naughty_face",
    "disgusted", "disgust", "contempt", "sigh", "sighing",
    "pouting", "sulking",
    "curious", "interested", "excited", "excitement",
    "disappointed", "disappointment", "despair",
]

# Mouth pose/shape tags (physical mouth state)
MOUTH_POSES = [
    # Open/closed
    "open_mouth", "closed_mouth", "mouth_closed", "parted_lips",
    "half-open_mouth", "wide_open_mouth",
    # Smiles/grins (physical shape)
    "grin", "grinning", "evil_grin",
    # Frowns (physical shape)
    "frown", "frowning", "scowl", "scowling",
    # Special mouth shapes
    "pout", ":3", "=3", "cat_mouth", "w", "3",
    ":d", ":)", ":o", ":p", "xd", ";d", ";)", ";p",
    "^_^", ">_<", ">:(", "o_o", "@_@", "x_x", "-_-", "ಠ_ಠ", "?: ",
    # Teeth/tongue
    "teeth", "clenched_teeth", "gritted_teeth", "fangs", "sharp_teeth",
    "tongue", "tongue_out", "licking", "licking_lips",
    # Other
    "wavy_mouth", "lipbite", "lip_biting", "pursed_lips",
    "kiss", "kissy_face", "blowing_kiss", "puckered_lips",
    "drool", "drooling", "saliva", "spit",
]

# Gaze/Eye direction tags (where the character is looking)
GAZES = [
    # Direction
    "looking_at_viewer", "looking_away", "looking_back", "looking_down",
    "looking_up", "looking_to_the_side", "looking_at_another",
    "sideways_glance", "looking_ahead", "looking_afar",
    # Eye contact
    "eye_contact", "avoiding_eye_contact",
    # Intensity/style of gaze
    "stare", "staring", "glare", "glaring", "intense_eyes",
]

# Eye state tags (open, closed, wink, etc.)
EYE_STATES = [
    # Open/closed
    "eyes_closed", "closed_eyes", "eyes_open", "open_eyes",
    "half-closed_eyes", "narrowed_eyes", "squinting",
    # Winking
    "one_eye_closed", "wink", "winking",
    # Emoticon-style (eye state focused)
    "^_^", ">_<", "x_x",
    # Wide eyes
    "wide-eyed", "wide_eyes", "eyes_wide_open",
]

# Eye features/attributes (special properties, not state or direction)
EYE_FEATURES = [
    # Special appearances
    "glowing_eyes", "empty_eyes", "solid_eyes", "no_pupils",
    "sparkling_eyes", "shiny_eyes", "teary_eyes", "watery_eyes",
    "lifeless_eyes", "dull_eyes", "crazy_eyes",
    "bedroom_eyes", "seductive_eyes",
    # Pupil shapes
    "heart-shaped_pupils", "heart_in_eye", "star-shaped_pupils", "slit_pupils",
    "constricted_pupils", "dilated_pupils", "spiral_eyes", "swirly_eyes",
    # Eye anatomy
    "heterochromia", "extra_eyes", "third_eye",
    "tsurime", "tareme", "sanpaku", "upturned_eyes", "downturned_eyes",
]

# Build category definitions
# Categories are checked in order - more specific ones first
TAG_CATEGORIES = {
    # Hair categories
    "LENGTH_HAIR": HAIR_LENGTHS,
    "STYLE_HAIR": HAIR_STYLES,
    "COLOR_HAIR": [f"{color}_hair" for color in COLORS],

    # Eye categories
    "COLOR_EYES": [f"{color}_eyes" for color in COLORS],

    # Skin/fur categories
    "COLOR_SKIN": [f"{color}_skin" for color in COLORS],
    "COLOR_FUR": [f"{color}_fur" for color in COLORS],

    # Body features
    "EARS": ["*_ears", "animal_ears", "pointy_ears", "elf_ears", "cat_ears",
             "dog_ears", "fox_ears", "bunny_ears", "mouse_ears", "bear_ears"],
    "TAIL": ["*_tail", "animal_tail", "cat_tail", "dog_tail", "fox_tail",
             "bunny_tail", "demon_tail", "dragon_tail", "devil_tail"],
    "HORNS": ["horns", "*_horns", "demon_horns", "dragon_horns", "bull_horns",
              "goat_horns", "oni_horns", "curved_horns", "ram_horns"],
    "WINGS": ["wings", "*_wings", "angel_wings", "demon_wings", "dragon_wings",
              "bat_wings", "feathered_wings", "fairy_wings"],

    # Character count
    "CHARACTER_COUNT": ["solo", "1girl", "1boy", "2girls", "2boys", "3girls",
                        "3boys", "multiple_girls", "multiple_boys", "everyone"],

    # Focus
    "FOCUS": ["male_focus", "female_focus", "solo_focus", "character_focus"],

    # Body type/size
    "BODY_TYPE": ["chibi", "loli", "shota", "petite", "curvy", "muscular",
                  "chubby", "slender", "skinny", "tall", "short", "thicc"],

    # Breast size
    "BREAST_SIZE": ["flat_chest", "small_breasts", "medium_breasts",
                    "large_breasts", "huge_breasts", "gigantic_breasts"],

    # Species/form
    "SPECIES": ["human", "humanoid", "furry", "anthro", "feral", "taur",
                "monster", "demon", "angel", "elf", "fairy", "mermaid",
                "robot", "android", "cyborg", "kemonomimi"],

    # Gender
    "GENDER": ["male", "female", "futanari", "intersex", "ambiguous_gender",
               "femboy", "tomboy", "trap", "reverse_trap", "otoko no ko"],

    # Emotions/Expressions (emotional state)
    "EMOTION": EMOTIONS,
    "EXPRESSION": EMOTIONS,  # Alias for EMOTION

    # Mouth poses (physical mouth state/shape)
    "MOUTH": MOUTH_POSES,
    "MOUTH_POSE": MOUTH_POSES,  # Alias for MOUTH

    # Gazes/Eye direction (where looking)
    "GAZE": GAZES,
    "EYE_DIRECTION": GAZES,  # Alias for GAZE

    # Eye state (open/closed/wink)
    "EYE_STATE": EYE_STATES,
    "EYES_STATE": EYE_STATES,  # Alias

    # Eye features (special attributes)
    "EYE_FEATURE": EYE_FEATURES,
    "EYE_FEATURES": EYE_FEATURES,  # Alias
}


def get_category_patterns(category_name):
    """Get patterns for a category name"""
    return TAG_CATEGORIES.get(category_name, [])


def get_all_categories():
    """Get list of all available category names"""
    return list(TAG_CATEGORIES.keys())
