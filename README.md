# ComfyUI Tag Filter

Smart tag filtering node for ComfyUI workflows with semantic category support for Danbooru/E621 tags.

## Features

- **Semantic Categories**: Built-in knowledge of Danbooru/E621 tag structures
- **Category Limits**: Keep only N tags from each category to avoid contradictions
- **Whitelist filtering**: Keep only specified tags from a comma-separated list
- **Wildcard support**: Use `*` for pattern matching (e.g., `*_eyes`, `white_*`)
- **Flexible input**: Whitelist accepts comma or newline-separated values
- **Multiple modes**:
  - `keep_all_matches`: Keep all matching tags in original order (default)
  - `keep_order`: Keep original tag order, only first match per whitelist item
  - `whitelist_order`: Return tags in the order they appear in whitelist

## Category System

### Syntax

Use `$CATEGORY_NAME:N` where N is the maximum number of tags to keep from that category.

### Available Categories

**Appearance:**
- `$COLOR_EYES:N` - Eye colors (red_eyes, blue_eyes, etc.)
- `$COLOR_HAIR:N` - Hair colors (black_hair, blonde_hair, etc.)
- `$LENGTH_HAIR:N` - Hair length (short_hair, long_hair, etc.)
- `$STYLE_HAIR:N` - Hair styles (ponytail, braid, etc.)
- `$COLOR_SKIN:N` - Skin colors
- `$COLOR_FUR:N` - Fur colors

**Features:**
- `$EARS:N` - Ear types (cat_ears, elf_ears, etc.)
- `$TAIL:N` - Tail types (cat_tail, fox_tail, etc.)
- `$HORNS:N` - Horn types (demon_horns, goat_horns, etc.)
- `$WINGS:N` - Wing types (angel_wings, dragon_wings, etc.)

**Character:**
- `$CHARACTER_COUNT:N` - solo, 1girl, 2boys, etc.
- `$FOCUS:N` - male_focus, female_focus, etc.
- `$BODY_TYPE:N` - petite, muscular, curvy, etc.
- `$BREAST_SIZE:N` - small_breasts, large_breasts, etc.
- `$SPECIES:N` - human, furry, elf, etc.
- `$GENDER:N` - male, female, etc.

**Expressions:**
- `$EMOTION:N` / `$EXPRESSION:N` - happy, sad, angry, blushing, scared, etc.
- `$MOUTH:N` / `$MOUTH_POSE:N` - open_mouth, :3, grin, tongue_out, teeth, etc.
- `$GAZE:N` / `$EYE_DIRECTION:N` - looking_at_viewer, looking_away, staring, etc.
- `$EYE_STATE:N` - closed_eyes, half-closed_eyes, wink, wide-eyed, etc.
- `$EYE_FEATURE:N` - glowing_eyes, heart-shaped_pupils, heterochromia, etc.

## Usage Examples

### Avoiding Contradictions

**Problem:** Getting contradictory tags like `red_eyes, brown_eyes, short_hair, black_hair, medium_hair`

**Input tags:**
```
red_eyes, brown_eyes, short_hair, brown_hair, black_hair, medium_hair
```

**Whitelist:**
```
$COLOR_EYES:1
$COLOR_HAIR:2
$LENGTH_HAIR:1
```

**Output:**
```
red_eyes, short_hair, brown_hair, black_hair
```

This keeps: 1 eye color, 2 hair colors, 1 hair length - avoiding contradictions!

### Basic Examples

**Exact tags:**
```
black_eyes
white_hair
```

**Wildcards:**
```
*_eyes
*_hair
```

**Mixed approach:**
```
$COLOR_EYES:1
$LENGTH_HAIR:1
$EMOTION:1
$MOUTH:1
$GAZE:1
$EYE_STATE:1
white_*
goat_ears
```

### Character Consistency

Keep only the most relevant facial features and expressions:

```
$COLOR_EYES:1
$COLOR_HAIR:2
$LENGTH_HAIR:1
$EMOTION:1
$MOUTH:1
$GAZE:1
$EYE_STATE:1
```

This ensures you get consistent character details without contradictory tags:
- ❌ "happy, sad, angry" → ✅ "happy"
- ❌ "open_mouth, closed_mouth, :3" → ✅ "open_mouth"
- ❌ "looking_at_viewer, looking_away" → ✅ "looking_at_viewer"
- ❌ "closed_eyes, half-closed_eyes, wink" → ✅ "closed_eyes"

## Installation

This is a standalone custom node package. Place it in your `ComfyUI/custom_nodes/` directory and restart ComfyUI.

## Category

The node appears under: **Tag Filter**
