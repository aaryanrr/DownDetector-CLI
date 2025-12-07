# Changelog

## [Unreleased] - 2025-12-06

### Fixed
- Fixed scraping functionality to work with modern DownDetector website structure
- Improved bot detection bypass with updated headers and session handling
- Added backward compatibility with original HTML structure

### Changed
- Updated User-Agent to modern Chrome version (120.0.0.0)
- Added comprehensive HTTP headers (Accept, Accept-Language, Sec-Fetch-*, etc.)
- Implemented session-based requests for better connection handling
- Added timeout (10 seconds) to prevent hanging requests

### Added
- Multi-strategy HTML parsing:
  - Strategy 1: Original selector for backward compatibility
  - Strategy 2: Direct entry-title class lookup (most common)
  - Strategy 3: Find elements with "status" or "entry-title" in class names
  - Strategy 4: Fallback to h1 with status-related keywords
- Better error messages for different failure scenarios
- Response status validation with `raise_for_status()`
- Timeout handling for connection issues

### Technical Details

The scraper now attempts multiple strategies to find the status message, making it more resilient to website changes:

1. **Backward Compatibility**: Tries the original `div#company > div.h2.entry-title` selector first
2. **Modern Structure**: Looks for `.entry-title` class on h1, h2, h3, or div elements
3. **Class Pattern Matching**: Searches for elements with "status" or "entry-title" in their class names
4. **Keyword-Based Fallback**: Uses h1 tags containing status keywords (problem, issue, outage, down, working, reports, no problems)

This multi-layered approach ensures the scraper works with both old and new website structures.
