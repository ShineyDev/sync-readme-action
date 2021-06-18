import argparse
import asyncio
import sys
import textwrap
import traceback


_printers = list()


def _create_printer(level, prefix, suffix, *, stream=None):
    def printer(*args, **kwargs):
        if not printer.is_active:
            return

        if args and isinstance(args[-1], BaseException):
            *args, e = args
            args += ("See the error output below.",)
        else:
            e = None

        file = kwargs.pop("file", stream) or sys.stdout
        sep = kwargs.pop("sep", " ")

        s = prefix + sep.join(o if isinstance(o, str) else repr(o) for o in args) + suffix

        if e is not None:
            s += "\n\n" + textwrap.indent(
                "".join(traceback.format_exception(type(e), e, e.__traceback__)),
                "    ",
            )

        print(s, file=file, **kwargs)

    printer.level = level
    printer.is_active = False

    _printers.append(printer)

    return printer


print_debug = _create_printer(4, "\x1B[32m[DEBUG]\x1B[39m ", "")
print_info = _create_printer(3, "\x1B[34m[INFO]\x1B[39m ", "")
print_warning = _create_printer(2, "\x1B[33m[WARNING]\x1B[39m ", "")
print_error = _create_printer(1, "\x1B[31m[ERROR] ", "\x1B[39m", stream=sys.stderr)


async def main(*, destination, source):
    print_debug(destination, source)

    return 0


async def main_catchall(*args, **kwargs):
    try:
        code = await main(*args, **kwargs)
    except BaseException as e:
        print_error(e)

        code = 1
    finally:
        return code


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", required=True, metavar="PATH")
    parser.add_argument("--source", required=True, metavar="PATH")
    parser.add_argument("--verbosity", required=True, type=int, metavar="0-4")
    kwargs = vars(parser.parse_args())

    verbosity = kwargs.pop("verbosity")
    for printer in _printers:
        if verbosity >= printer.level:
            printer.is_active = True

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    exit(asyncio.run(main_catchall(**kwargs)))
