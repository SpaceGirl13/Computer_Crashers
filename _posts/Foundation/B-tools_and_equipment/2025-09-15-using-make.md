---
title: "Using Make"
date: 2025-09-15
author: ComputerCrashers
tags: ["tools", "setup", "vscode", "git", "learning-experience-design"]
permalink: /lxd/setup/make
---

# Introduction to GNU Make: How It Works and Basic Commands

When working on software projects, you often need to compile code, run tests, or automate repetitive tasks. Doing these steps manually can be tedious and error-prone. This is where **GNU Make** comes in. It's a powerful build automation tool that helps developers define and run tasks in a structured way.

---

## What is Make?

**Make** is a build automation tool that reads instructions from a file called a **Makefile**. It uses these instructions to figure out:

- What needs to be built.
- The dependencies between files.
- The commands required to build them.

Originally designed to compile programs from source code, `make` is now used for a wide range of tasks: generating documents, switching site themes, running tests, and more.

---

## How Make Works

At its core, Make relies on **rules** written in a `Makefile`. A rule usually has three parts:

```make
target: dependencies
    command
```

- **target** → the file or action to produce (e.g., an executable).
- **dependencies** → the files the target depends on (e.g., source code).
- **command** → the shell command(s) used to create the target.

Make works by checking timestamps:

- If the target doesn't exist, or if any of its dependencies have changed since the last build, the command is executed.
- Otherwise, it skips rebuilding that target.

---

## Using Make for GitHub Pages Themes

When you're working with a Jekyll-based site (like GitHub Pages), make can also automate switching themes and running your site locally.

For example, suppose your Makefile looks like this:

```make
THEME ?= cayman

serve:
    bundle exec jekyll serve --theme $(THEME)

build:
    bundle exec jekyll build --theme $(THEME)

clean:
    rm -rf _site

help:
    @echo "make serve THEME=<theme>  - Serve site with a theme (cayman, midnight, minima, etc.)"
    @echo "make build THEME=<theme>  - Build static site with the given theme"
    @echo "make clean                - Remove generated site files"
    @echo "make help                 - Show available commands"
```

### Switching Themes

You can quickly change the look of your site by passing a theme variable:

```bash
make serve THEME=cayman
make serve THEME=midnight
make serve THEME=minima
```

Each time you run the command, Jekyll will serve the site with the specified theme, making it easy to preview different styles.

---

## Common Make Commands

Here are some essential commands to use with the example above:

**Show help:**
```bash
make help
```

**Serve the site with the Cayman theme:**
```bash
make serve THEME=cayman
```

**Serve the site with the Midnight theme:**
```bash
make serve THEME=midnight
```

**Build the site for deployment:**
```bash
make build THEME=minima
```

**Clean up generated files:**
```bash
make clean
```

---

## Why This Works Well

- **Consistency** → Every developer uses the same commands.
- **Flexibility** → You can preview multiple themes without editing configuration files.
- **Automation** → Switching, building, and cleaning are all one-liners.

---

## Conclusion

GNU Make is not just for compiling programs—it's also great for managing tasks in web projects. By writing rules in a Makefile, you can easily switch themes, build your site, or serve it locally with one command. Whether you're testing out the Cayman theme or experimenting with Midnight, make helps keep your workflow simple and efficient.