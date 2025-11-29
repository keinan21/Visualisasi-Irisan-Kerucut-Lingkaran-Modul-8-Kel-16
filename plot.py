import matplotlib.pyplot as plt

def gambarGrafik(x, y, radius,):

    plt.style.use('dark_background')

    fig, ax = plt.subplots()
    ax.grid(True)
    circle = plt.Circle((x, y), radius, color='red', fill=False, linewidth=2, zorder=10)
    ax.add_artist(circle)

    ax.set_xlim(x - radius - 1, x + radius + 1)
    ax.set_ylim(y - radius - 1, y + radius + 1)
    ax.set_aspect('equal')
    
    ax.set_title('Grafik Lingkaran')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    fig.savefig("hasil.png", dpi=150)
    plt.close(fig)
