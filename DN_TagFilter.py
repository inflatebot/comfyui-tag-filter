"""
Tag Filter Node - Filters tags to keep only specified ones
Supports wildcards for pattern matching and semantic categories
"""

import re
from .tag_categories import TAG_CATEGORIES, get_category_patterns


class DN_TagFilter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "tags": ("STRING", {"forceInput": True}),
                "whitelist": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Tags to keep:\n  *_eyes (wildcards)\n  $COLOR_EYES:1 (limit)\n  $COLOR_HAIR:2 (categories)\n  white_hair (exact)"
                }),
            },
            "optional": {
                "mode": (["keep_all_matches", "keep_order", "whitelist_order"], {
                    "default": "keep_all_matches"
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filtered_tags",)
    FUNCTION = "filter_tags"
    CATEGORY = "Tag Filter"

    def filter_tags(self, tags, whitelist, mode="keep_all_matches"):
        """
        Filter tags to keep only those matching the whitelist.

        Args:
            tags: Comma-separated tags
            whitelist: Tags/patterns to keep (comma or newline separated)
                      Supports: wildcards (*_eyes), categories ($COLOR_EYES:1)
            mode:
                - keep_all_matches: Keep all matching tags in original order
                - keep_order: Keep tags in original order, but only first match per whitelist item
                - whitelist_order: Return tags in whitelist order
        """
        if not whitelist.strip():
            return (tags,)

        # Parse input tags
        tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]

        # Parse whitelist - separate categories from patterns
        category_limits = {}  # category_name -> limit
        pattern_items = []    # regular patterns/wildcards

        for line in whitelist.split('\n'):
            for item in line.split(','):
                item = item.strip()
                if not item:
                    continue

                # Check if it's a category with limit: $CATEGORY_NAME:N
                if item.startswith('$'):
                    match = re.match(r'^\$([A-Z_]+):(\d+)$', item)
                    if match:
                        category_name = match.group(1)
                        limit = int(match.group(2))
                        if category_name in TAG_CATEGORIES:
                            category_limits[category_name] = limit
                        else:
                            print(f"Warning: Unknown category ${category_name}")
                    else:
                        print(f"Warning: Invalid category syntax: {item}")
                else:
                    pattern_items.append(item)

        if not category_limits and not pattern_items:
            return (tags,)

        def normalize_tag(tag):
            """Normalize tag by replacing spaces with underscores"""
            return tag.replace(' ', '_')

        def matches_pattern(tag, pattern):
            """Check if tag matches a pattern (supports * wildcard)"""
            tag_norm = normalize_tag(tag)
            pattern_norm = normalize_tag(pattern)

            # If no wildcard, do exact match
            if '*' not in pattern_norm:
                return tag_norm == pattern_norm

            # Convert wildcard pattern to regex-like matching
            regex_pattern = pattern_norm.replace('*', '.*')
            regex_pattern = f"^{regex_pattern}$"
            return re.match(regex_pattern, tag_norm) is not None

        def tag_matches_category(tag, category_patterns):
            """Check if tag matches any pattern in a category"""
            for pattern in category_patterns:
                if matches_pattern(tag, pattern):
                    return True
            return False

        filtered_tags = []
        used_tags = set()  # Track tags we've already added

        # Process categories first (with limits)
        for category_name, limit in category_limits.items():
            category_patterns = TAG_CATEGORIES[category_name]
            matched_count = 0

            for tag in tag_list:
                if tag in used_tags:
                    continue

                if tag_matches_category(tag, category_patterns):
                    filtered_tags.append(tag)
                    used_tags.add(tag)
                    matched_count += 1

                    if matched_count >= limit:
                        break

        # Process regular patterns (respecting mode)
        if pattern_items:
            if mode == "whitelist_order":
                # Return tags in whitelist order
                for pattern in pattern_items:
                    for tag in tag_list:
                        if tag not in used_tags and matches_pattern(tag, pattern):
                            filtered_tags.append(tag)
                            used_tags.add(tag)

            elif mode == "keep_order":
                # Keep original tag order, but only first match per whitelist item
                matched_patterns = set()
                for tag in tag_list:
                    if tag in used_tags:
                        continue
                    for pattern in pattern_items:
                        if pattern not in matched_patterns and matches_pattern(tag, pattern):
                            filtered_tags.append(tag)
                            used_tags.add(tag)
                            matched_patterns.add(pattern)
                            break

            else:  # keep_all_matches (default)
                # Keep all matches in original tag order
                for tag in tag_list:
                    if tag in used_tags:
                        continue
                    if any(matches_pattern(tag, pattern) for pattern in pattern_items):
                        filtered_tags.append(tag)
                        used_tags.add(tag)

        # Sort filtered_tags back to original order
        if mode == "keep_all_matches" or mode == "keep_order":
            # Maintain original order from tag_list
            tag_order = {tag: i for i, tag in enumerate(tag_list)}
            filtered_tags.sort(key=lambda t: tag_order.get(t, float('inf')))

        result = ', '.join(filtered_tags)
        return (result,)


NODE_CLASS_MAPPINGS = {
    "DN_TagFilter": DN_TagFilter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DN_TagFilter": "Tag Filter"
}
