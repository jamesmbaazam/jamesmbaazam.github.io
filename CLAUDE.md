# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal academic/professional website built with Quarto. The site showcases research, publications, open-source projects, teaching materials, and blog posts related to infectious disease modeling and epidemiological analytics.

The site is published at https://jamesmbaazam.github.io using GitHub Pages.

## Tech Stack

- **Quarto**: Static site generator for the website
- **R**: Primary programming language for blog posts and computational content
- **renv**: R package dependency management
- **GitHub Actions**: CI/CD pipeline for automated publishing

## Repository Structure

- `_quarto.yml`: Main Quarto configuration file
- `index.qmd`: Homepage
- `blog.qmd`: Blog listing page
- `blog/`: Individual blog posts (each in its own subdirectory with `index.qmd`)
  - `blog/epinow2-eval-guide/`: Guide on evaluating EpiNow2 model runs
  - `blog/julia-sugar-vs-r/`: Comparison of Julia and R syntax
- `research_projects.qmd`: Research and publications page
- `opensource_projects.qmd`: Open-source projects page
- `teaching.qmd`: Teaching materials page
- `images/`: Static images for the site
- `styles.css`: Custom CSS styles
- `_extensions/`: Quarto extensions (e.g., auto-dark mode)
- `docs/`: Output directory for rendered site (published to GitHub Pages)
- `renv/`: R package environment (managed by renv)
- `renv.lock`: Locked R package dependencies

## Development Commands

### Preview the website locally
```bash
quarto preview
```

### Render the entire website
```bash
quarto render
```

### Render a specific page
```bash
quarto render index.qmd
quarto render blog/epinow2-eval-guide/index.qmd
```

### Working with R dependencies

Initialize or restore R environment:
```r
# In R console
renv::restore()
```

Install new R packages:
```r
# In R console
install.packages("package_name")
renv::snapshot()  # Update renv.lock after installing
```

## Blog Post Structure

Blog posts are written in Quarto markdown (`.qmd`) files located in subdirectories under `blog/`. Each post typically includes:

- YAML frontmatter with metadata (title, author, date, categories, ORCID)
- R code chunks (often with caching enabled via `freeze: true` for computationally intensive content)
- Categories include: forecasting, EpiNow2, Bayesian Analysis, Reproduction numbers, R, Stan, Julia

Blog posts often use R packages like:
- EpiNow2 (epidemiological nowcasting/forecasting)
- data.table, dplyr (data manipulation)
- ggplot2 (visualization)
- bayesplot, posterior (Bayesian analysis)
- scoringutils (forecast evaluation)

## Publishing Workflow

The site is automatically built and published to GitHub Pages on every push to `main` branch via `.github/workflows/quarto-publish.yml`. The workflow:

1. Sets up Quarto (pre-release version)
2. Sets up R
3. Restores R environment using renv
4. Installs system dependency (GLPK for igraph package)
5. Renders and publishes to `gh-pages` branch

## Key Configuration Details

- **Output directory**: `docs/` (configured in `_quarto.yml`)
- **R version**: 4.5.1 (as specified in `renv.lock`)
- **Theme**: cosmo (light), darkly (dark mode)
- **Auto-dark filter**: Automatically switches between light/dark themes
- **Site navigation**: Top navbar with Home, Research, Open-source Projects, Teaching, Blog
- **Social links**: Twitter, GitHub, LinkedIn, Google Scholar, Email

## Important Notes

- The site uses `renv` for R package management. Always run `renv::restore()` when setting up a new environment.
- Blog posts with computationally intensive code use `freeze: true` to cache results and avoid re-execution on every render.
- The GitHub Actions workflow requires GLPK to be installed for the igraph R package dependency.
- The output directory is `docs/` (not the default `_site/`), which is configured for GitHub Pages publishing.
