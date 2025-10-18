import argparse
import os

# Use a non-interactive backend by default (safe for headless runs).
# If --show is passed, matplotlib will switch to an interactive backend automatically on import.
import matplotlib

matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt


def compute_mandelbrot(
    width: int,
    height: int,
    x_center: float,
    y_center: float,
    zoom: float,
    max_iter: int,
):
    """
    Vectorized escape-time algorithm.
    Returns a 2D array of iteration counts.
    """
    # View window size scales with zoom (higher zoom => smaller window)
    span = 3.0 / zoom
    x_min, x_max = x_center - span / 2, x_center + span / 2
    y_min, y_max = y_center - span / 2, y_center + span / 2

    # Build complex plane grid
    xs = np.linspace(x_min, x_max, width, dtype=np.float64)
    ys = np.linspace(y_min, y_max, height, dtype=np.float64)
    X, Y = np.meshgrid(xs, ys)
    C = X + 1j * Y

    Z = np.zeros_like(C)
    iters = np.zeros(C.shape, dtype=np.uint16)
    mask = np.ones(C.shape, dtype=bool)

    for i in range(max_iter):
        # Z <- Z^2 + C only on points that are still bounded
        Z[mask] = Z[mask] * Z[mask] + C[mask]

        # Points that just escaped this iteration
        escaped = np.abs(Z) > 2.0
        just_escaped = escaped & mask
        iters[just_escaped] = i
        mask &= ~escaped

        if not mask.any():
            break

    # For points that never escaped, set to max_iter (gives the solid interior)
    iters[mask] = max_iter
    return iters


def render(
    iters: np.ndarray,
    cmap: str,
    output: str | None,
    show: bool,
):
    fig, ax = plt.subplots(figsize=(8, 6), dpi=120)
    im = ax.imshow(iters, cmap=cmap, origin="lower", interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Mandelbrot Set")

    # Add a small colorbar for didactic purposes
    cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Escape iteration")

    if output:
        os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
        plt.savefig(output, bbox_inches="tight")
        print(f"Saved image to {output}")

    if show:
        # Switch to default interactive backend if possible
        # (If running on a machine with display)
        plt.switch_backend(plt.get_backend())
        plt.show()


def build_argparser():
    p = argparse.ArgumentParser(description="Render a Mandelbrot image (demo for uv).")
    p.add_argument("--width", type=int, default=1200, help="Image width in px")
    p.add_argument("--height", type=int, default=900, help="Image height in px")
    p.add_argument("--x-center", type=float, default=-0.75, help="Center X")
    p.add_argument("--y-center", type=float, default=0.0, help="Center Y")
    p.add_argument("--zoom", type=float, default=1.0, help="Zoom factor (>1 zooms in)")
    p.add_argument("--max-iter", type=int, default=300, help="Max iterations")
    p.add_argument(
        "--cmap",
        default="turbo",
        help="Matplotlib colormap (e.g., viridis, magma, turbo)",
    )
    p.add_argument("--output", "-o", default="mandelbrot.png", help="Output PNG path")
    p.add_argument("--show", action="store_true", help="Show interactive figure")
    return p


def main():
    args = build_argparser().parse_args()
    iters = compute_mandelbrot(
        width=args.width,
        height=args.height,
        x_center=args.x_center,
        y_center=args.y_center,
        zoom=args.zoom,
        max_iter=args.max_iter,
    )
    render(iters, cmap=args.cmap, output=args.output, show=args.show)


if __name__ == "__main__":
    main()
