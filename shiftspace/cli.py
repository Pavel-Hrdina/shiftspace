import argparse


def cmdline_args():
    """_summary_

    _extended_summary_
    """
    parser = argparse.ArgumentParser(
        description="A Python package, that creates a reproducible workspace",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("path")


if __name__ == "__manin__":
    cmdline_args()
