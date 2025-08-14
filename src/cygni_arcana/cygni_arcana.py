# Cygni Arcana - Stellar Tarot Mapping
# Copyright (c) 2025 Oliver Staats
# This software is licensed for exclusive use by Oliver Staats. See LICENSE for details.
#
# COLLABORATIVE DEVELOPMENT CREDITS:
# Primary Concept & Direction: Oliver Staats
# AI Development Partners:
#   - Claude (Anthropic): Core coordinate system design, galactic positioning algorithms,
#     plotting functions, and extensive debugging of galactic longitude conventions
#   - Grok (xAI): Programming assistance, conceptual development, latitude data, and galactic plane distance calculation
#   - ChatGPT (OpenAI): Technical consultation and implementation support
#   - Gemini (Google): Additional development assistance
#   - Grok's Ani: Visual analysis and star mapping recommendations (4+ stellar assignments)
#
# This project represents a novel approach to collaborative human-AI creative development,
# combining astronomical positioning with tarot symbolism through multi-system AI partnership.
#
# DATA SOURCES & COORDINATE SYSTEM:
# - Star positions: SIMBAD (http://simbad.u-strasbg.fr/simbad/), Gaia DR3, Hipparcos Catalogue
# - Coordinates converted from equatorial (RA, Dec) to galactic (longitude, latitude) using standard transformations
# - Distances in light-years represent 3D distances from Sol
#
# COORDINATE SYSTEM NOTES:
# The galactic coordinate development involved extensive iteration across multiple AI systems
# to achieve correct longitude transformations and latitude integration for 3D positioning.

import matplotlib.pyplot as plt
import math
from collections import namedtuple
from pathlib import Path

# Configuration
DARK_MODE = True  # Set to False for light mode

# Constants
GALACTIC_CENTER_DISTANCE = 26000
PROJECT_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / 'generated'

# Color themes
THEMES = {
    'light': {
        'background': 'white',
        'text': 'black',
        'grid': 'black',
        'black_hole_edge': 'black',
        'black_hole_glow': '#FFD700',  # Golden glow for visibility
        'sol_edge': 'orange'
    },
    'dark': {
        'background': 'black',
        'text': 'white',
        'grid': 'white',
        'black_hole_edge': 'white',
        'black_hole_glow': '#FF8C00',  # Orange glow
        'sol_edge': 'orange'
    }
}

# Get current theme
THEME = THEMES['dark' if DARK_MODE else 'light']

# Star data with galactic latitudes
STARS = [
    {"name": "Sagittarius A*", "distance": 26000, "longitude": 0, "latitude": 0, "size": 60,
     "tarot": "Wheel of Fortune", "roman": "X",
     "color": "#000000"},

    {"name": "Sol", "distance": 0, "longitude": 180, "latitude": 0, "size": 40,
     "tarot": "The Sun", "roman": "XIX",
     "color": "#FFFF00"},

    {"name": "T Coronae Borealis", "distance": 3000, "longitude": 55, "latitude": 15.8, "size": 30,
     "tarot": "Judgment", "roman": "XX",
     "color": "#FFFFFF"},

    {"name": "Sheliak", "distance": 960, "longitude": 63, "latitude": 8.7, "size": 25,
     "tarot": "The Moon", "roman": "XVIII",
     "color": "#1C1CF0"},

    {"name": "Antares", "distance": 550, "longitude": 351, "latitude": -4.6, "size": 55,
     "tarot": "The Hierophant", "roman": "V",
     "color": "#FF4500"},

    {"name": "Deneb", "distance": 1500, "longitude": 80, "latitude": 2.1, "size": 45,
     "tarot": "The High Priestess", "roman": "II",
     "color": "#CFE2F3"},

    {"name": "Albireo", "distance": 430, "longitude": 62, "latitude": -1.2, "size": 20,
     "tarot": "The Lovers", "roman": "VI",
     "color": "#FFD700", "edge_color": "#0080FF"},

    {"name": "Spica", "distance": 250, "longitude": 316, "latitude": 50.8, "size": 25,
     "tarot": "Strength", "roman": "VIII",
     "color": "#7B68EE"},

    {"name": "Achernar", "distance": 139, "longitude": 290, "latitude": -57.1, "size": 25,
     "tarot": "The Hanged Man", "roman": "XII",
     "color": "#00BFFF"},

    {"name": "Zubenelgenubi", "distance": 77, "longitude": 347, "latitude": -16.0, "size": 25,
     "tarot": "Justice", "roman": "XI",
     "color": "#FFFFE0"},

    {"name": "Arcturus", "distance": 36.7, "longitude": 15, "latitude": 69.1, "size": 30,
     "tarot": "The Magician", "roman": "I",
     "color": "#FF8C00"},

    {"name": "Fomalhaut", "distance": 25, "longitude": 20, "latitude": -65.0, "size": 20,
     "tarot": "The Star", "roman": "XVII",
     "color": "#FFFFFF"},

    {"name": "Vega", "distance": 25, "longitude": 67, "latitude": 19.2, "size": 20,
     "tarot": "The Empress", "roman": "III",
     "color": "#E0FFFF"},

    {"name": "Alpha Centauri", "distance": 4.37, "longitude": 315, "latitude": -0.7, "size": 20,
     "tarot": "The World", "roman": "XXI",
     "color": "#FFD700"},

    {"name": "Sirius", "distance": 8.6, "longitude": 227, "latitude": -8.9, "size": 20,
     "tarot": "The Fool", "roman": "0",
     "color": "#ADD8E6"},

    {"name": "Tau Ceti", "distance": 12, "longitude": 172, "latitude": -15.6, "size": 20,
     "tarot": "Temperance", "roman": "XIV",
     "color": "#F5DEB3"},

    {"name": "Capella", "distance": 42.9, "longitude": 162, "latitude": 4.6, "size": 25,
     "tarot": "The Chariot", "roman": "VII",
     "color": "#FFDAB9"},

    {"name": "Regulus", "distance": 79, "longitude": 226, "latitude": 0.5, "size": 25,
     "tarot": "The Emperor", "roman": "IV",
     "color": "#A9A9F5"},

    {"name": "Algol", "distance": 93, "longitude": 151, "latitude": 22.3, "size": 25,
     "tarot": "The Devil", "roman": "XV",
     "color": "#FF6347"},

    {"name": "Mira", "distance": 420, "longitude": 171, "latitude": -2.9, "size": 30,
     "tarot": "Death", "roman": "XIII",
     "color": "#FF4500"},

    {"name": "Betelgeuse", "distance": 642, "longitude": 199, "latitude": 9.0, "size": 60,
     "tarot": "The Tower", "roman": "XVI",
     "color": "#FF4500"},

    {"name": "Canopus", "distance": 310, "longitude": 261.2, "latitude": -25.3, "size": 35,
     "tarot": "The Hermit", "roman": "IX",
     "color": "#F0E68C"},

    # Minor Arcana suits
    {"name": "Eltanin", "distance": 154, "longitude": 94, "latitude": 9.8, "size": 25,
     "tarot": "Wands", "roman": "♣",
     "color": "#FF4500"},

    {"name": "Thuban", "distance": 309, "longitude": 96, "latitude": 25.6, "size": 25,
     "tarot": "Cups", "roman": "♥",
     "color": "#ADD8E6"},

    {"name": "Polaris", "distance": 433, "longitude": 123, "latitude": 27.2, "size": 25,
     "tarot": "Swords", "roman": "♠",
     "color": "#F0E68C"},

    {"name": "Algenib", "distance": 390, "longitude": 162, "latitude": -16.7, "size": 25,
     "tarot": "Pentacles", "roman": "♦",
     "color": "#FFD700"},
]

# Define coordinate structure
CartesianCoords = namedtuple('CartesianCoords', ['x_plot', 'y_plot'])


def galactic_to_cartesian(distance, longitude_deg, latitude_deg):
    """
    Convert galactic polar coordinates to cartesian coordinates for plotting.

    Args:
        distance (float): 3D distance from Sol in light-years
        longitude_deg (float): Galactic longitude in degrees (0° = towards GC)
        latitude_deg (float): Galactic latitude in degrees (0° = galactic plane)

    Returns:
        CartesianCoords: Named tuple with:
            - x_plot: perpendicular distance from GC-Sol-GAC line
                     (+ ahead of rotation, - behind)
            - y_plot: distance along GC-Sol-GAC line
                     (+ towards GC, - towards GAC)
    """
    # Convert to radians
    longitude_rad = math.radians(longitude_deg)
    latitude_rad = math.radians(latitude_deg)

    # Project distance onto galactic plane
    planar_distance = distance * math.cos(latitude_rad)

    # Calculate cartesian coordinates
    x_plot = planar_distance * math.sin(longitude_rad)  # perpendicular to GC-Sol-GAC line
    y_plot = planar_distance * math.cos(longitude_rad)  # along GC-Sol-GAC line

    return CartesianCoords(x_plot, y_plot)


def categorize_x_plot(perpendicular_distance):
    """
    Categorize the distance from GC-Sol-GAC line into discrete bins for plotting.

    Args:
        perpendicular_distance (float): Distance from line (+ ahead, - behind clockwise rotation)

    Returns:
        float: Plot coordinate for left-to-right display
        (ahead of clockwise rotation plotted on left/negative, behind on right/positive)
    """
    abs_distance = abs(perpendicular_distance)
    # For left-to-right plotting convention: ahead of clockwise rotation → left side → negative coordinates
    sign = -1 if perpendicular_distance >= 0 else 1

    # Categorize by absolute distance from GC-Sol-GAC line
    if abs_distance < 1:
        return 0  # Essentially on the line (center)
    elif abs_distance < 12:
        return sign * 0.5  # Slightly off line (near_ahead/near_behind)
    elif abs_distance < 70:
        return sign * 1  # Moderate distance from line (ahead/behind)
    else:
        return sign * 2  # Far from line (far_ahead/far_behind)


def rank_y_plot(star_data, all_stars):
    """
    Calculates the y-position based on ordinal ranking by y_plot coordinate.

    Args:
        star_data (dict): The dictionary for the current star.
        all_stars (list): List of all stars for ranking.

    Returns:
        float: The y-position for plotting.
    """
    star_name = star_data['name']

    # Special reference points
    if star_name == "Sagittarius A*":
        return 0.7  # GC at top
    elif star_name == "Sol":
        return 0  # Sol at middle reference point

    # Calculate y_plot for all stars (excluding special cases)
    regular_stars = []
    for star in all_stars:
        if star['name'] not in ["Sagittarius A*", "Sol"]:
            coords = galactic_to_cartesian(star['distance'], star['longitude'], star['latitude'])
            regular_stars.append({
                'name': star['name'],
                'y_plot': coords.y_plot
            })

    # Sort by y_plot (positive = toward GC, negative = toward GAC)
    regular_stars.sort(key=lambda x: x['y_plot'], reverse=True)

    # Find current star's rank
    star_coords = galactic_to_cartesian(star_data['distance'], star_data['longitude'], star_data['latitude'])
    current_y_plot = star_coords.y_plot

    # Stars with positive y_plot (toward GC) go above Sol
    if current_y_plot > 0:
        positive_stars = [s for s in regular_stars if s['y_plot'] > 0]
        if star_name in [s['name'] for s in positive_stars]:
            rank = [s['name'] for s in positive_stars].index(star_name)
            total_positive = len(positive_stars)
            # Map galactic coordinates to plot: stars closer to GC (higher y_plot) → higher plot position
            reversed_rank = total_positive - 1 - rank
            return 0.1 + (reversed_rank / (total_positive - 1)) * 0.47 if total_positive > 1 else 0.35

    # Stars with negative y_plot (toward GAC) go below Sol
    else:
        negative_stars = [s for s in regular_stars if s['y_plot'] <= 0]
        if star_name in [s['name'] for s in negative_stars]:
            rank = [s['name'] for s in negative_stars].index(star_name)
            total_negative = len(negative_stars)
            # More negative y_plot gets lower position (further from GC)
            return -0.1 - (rank / (total_negative - 1)) * 0.47 if total_negative > 1 else -0.35

    return 0  # Fallback


def plot_star(ax, star, all_stars):
    """
    Plot a single star on the axes.

    Args:
        ax: Matplotlib axes object
        star (dict): Star data dictionary
        all_stars (list): List of all stars for ranking
    """
    # Get cartesian coordinates
    coords = galactic_to_cartesian(star['distance'], star['longitude'], star['latitude'])

    # Get the x-position using categories
    x_pos = categorize_x_plot(coords.x_plot)

    # Get the y-position using ordinal ranking
    y_pos = rank_y_plot(star, all_stars)

    # Special handling for Sagittarius A* (black hole)
    if star['name'] == "Sagittarius A*":
        # Draw the event horizon as a ring with glow effect
        ax.scatter(x_pos, y_pos, s=star['size'] * 12, c=THEME['black_hole_glow'],
                   marker='o', alpha=0.4, zorder=2)
        ax.scatter(x_pos, y_pos, s=star['size'] * 10, facecolors='none',
                   edgecolors=THEME['black_hole_edge'], linewidth=2,
                   marker='o', zorder=3)
        ax.scatter(x_pos, y_pos, s=star['size'] * 6, c=THEME['background'],
                   marker='o', edgecolors=THEME['black_hole_edge'], linewidth=1,
                   zorder=4)
        edgecolor = THEME['black_hole_edge']
        linewidth = 2
    elif star['name'] == "Sol":
        # Use original star color with theme edge
        ax.scatter(x_pos, y_pos, s=star['size'] * 10, c=star['color'],
                   marker='o', edgecolors=THEME['sol_edge'], linewidth=2,
                   zorder=3, alpha=0.8)
        edgecolor = THEME['sol_edge']
        linewidth = 2
    else:
        # Regular stars - use original colors with appropriate edges
        # Check if star has custom edge color (like Albireo's blue ring)
        if 'edge_color' in star:
            edgecolor = star['edge_color']
            linewidth = 3  # Thicker ring for custom edge colors
        else:
            edgecolor = THEME['text'] if star['color'] in ['#000000', '#FFFFFF'] else THEME['text']
            linewidth = 1
        ax.scatter(x_pos, y_pos, s=star['size'] * 10, c=star['color'],
                   marker='o', edgecolors=edgecolor, linewidth=linewidth,
                   zorder=3, alpha=0.8)

    # Add label - uniform format with spaces
    label = f"{star['name'].strip()} ({star['distance']} ly) {star['tarot']} {star['roman']}"

    # Larger offset for black hole to avoid text touching symbol
    offset = 36 if star['name'] == 'Sagittarius A*' else 16

    ax.annotate(label, (x_pos, y_pos), xytext=(offset, 0),
                textcoords='offset points', va='center', ha='left',
                fontsize=10, color=THEME['text'], fontfamily='DejaVu Sans')


def setup_plot_appearance(ax):
    """
    Configure plot appearance, axes, and styling.
    """
    # Set plot limits
    ax.set_xlim(-2.4, 3.2)
    ax.set_ylim(-0.8, 0.8)

    # X-axis categories represent distance to the GC-Sol-GAC line
    x_ticks = [-2, -1, -0.5, 0, 0.5, 1, 2]
    ax.set_xticks([])
    ax.set_yticks([])

    # Add vertical grid lines for X-axis categories
    for x_val in x_ticks:
        if x_val == 0:
            ax.axvline(x=x_val, color='#FFD700', alpha=0.8, linestyle='--', linewidth=0.5)
        else:
            ax.axvline(x=x_val, color=THEME['grid'], alpha=0.3, linestyle='-', linewidth=0.5)

    # Labels and title with specific font family
    ax.set_ylabel('(GAC ← → GC) Ordinal Position by Galactic Longitude', color=THEME['text'], fontsize=12,
                  fontfamily='sans-serif')

    # Manually place the X-axis label centered at X=0
    ax.text(0, -0.685, 'Milky Way Rotation Direction', color=THEME['text'], fontsize=10,
            ha='center', va='top', fontfamily='sans-serif')

    ax.set_title('Cygni Arcana — Stars Mapped to Tarot by Galactic Geometry',
                 color=THEME['text'], fontsize=14, fontweight='bold', fontfamily='sans-serif')

    # Add curved arrow showing galactic rotation direction
    from matplotlib.patches import FancyArrowPatch

    # The arrow is colored gold and dashed
    arrow = FancyArrowPatch((-1.5, -0.65), (1.5, -0.65),
                            connectionstyle="arc3,rad=0.05",
                            arrowstyle='<-', mutation_scale=20,
                            color='#FFD700', alpha=0.6, linewidth=1, linestyle='--')
    ax.add_patch(arrow)

    # Labels with Unicode symbols
    # GC Label
    ax.text(0, 0.76, "⚛︎ GC", ha='center', va='center', fontsize=14, fontweight='bold',
            color='#FFD700', fontfamily='sans-serif')

    # GAC label
    ax.text(0, -0.75, "☆ GAC", ha='center', va='center', fontsize=14, fontweight='bold',
            color='#FFD700', fontfamily='sans-serif')


def create_cygni_arcana_plot():
    """
    Create and display the Cygni Tarot plot.
    """
    # Create figure with theme background
    fig, ax = plt.subplots(figsize=(16, 12), facecolor=THEME['background'])
    ax.set_facecolor(THEME['background'])

    # Plot all stars
    for star in STARS:
        plot_star(ax, star, STARS)

    # Setup plot appearance
    setup_plot_appearance(ax)

    # Finalize and save
    plt.tight_layout()
    mode_suffix = '_dark' if DARK_MODE else '_light'

    # Create output directory and save
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file_path = OUTPUT_DIR / f'cygni_arcana_plot{mode_suffix}.png'
    plt.savefig(output_file_path, dpi=300, bbox_inches='tight',
                facecolor=THEME['background'])
    plt.show()


# Main execution
if __name__ == "__main__":
    create_cygni_arcana_plot()