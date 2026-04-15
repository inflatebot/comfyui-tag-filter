# Tag Filter - Quick Reference

## Quick Syntax Guide

```
# Category with limit
$CATEGORY_NAME:N

# Wildcard
*_pattern

# Exact tag
exact_tag_name
```

## Common Patterns

### Character Extraction (Minimal)
For image editing - just the essentials:
```
$COLOR_EYES:1
$COLOR_HAIR:1
$LENGTH_HAIR:1
```

### Character Extraction (Detailed)
More details but avoid contradictions:
```
$COLOR_EYES:1
$COLOR_HAIR:2
$LENGTH_HAIR:1
$STYLE_HAIR:1
$SPECIES:1
$EARS:1
$TAIL:1
```

### Character + Expression
Include facial details:
```
$COLOR_EYES:1
$COLOR_HAIR:2
$LENGTH_HAIR:1
$EMOTION:1
$MOUTH:1
$GAZE:1
$EYE_STATE:1
```

### Everything Character-Related
Comprehensive character description:
```
$COLOR_EYES:1
$COLOR_HAIR:2
$LENGTH_HAIR:1
$STYLE_HAIR:1
$EMOTION:1
$MOUTH:1
$GAZE:1
$EYE_STATE:1
$EYE_FEATURE:1
$SPECIES:1
$GENDER:1
$BODY_TYPE:1
$EARS:1
$TAIL:1
$HORNS:1
$WINGS:1
```

### Specific Features Only
```
goat_ears
goat_tail
goat_horns
```

### Mixed Approach
Combine categories and exact matches:
```
$COLOR_EYES:1
$COLOR_HAIR:1
$EMOTION:1
goat_ears
solo
```

## Category Cheat Sheet

| Category | Example Tags | Use When |
|----------|-------------|----------|
| `$COLOR_EYES:1` | red_eyes, blue_eyes | Avoid multiple eye colors |
| `$COLOR_HAIR:2` | black_hair, brown_hair | Allow highlights/tips |
| `$LENGTH_HAIR:1` | short_hair, long_hair | Avoid length contradictions |
| `$STYLE_HAIR:1` | ponytail, braid | Pick one style |
| `$EMOTION:1` | happy, sad, angry | One emotion at a time |
| `$MOUTH:1` | open_mouth, :3, grin | One mouth pose |
| `$GAZE:1` | looking_at_viewer | One direction |
| `$EYE_STATE:1` | closed_eyes, wink | One eye state |
| `$SPECIES:1` | human, furry, elf | One species |
| `$EARS:1` | cat_ears, elf_ears | One ear type |
| `$TAIL:1` | cat_tail, fox_tail | One tail type |

## Common Problems & Solutions

### Problem: Too many hair tags
**Input:** `red_hair, blue_hair, short_hair, long_hair, ponytail`

**Solution:**
```
$COLOR_HAIR:1
$LENGTH_HAIR:1
$STYLE_HAIR:1
```

**Output:** `red_hair, short_hair, ponytail`

---

### Problem: Contradictory expressions
**Input:** `smiling, crying, open_mouth, closed_mouth, looking_at_viewer, closed_eyes`

**Solution:**
```
$EMOTION:1
$MOUTH:1
$GAZE:1
$EYE_STATE:1
```

**Output:** `smiling, open_mouth, looking_at_viewer, closed_eyes`

---

### Problem: Want specific features only
**Input:** `1girl, long_hair, red_eyes, sitting, outdoors, tree, grass`

**Solution:**
```
red_eyes
long_hair
```

**Output:** `long_hair, red_eyes`

---

### Problem: Want all animal features
**Input:** `cat_ears, cat_tail, whiskers, paws, long_hair, blue_eyes`

**Solution:**
```
cat_*
whiskers
paws
```

**Output:** `cat_ears, cat_tail, whiskers, paws`

## Tips

1. **Categories are processed first** - They get first pick of matching tags
2. **Order matters** - Tags returned in original order (preserves importance)
3. **No duplicates** - Each tag counted only once
4. **Limit = max, not exact** - `$COLOR_HAIR:2` means "up to 2", not "exactly 2"
5. **Case doesn't matter** - Tags normalized (spaces → underscores)

## All Available Categories

```
Appearance:
  $COLOR_EYES, $COLOR_HAIR, $COLOR_SKIN, $COLOR_FUR
  $LENGTH_HAIR, $STYLE_HAIR

Features:
  $EARS, $TAIL, $HORNS, $WINGS

Character:
  $CHARACTER_COUNT, $FOCUS, $BODY_TYPE
  $BREAST_SIZE, $SPECIES, $GENDER

Expressions:
  $EMOTION, $EXPRESSION (alias)
  $MOUTH, $MOUTH_POSE (alias)
  $GAZE, $EYE_DIRECTION (alias)
  $EYE_STATE
  $EYE_FEATURE, $EYE_FEATURES (alias)
```

## Node Settings

**Mode options:**
- `keep_all_matches` (default) - All matches in original order
- `keep_order` - Original order, first match per whitelist item
- `whitelist_order` - Output in whitelist order

Most use cases: stick with `keep_all_matches`
