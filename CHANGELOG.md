# Changelog

All notable changes to the ComfyUI Tag Filter node will be documented in this file.

## [1.3.0] - 2026-02-20

### Added
- Separated eye-related tags into three distinct categories:
  - `$EYE_STATE` - Physical eye state (closed_eyes, wink, half-closed_eyes)
  - `$GAZE` / `$EYE_DIRECTION` - Where character is looking (now only direction)
  - `$EYE_FEATURE` - Special eye attributes (glowing_eyes, heart_pupils, heterochromia)
- Added aliases: `$EYES_STATE`, `$EYE_FEATURES`

### Changed
- `$GAZE` now only includes directional tags (looking_at_viewer, looking_away, etc.)
- Eye state tags moved from `$GAZE` to new `$EYE_STATE` category
- Special eye features moved from `$GAZE` to new `$EYE_FEATURE` category

### Improved
- Better granular control over facial expressions
- Prevents contradictions like "looking_at_viewer, closed_eyes"

## [1.2.0] - 2026-02-20

### Added
- `$MOUTH` / `$MOUTH_POSE` category for physical mouth poses
- Separated mouth-specific tags from emotional expressions
- New mouth tags: open_mouth, :3, grin, tongue_out, teeth, etc.

### Changed
- `$EMOTION` now focuses purely on emotional state
- Mouth pose tags (grin, :d, :3, etc.) moved to `$MOUTH` category
- Emoticon-style tags distributed between `$EMOTION` and `$MOUTH` based on meaning

### Improved
- Clearer separation between emotional state and physical mouth shape
- Better handling of emoticons like :3, :d, ^_^

## [1.1.0] - 2026-02-20

### Added
- `$EMOTION` / `$EXPRESSION` category for emotions and expressions
- `$GAZE` / `$EYE_DIRECTION` category for eye-related tags
- Comprehensive emotion tags from Danbooru face tags
- Comprehensive gaze/eye tags from Danbooru eye tags
- Category aliases for easier use

### Improved
- Better facial expression control
- Prevents contradictions in emotional tags

## [1.0.0] - 2026-02-20

### Added
- Initial release with semantic category system
- Category syntax: `$CATEGORY_NAME:N` for limiting tags per category
- Predefined categories for Danbooru/E621 tags:
  - Appearance: `$COLOR_EYES`, `$COLOR_HAIR`, `$LENGTH_HAIR`, `$STYLE_HAIR`
  - Features: `$EARS`, `$TAIL`, `$HORNS`, `$WINGS`
  - Character: `$CHARACTER_COUNT`, `$FOCUS`, `$SPECIES`, `$GENDER`, etc.
- Wildcard pattern support (`*_eyes`, `white_*`)
- Exact tag matching
- Three output modes:
  - `keep_all_matches` - All matches in original order (default)
  - `keep_order` - First match per whitelist item
  - `whitelist_order` - Output in whitelist order
- Tag normalization (space to underscore conversion)
- Maintains original tag order for importance preservation
- Duplicate prevention

### Features
- Prevents tag contradictions (e.g., multiple eye colors, hair lengths)
- Smart semantic grouping of Danbooru/E621 tags
- Extensible category system
- Comprehensive tag database for common categories

---

## Version Numbering

This project follows [Semantic Versioning](https://semver.org/):
- **Major** (X.0.0): Breaking changes to API or category structure
- **Minor** (0.X.0): New categories or features (backwards compatible)
- **Patch** (0.0.X): Bug fixes and minor improvements

## Future Roadmap

Planned features for consideration:
- [ ] Tag prioritization within categories
- [ ] Negative filtering (exclude tags)
- [ ] Custom user-defined categories
- [ ] Tag relationship understanding (multicolored_hair)
- [ ] Debug mode showing category matches
- [ ] Booru-specific category presets
- [ ] Clothing categories
- [ ] Pose/position categories
- [ ] Background/setting categories
