# Cygni Arcana
# Copyright (c) 2025 Oliver Staats
# This software is licensed for exclusive use by Oliver Staats. See LICENSE for details.
import matplotlib.pyplot as plt
import math

# Configuration
DARK_MODE = True  # Set to False for light mode

# Constants
GALACTIC_CENTER_DISTANCE = 26000

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

# Star data
STARS = [
    {"name": "Sagittarius A*", "distance": 26000, "longitude": 0, "size": 60,
     "tarot": "Wheel of Fortune", "roman": "X", "d_GC": 0,
     "color": "#000000", "tarot_highlight": "#4B0082"},

    {"name": "Sol", "distance": 0, "longitude": 0, "size": 40,
     "tarot": "The Sun", "roman": "XIX", "d_GC": 26000,
     "color": "#FFFF00", "tarot_highlight": "#FFD700"},

    {"name": "T Coronae Borealis", "distance": 3000, "longitude": 55, "size": 30,
     "tarot": "Judgment", "roman": "XX", "d_GC": 18000,
     "color": "#FFFFFF", "tarot_highlight": "#FFA500"},

    {"name": "Sheliak", "distance": 960, "longitude": 63, "size": 25,
     "tarot": "The Moon", "roman": "XVIII", "d_GC": 25040,
     "color": "#1C1CF0", "tarot_highlight": "#000080"},

    {"name": "Antares", "distance": 550, "longitude": 351, "size": 50,
     "tarot": "The Hierophant", "roman": "V", "d_GC": 25450,
     "color": "#FF4500", "tarot_highlight": "#8B4513"},

    {"name": "Deneb", "distance": 1500, "longitude": 80, "size": 50,
     "tarot": "The High Priestess", "roman": "II", "d_GC": 25780,
     "color": "#CFE2F3", "tarot_highlight": "#4B0082"},

    {"name": "Polaris", "distance": 433, "longitude": 123, "size": 25,
     "tarot": "The Hermit", "roman": "IX", "d_GC": 25567,
     "color": "#F0E68C", "tarot_highlight": "#ADD8E6"},

    {"name": "Albireo", "distance": 430, "longitude": 62, "size": 25,
     "tarot": "The Lovers", "roman": "VI", "d_GC": 25570,
     "color": "#FFD700", "tarot_highlight": "#FF69B4"},

    {"name": "Spica", "distance": 250, "longitude": 316, "size": 25,
     "tarot": "Strength", "roman": "VIII", "d_GC": 25750,
     "color": "#7B68EE", "tarot_highlight": "#808000"},

    {"name": "Achernar", "distance": 139, "longitude": 290, "size": 25,
     "tarot": "The Hanged Man", "roman": "XII", "d_GC": 25862,
     "color": "#00BFFF", "tarot_highlight": "#90EE90"},

    {"name": "Zubenelgenubi", "distance": 77, "longitude": 347, "size": 25,
     "tarot": "Justice", "roman": "XI", "d_GC": 25923,
     "color": "#FFFFE0", "tarot_highlight": "#C0C0C0"},

    {"name": "Arcturus", "distance": 36.7, "longitude": 15, "size": 30,
     "tarot": "The Magician", "roman": "I", "d_GC": 25963,
     "color": "#FF8C00", "tarot_highlight": "#FFA500"},

    {"name": "Fomalhaut", "distance": 25, "longitude": 20, "size": 20,
     "tarot": "The Star", "roman": "XVII", "d_GC": 25975,
     "color": "#FFFFFF", "tarot_highlight": "#87CEFA"},

    {"name": "Vega", "distance": 25, "longitude": 67, "size": 20,
     "tarot": "The Empress", "roman": "III", "d_GC": 25975,
     "color": "#E0FFFF", "tarot_highlight": "#228B22"},

    {"name": "Alpha Centauri", "distance": 4.37, "longitude": 315, "size": 20,
     "tarot": "The World", "roman": "XXI", "d_GC": 25996,
     "color": "#FFD700", "tarot_highlight": "#8B4513"},

    {"name": "Sirius", "distance": 8.6, "longitude": 227, "size": 20,
     "tarot": "The Fool", "roman": "0", "d_GC": 26008,
     "color": "#ADD8E6", "tarot_highlight": "#00BFFF"},

    {"name": "Tau Ceti", "distance": 12, "longitude": 172, "size": 20,
     "tarot": "Temperance", "roman": "XIV", "d_GC": 26012,
     "color": "#F5DEB3", "tarot_highlight": "#87CEEB"},

    {"name": "Capella", "distance": 42.9, "longitude": 162, "size": 25,
     "tarot": "The Chariot", "roman": "VII", "d_GC": 26042,
     "color": "#FFDAB9", "tarot_highlight": "#808080"},

    {"name": "Regulus", "distance": 79, "longitude": 226, "size": 25,
     "tarot": "The Emperor", "roman": "IV", "d_GC": 26078,
     "color": "#A9A9F5", "tarot_highlight": "#800000"},

    {"name": "Algol", "distance": 93, "longitude": 151, "size": 25,
     "tarot": "The Devil", "roman": "XV", "d_GC": 26092,
     "color": "#FF6347", "tarot_highlight": "#8B0000"},

    {"name": "Mira", "distance": 420, "longitude": 171, "size": 30,
     "tarot": "Death", "roman": "XIII", "d_GC": 26420,
     "color": "#FF4500", "tarot_highlight": "#4B0082"},

    {"name": "Betelgeuse", "distance": 642, "longitude": 199, "size": 50,
     "tarot": "The Tower", "roman": "XVI", "d_GC": 26641,
     "color": "#FF4500", "tarot_highlight": "#FF0000"},

    # Minor Arcana suits
    {"name": "Eltanin", "distance": 154, "longitude": 94, "size": 25,
     "tarot": "Wands", "roman": "♣", "d_GC": 26154,
     "color": "#FF4500", "tarot_highlight": "#FF4500"},

    {"name": "Thuban", "distance": 309, "longitude": 96, "size": 25,
     "tarot": "Cups", "roman": "♥", "d_GC": 26309,
     "color": "#ADD8E6", "tarot_highlight": "#87CEEB"},

    {"name": "Algenib", "distance": 390, "longitude": 162, "size": 25,
     "tarot": "Swords", "roman": "♠", "d_GC": 26390,
     "color": "#FFD700", "tarot_highlight": "#4682B4"},

    {"name": "Markab", "distance": 140, "longitude": 139, "size": 25,
     "tarot": "Pentacles", "roman": "♦", "d_GC": 26140,
     "color": "#228B22", "tarot_highlight": "#228B22"},
]


def galactic_to_cartesian_x(distance, longitude_deg):
    """
    Convert galactic polar coordinates (distance, longitude) relative to Sol
    into perpendicular distance from GC-Sol-GAC line.

    Galactic longitude = 0° points from Sol towards GC.
    Returns the perpendicular offset from the GC-Sol-GAC line.
    """
    # Convert longitude to radians
    angle_rad = math.radians(longitude_deg)

    # Calculate perpendicular distance from GC-Sol-GAC line
    perpendicular_distance = distance * math.sin(angle_rad)

    return perpendicular_distance


def categorize_distance_from_line(perpendicular_distance):
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
    if abs_distance < 12:  # Close to the GC-Sol-GAC line
        if abs_distance < 1:
            return 0  # Essentially on the line (center)
        else:
            return sign * 0.5  # Slightly off line (near_ahead/near_behind)
    elif abs_distance < 70:
        return sign * 1  # Moderate distance from line (ahead/behind)
    else:
        return sign * 2  # Far from line (far_ahead/far_behind)


def calculate_y_position(d_gc, star_name):
    """
    Calculate Y position based on ORDINAL RANKING by distance from Galactic Center.

    The Y-axis represents approximate relative distance from GC, not exact distance.
    Stars are positioned based on their rank order when sorted by d_GC value.

    Args:
        d_gc (float): Distance from Galactic Center (used for sorting only)
        star_name (str): Name of the star

    Returns:
        float: Y position for plotting (ordinal-based, not distance-based)
    """
    # Sort all stars by d_GC to determine ordinal ranking
    stars_sorted = sorted(STARS, key=lambda x: x['d_GC'])

    # Special reference points
    if star_name == "Sagittarius A*":
        return 0.7  # GC at top (closest to GC)
    elif star_name == "Sol":
        return 0  # Sol at middle reference point

    # Stars closer to GC than Sol (positioned above Sol based on rank order)
    elif d_gc < GALACTIC_CENTER_DISTANCE:
        closer_stars = [s for s in stars_sorted
                        if s['d_GC'] < GALACTIC_CENTER_DISTANCE and s['name'] != "Sagittarius A*"]

        if star_name in [s['name'] for s in closer_stars]:
            # Find ordinal position in the sorted list
            ordinal_idx = [s['name'] for s in closer_stars].index(star_name)
            total_closer = len(closer_stars)
            # Reverse order: stars closest to GC get highest Y positions
            reversed_ordinal = total_closer - 1 - ordinal_idx
            return 0.1 + (reversed_ordinal / (total_closer - 1)) * 0.47 if total_closer > 1 else 0.35

    # Stars further from GC than Sol (positioned below Sol based on rank order)
    else:
        further_stars = [s for s in stars_sorted if s['d_GC'] > GALACTIC_CENTER_DISTANCE]

        if star_name in [s['name'] for s in further_stars]:
            # Find ordinal position in the sorted list
            ordinal_idx = [s['name'] for s in further_stars].index(star_name)
            total_further = len(further_stars)
            # Normal order: stars closest to Sol get positions nearest to Sol
            return -0.1 - (ordinal_idx / (total_further - 1)) * 0.47 if total_further > 1 else -0.35


def plot_star(ax, star):
    """
    Plot a single star on the axes.

    Args:
        ax: Matplotlib axes object
        star (dict): Star data dictionary
    """
    # Calculate perpendicular distance from GC-Sol-GAC line
    perpendicular_distance = galactic_to_cartesian_x(star['distance'], star['longitude'])

    # Convert to category for x-position (flipped for display - ahead rotation gets negative plot_x)
    plot_x = categorize_distance_from_line(perpendicular_distance)

    # Y position represents ordinal ranking by distance from GC
    y_pos = calculate_y_position(star['d_GC'], star['name'])

    # Special handling for Sagittarius A* (black hole)
    if star['name'] == "Sagittarius A*":
        # Draw the event horizon as a ring with glow effect
        # Outer glow
        ax.scatter(plot_x, y_pos, s=star['size'] * 12, c=THEME['black_hole_glow'],
                   marker='o', alpha=0.4, zorder=2)
        # Inner event horizon ring
        ax.scatter(plot_x, y_pos, s=star['size'] * 10, facecolors='none',
                   edgecolors=THEME['black_hole_edge'], linewidth=2,
                   marker='o', zorder=3)
        # Central black hole
        ax.scatter(plot_x, y_pos, s=star['size'] * 6, c=THEME['background'],
                   marker='o', edgecolors=THEME['black_hole_edge'], linewidth=1,
                   zorder=4)
        edgecolor = THEME['black_hole_edge']
        linewidth = 2
    elif star['name'] == "Sol":
        # Use original star color with theme edge
        ax.scatter(plot_x, y_pos, s=star['size'] * 10, c=star['color'],
                   marker='o', edgecolors=THEME['sol_edge'], linewidth=2,
                   zorder=3, alpha=0.8)
        edgecolor = THEME['sol_edge']
        linewidth = 2
    else:
        # Regular stars - use original colors with appropriate edges
        edge_color = THEME['text'] if star['color'] in ['#000000', '#FFFFFF'] else THEME['text']
        ax.scatter(plot_x, y_pos, s=star['size'] * 10, c=star['color'],
                   marker='o', edgecolors=edge_color, linewidth=1,
                   zorder=3, alpha=0.8)
        edgecolor = edge_color
        linewidth = 1

    # Add label - uniform format with spaces
    label = f"{star['name'].strip()} ({star['distance']} ly) {star['tarot']} ({star['roman']})"

    # Larger offset for black hole to avoid text touching symbol
    offset = 36 if star['name'] == 'Sagittarius A*' else 16

    ax.annotate(label, (plot_x, y_pos), xytext=(offset, 0),
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
    ax.set_ylabel('(GAC ← → GC) Ordinal Distance Ranking', color=THEME['text'], fontsize=12, fontfamily='sans-serif')

    # Manually place the X-axis label centered at X=0
    ax.text(0, -0.685, 'Milky Way Rotation Direction', color=THEME['text'], fontsize=10,
            ha='center', va='top', fontfamily='sans-serif')

    ax.set_title('Cygni Arcana - Stars Mapped to Tarot Cards by Galactic Coordinates',
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
    # GC symbol
    ax.text(0, 0.76, "⚛︎ GC", ha='center', va='center', fontsize=14, fontweight='bold',
            color='#FFD700', fontfamily='sans-serif')

    # The GAC label
    ax.text(0, -0.75, "★ GAC", ha='center', va='bottom', fontsize=14, fontweight='bold',
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
        plot_star(ax, star)

    # Setup plot appearance
    setup_plot_appearance(ax)

    # Finalize and save
    plt.tight_layout()
    mode_suffix = '_dark' if DARK_MODE else '_light'
    plt.savefig(f'../../generated/cygni_arcana_plot{mode_suffix}.png', dpi=300, bbox_inches='tight',
                facecolor=THEME['background'])
    plt.show()


# Main execution
if __name__ == "__main__":
    create_cygni_arcana_plot()