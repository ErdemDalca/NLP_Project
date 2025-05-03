# Game Design Document

## Levels System – Game Rules

The game progresses through a series of levels, each introducing new challenges via three variables:

- Number of emojis to spot
- Time allowed
- Active emoji categories

The progression is non-linear to provide moments of relief, spikes in tension, and novelty via new category reveals.

### Level Structure

Each level defines:
- **matches**: how many emojis the player must find
- **time**: how long the player has
- **active categories**: how many emoji groups are in play
- **new category**: which category is introduced (if any)

### Category Reveal Order

Categories are introduced in the following sequence:

1. Smileys  
2. People  
3. Animals & Nature  
4. Food & Drink  
5. Activity  
6. Travel & Places  
7. Objects  
8. Symbols  
9. Flags *(final category due to difficulty)*

### Levels 1–20 Progression Table

| Level | Matches | Time  | Active Categories Count | New Category Introduced | Notes                      |
|-------|---------|-------|--------------------------|--------------------------|----------------------------|
| 1     | 3       | 45s   | 1                        | Smileys                 | Intro                      |
| 2     | 4       | 45s   | 1                        | –                       | Slight bump                |
| 3     | 5       | 45s   | 1                        | –                       | Base mastery               |
| 4     | 3       | 40s   | 2                        | People                  | New visual layer           |
| 5     | 4       | 40s   | 2                        | –                       | Build confidence           |
| 6     | 5       | 35s   | 2                        | –                       | First tension              |
| 7     | 5       | 45s   | 3                        | Animals & Nature        | Complexity expands         |
| 8     | 6       | 45s   | 3                        | –                       |                            |
| 9     | 5       | 35s   | 3                        | –                       | Fast reaction round        |
| 10    | 7       | 40s   | 3                        | –                       | First skill gate           |
| 11    | 4       | 30s   | 4                        | Food & Drink            | Speed-focused challenge    |
| 12    | 6       | 45s   | 4                        | –                       | Recovery level             |
| 13    | 7       | 35s   | 5                        | Activity                | High load starts           |
| 14    | 6       | 40s   | 6                        | Travel & Places         | Distractions increase      |
| 15    | 8       | 45s   | 7                        | Objects                 | Visual complexity          |
| 16    | 6       | 30s   | 7                        | –                       | Pressure spike             |
| 17    | 9       | 45s   | 7                        | –                       | Mastery checkpoint         |
| 18    | 7       | 40s   | 8                        | Symbols                 | One before final           |
| 19    | 10      | 35s   | 8                        | –                       | Final stretch              |
| 20    | 8       | 45s   | 9                        | Flags                   | Final level, full chaos    |

---

## Scoring System

The scoring system rewards speed, accuracy, and difficulty while avoiding harsh point penalties. This system is designed to feel fair, skill-based, and motivating.

### Base Score
- Each correctly spotted emoji: **20 points**

### Speed Bonus
- Find the emoji quickly after prompt is revealed:
  - Within 1 second: **+10 pts**
  - 1–3 seconds: **+5 pts**
  - 3–5 seconds: **+2 pts**
  - 5+ seconds: **no bonus**

### Accuracy Bonus
- No mistakes (i.e. correct on first try): **+5 pts**
- Mistakes made: **no bonus**

### Category Bonus
Some categories are harder to visually process. Bonus points apply per correct match:

| Category         | Bonus |
|------------------|-------|
| Flags            | +10   |
| Symbols          | +5    |
| All others       | –     |

*This mapping can be adjusted via config.*

### Confusable Emoji Bonus
If a match involves an emoji from a "confusable group" (e.g. 😔 😞 😣), and the player matches it without errors:
- **+10 bonus**

Confusable emoji groups will be predefined.

### Mistake Penalty
- Each incorrect tap: **-5 seconds**
- Optional future rule: higher time loss after repeated mistakes on same target.

*Note: No points are deducted for mistakes.*
