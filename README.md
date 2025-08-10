# Cygni Arcana

Copyright (c) 2025 Oliver Staats

Cygni Arcana is a Python project that maps notable stars, including those in the Cygnus constellation, to tarot cards (Major and Minor Arcana) based on their galactic coordinates. The project visualizes these mappings in a plot, positioning stars relative to the Galactic Center (GC) and the Galactic Anti-Center (GAC) using their distances and longitudes.

-----

## Features

  * **Maps 22 Major Arcana cards and the 4 Minor Arcana suits** to 26 notable stars (e.g., Deneb, Albireo, Sirius), such as "The Sun" (Sol) and "The High Priestess" (Deneb).
  * **Converts galactic polar coordinates** (distance, longitude) to a 2D plot.
  * **Uses matplotlib** to generate a visual representation, saved as `cygni_arcana_plot.png`.

-----

## Usage

Run the main script to generate the tarot-star plot:

```bash
uv run src/cygni_arcana/tarot_map.py
```

The script generates a plot saved as `cygni_arcana_plot.png` in the project root. The plot displays stars with their tarot assignments, distances, and Roman numerals (for Major Arcana), color-coded by star properties.

-----

## Example Output

The generated plot (`cygni_arcana_plot.png`) shows:

  * Stars positioned along the x-axis based on their **position relative to the Milky Way's clockwise galactic rotation**, as viewed from galactic north. Stars "ahead" of Sol are on the left, and stars "behind" are on the right.
  * The y-axis represents **ordinal ranking by distance from the Galactic Center**, with Sagittarius A\* ("Wheel of Fortune") at the top and stars like Betelgeuse ("The Tower") further down.
  * Labels include star name, distance (in light-years), and tarot card (e.g., "Deneb(1500 ly) The High Priestess(II)").

-----

## License

This project is under a restrictive license. Please see the `LICENSE` file for details on usage.

-----

## Contact

For inquiries, contact Oliver Staats at `olambo@gmail.com`.

-----

## Future Development

Future enhancements may include interactive visualizations or alternative plotting styles.