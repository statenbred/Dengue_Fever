# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands
- Run Jupyter notebook: `jupyter notebook [filename].ipynb`
- Lint Python code: `flake8`
- Check types: `mypy`

## Code Style Guidelines
- Import order: standard library, third-party packages, local modules
- Use pandas for data manipulation and analysis
- Use matplotlib/seaborn for visualizations
- Format floating-point numbers to 2-3 decimal places in displays
- Variable naming: snake_case for variables, functions
- Split large dataframe operations into logical chunks with comments
- Document data transformation steps clearly
- For modeling: handle missing values, document feature engineering

## Data Structure
- Two cities: San Juan (sj), Iquitos (iq) with different patterns
- Target: predict total_cases of dengue fever
- Features: weather, precipitation, temperature, vegetation indices
- Time series data with weekly observations