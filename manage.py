import os
import sys


def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "social_media.settings"
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django import nahi ho raha. "
            "Check karo Django installed hai ya nahi."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()