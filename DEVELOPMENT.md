# Development Notes - ComfyUI Tag Filter

## Project History

This custom node package was created to solve a specific problem in AI image generation workflows: filtering and managing Danbooru/E621 tags to extract relevant character details while avoiding contradictions.

### Original Problem

When using image tagging models (like JoyTagger or PixAI Tagger), you often get comprehensive tag lists like:

```
furry, furry_male, goat_ears, 1boy, green_shirt, shorts, male_focus, white_hair,
horns, sitting, shirt, beach_umbrella, fewer_digits, goat_horns, solo, full_body,
goat_tail, goat_boy, umbrella, goat_girl, goat, animal_ears, navel, short_sleeves,
open_mouth, skin_fangs, claws, barefoot, sheep_ears, black_eyes
```

But when you want to extract character details for image editing (e.g., "take this character and put them in a different scene"), you need only specific details like:
- `black_eyes, white_hair`

### Evolution

#### Phase 1: Basic Filtering
Initial implementation supported:
- Simple wildcards (`*_eyes`, `*_hair`)
- Exact tag matching
- Multiple output modes

**Problem:** Using wildcards like `*_hair` would return:
- `red_eyes, brown_eyes, short_hair, brown_hair, black_hair, medium_hair`

This creates contradictions:
- Multiple eye colors (impossible)
- Multiple hair lengths (contradictory)
- Multiple hair colors (unless multicolored_hair)

#### Phase 2: Semantic Categories with Limits
Added category system with syntax: `$CATEGORY_NAME:N`

Example:
```
$COLOR_EYES:1
$COLOR_HAIR:2
$LENGTH_HAIR:1
```

Results in: `red_eyes, short_hair, brown_hair, black_hair`
- Only 1 eye color (first found)
- Max 2 hair colors
- Only 1 hair length

#### Phase 3: Granular Expression Control
Further separated facial expressions into distinct categories:
- `$EMOTION` - Emotional state (happy, sad, angry)
- `$MOUTH` - Physical mouth pose (open_mouth, :3, grin)
- `$GAZE` - Where looking (at_viewer, away)
- `$EYE_STATE` - Eye open/closed state (wink, closed_eyes)
- `$EYE_FEATURE` - Special eye attributes (glowing_eyes, heart_pupils)

This prevents contradictions like:
- ❌ "happy, sad, angry" (multiple emotions)
- ❌ "open_mouth, closed_mouth" (impossible)
- ❌ "looking_at_viewer, looking_away, closed_eyes" (contradictory)

## Architecture

### File Structure

```
comfyui_tag_filter/
├── __init__.py           # Package registration
├── DN_TagFilter.py       # Main node implementation
├── tag_categories.py     # Category definitions
├── README.md             # User documentation
└── DEVELOPMENT.md        # This file
```

### Category System Design

Categories are defined in `tag_categories.py` with:

1. **Explicit tag lists** for specific categories (e.g., HAIR_LENGTHS)
2. **Generated lists** using comprehensions (e.g., COLOR_HAIR from COLORS)
3. **Wildcard patterns** for matching (e.g., `*_ears`, `*_tail`)

Categories are processed in definition order, with more specific categories first to avoid overlaps.

### Filtering Algorithm

1. **Parse input tags** - Split comma-separated string
2. **Parse whitelist** - Separate category rules (`$CATEGORY:N`) from patterns
3. **Process categories first** - For each category, find matching tags up to limit
4. **Process patterns** - Apply remaining wildcard/exact patterns
5. **Maintain order** - Sort results to match original tag order
6. **Deduplicate** - Track used tags to prevent duplicates

## Category Reference

### Appearance Categories

- `$COLOR_EYES` - Eye colors
- `$COLOR_HAIR` - Hair colors (excludes length tags)
- `$LENGTH_HAIR` - Hair length only
- `$STYLE_HAIR` - Hair styles (ponytail, braid, etc.)
- `$COLOR_SKIN` - Skin colors
- `$COLOR_FUR` - Fur colors

### Feature Categories

- `$EARS` - Ear types (cat_ears, elf_ears, etc.)
- `$TAIL` - Tail types
- `$HORNS` - Horn types
- `$WINGS` - Wing types

### Character Categories

- `$CHARACTER_COUNT` - solo, 1girl, 2boys, etc.
- `$FOCUS` - male_focus, female_focus
- `$BODY_TYPE` - petite, muscular, etc.
- `$BREAST_SIZE` - Breast size tags
- `$SPECIES` - human, furry, elf, etc.
- `$GENDER` - male, female, etc.

### Expression Categories

- `$EMOTION` / `$EXPRESSION` - Emotional state
- `$MOUTH` / `$MOUTH_POSE` - Physical mouth state
- `$GAZE` / `$EYE_DIRECTION` - Where character is looking
- `$EYE_STATE` - Eye open/closed state
- `$EYE_FEATURE` - Special eye attributes

## Common Use Cases

### Character Extraction for Image Editing

Extract only essential character features:

```
$COLOR_EYES:1
$COLOR_HAIR:2
$LENGTH_HAIR:1
$SPECIES:1
```

### Full Character Description

Get comprehensive but non-contradictory character details:

```
$COLOR_EYES:1
$COLOR_HAIR:2
$LENGTH_HAIR:1
$STYLE_HAIR:1
$EMOTION:1
$MOUTH:1
$GAZE:1
$EYE_STATE:1
$SPECIES:1
$EARS:1
$TAIL:1
```

### Specific Feature Search

Find all variations of a feature type:

```
$EARS:10
$TAIL:10
```

## Extending the System

### Adding New Categories

1. Define tag list in `tag_categories.py`:
   ```python
   CLOTHING_TOPS = ["shirt", "t-shirt", "blouse", "tank_top", ...]
   ```

2. Add to `TAG_CATEGORIES` dict:
   ```python
   TAG_CATEGORIES = {
       ...
       "CLOTHING_TOP": CLOTHING_TOPS,
   }
   ```

3. Document in README.md

### Adding Color Variants

Colors are auto-generated for common categories. To add a new color:

1. Add to `COLORS` list in `tag_categories.py`
2. Color automatically applies to `COLOR_HAIR`, `COLOR_EYES`, `COLOR_SKIN`, `COLOR_FUR`

### Adding Aliases

Some categories have aliases for convenience:
```python
"EXPRESSION": EMOTIONS,  # Alias for EMOTION
```

## Design Decisions

### Why Categories Over Pure Wildcards?

**Wildcards alone:** `*_hair` matches both `red_hair` AND `short_hair`

**Categories:** Separate `COLOR_HAIR` from `LENGTH_HAIR` based on semantic meaning

### Why Process Categories Before Patterns?

Categories with limits need first pick to enforce the limit. If patterns were processed first, they might consume tags that should count toward category limits.

### Why Maintain Original Order?

Danbooru/E621 taggers often output tags in importance order. Maintaining this order preserves the implicit ranking.

## Future Enhancements

Potential improvements:

1. **Tag prioritization** - Allow specifying preferred tags (e.g., prefer `black_hair` over `brown_hair`)
2. **Negative filtering** - Exclude specific tags or categories
3. **Tag relationships** - Understand that `multicolored_hair` allows multiple color tags
4. **Custom categories** - Allow users to define custom categories in UI
5. **Tag statistics** - Show which tags matched which categories (debug mode)
6. **Booru-specific modes** - Different category sets for Danbooru vs E621 vs other tag systems

## Related Nodes

This package was created to complement:
- **DN_TagOpsNode** (from comfyui_dados_nodes) - Tag transformation/manipulation
- **DN_JoyTaggerNode** - JoyTag image tagging
- **DN_PixAITaggerNode** - PixAI image tagging

## Technical Notes

### Tag Normalization

Tags are normalized by replacing spaces with underscores:
- `white hair` → `white_hair`
- This ensures matching works across different tag formats

### Pattern Matching

Wildcards are converted to regex:
- `*_eyes` → `^.*_eyes$`
- Exact matches skip regex for performance

### Performance Considerations

- Categories checked in order (O(categories × tags))
- Each tag checked against category patterns (O(patterns))
- For large tag lists (100+ tags), consider limiting number of categories

## Version History

- **v1.0.0** - Initial release with basic wildcard filtering
- **v1.1.0** - Added category system with limits
- **v1.2.0** - Separated mouth poses from emotions
- **v1.3.0** - Separated eye state from gaze direction, added eye features

---

*Last updated: 2026-02-20*
*Created during: Claude Code development session*
