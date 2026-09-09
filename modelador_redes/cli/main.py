# SPDX-License-Identifier: GPL-3.0-or-later
"""CLI `modelador`: build · check · zip · indice."""

from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="modelador", description="Modelador de Redes — generador del catálogo")
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build", help="genera public/ y data/ (solo en main)")
    p_build.add_argument("--target", choices=["all", "catalogo", "foss"], default="all")

    sub.add_parser("check", help="valida public/, enlaces, tamaños y la línea Draft vigente")

    p_zip = sub.add_parser("zip", help="regenera solo los zips de descarga")
    p_zip.add_argument("--modelo", help="id del modelo (por defecto todos)")

    p_ind = sub.add_parser("indice", help="escribe la línea «Draft vigente» en revision/00-indice.md")
    p_ind.add_argument("--modelo", required=True)
    p_ind.add_argument("--check", action="store_true", help="no escribe: exit 1 si está desfasada")

    args = parser.parse_args(argv)

    if args.command == "build":
        from modelador_redes.cli.build import run_build

        run_build(args.target)
        return 0
    if args.command == "check":
        from modelador_redes.cli.check import run

        return run()
    if args.command == "zip":
        from modelador_redes.cli.zip import run

        return run(args.modelo)
    if args.command == "indice":
        from modelador_redes.cli.indice import run

        return run(args.modelo, args.check)
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
