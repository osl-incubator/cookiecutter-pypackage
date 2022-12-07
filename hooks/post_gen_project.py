#!/usr/bin/env python
import os
import shutil
import subprocess
from pathlib import Path

PROJECT_DIRECTORY = Path(os.path.abspath(os.path.curdir)).resolve()

UNUSED_DOCS_DIRS = [
    PROJECT_DIRECTORY / 'docs-mkdocs',
    PROJECT_DIRECTORY / 'docs-sphinx',
    PROJECT_DIRECTORY / 'docs-jupyter-book'
]

DOCUMENTATION_ENGINE = ""

{% if cookiecutter.documentation_engine == 'mkdocs' -%}
DOCS_SPEC_DIR = UNUSED_DOCS_DIRS.pop(0)
DOCUMENTATION_ENGINE = "mkdocs"
{%- elif cookiecutter.documentation_engine == 'sphinx' -%}
DOCS_SPEC_DIR = UNUSED_DOCS_DIRS.pop(1)
DOCUMENTATION_ENGINE = "sphinx"
{%- elif cookiecutter.documentation_engine == 'jupyter-book' -%}
DOCS_SPEC_DIR = UNUSED_DOCS_DIRS.pop(2)
DOCUMENTATION_ENGINE = "jupyter-book"
{% endif %}


def remove_unused_docs_dirs(dirs: list=UNUSED_DOCS_DIRS):
    for dirs in dirs:
        shutil.rmtree(dirs)


def remove_file(filepath: str):
    os.remove(PROJECT_DIRECTORY / filepath)


def move_selected_doc_dir():
    docs_target_dir = PROJECT_DIRECTORY / "docs"
    for file_name in os.listdir(DOCS_SPEC_DIR):
        shutil.move(DOCS_SPEC_DIR / file_name, docs_target_dir)

    if DOCUMENTATION_ENGINE == "sphinx":
        remove_file("docs/index.md")

    shutil.rmtree(DOCS_SPEC_DIR)


def http2ssh(url):
    url = url.replace("https://", "git@")
    return url.replace("/", ":", 1)


def post_gen():
    remove_unused_docs_dirs()
    move_selected_doc_dir()

    subprocess.call(["git", "init"])

    git_https_origin = http2ssh("{{cookiecutter.git_https_origin}}")
    git_https_upstream = http2ssh("{{cookiecutter.git_https_upstream}}")
    git_main_branch = http2ssh("{{cookiecutter.git_main_branch}}")
    git_new_branch = "add-initial-structure"

    if git_https_origin != "":
        subprocess.call(["git", "remote", "add", "origin", git_https_origin])
        subprocess.call(["git", "fetch", "--all"])

    if git_https_upstream != "":
        subprocess.call(
            ["git", "remote", "add", "upstream", git_https_upstream]
        )
        subprocess.call(["git", "checkout", f"upstream/{git_main_branch}"])
        subprocess.call(["git", "fetch", "--all"])

    subprocess.call(
        ["git", "config", "user.name", "{{cookiecutter.author_full_name}}"]
    )
    subprocess.call(
        ["git", "config", "user.email", "{{cookiecutter.author_email}}"]
    )

    subprocess.call(["git", "checkout", "-b", git_new_branch])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "Initial commit"])


if __name__ == "__main__":
    post_gen()
