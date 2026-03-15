# Portfolio 🌿

A modern, minimalist portfolio website built with Astro. This static site showcases projects and content with a focus on performance, simplicity, and maintainability.

[![CI](https://github.com/dosorio79/portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/dosorio79/portfolio/actions/workflows/ci.yml)
[![Pages](https://github.com/dosorio79/portfolio/actions/workflows/pages.yml/badge.svg)](https://github.com/dosorio79/portfolio/actions/workflows/pages.yml)
[![Astro](https://img.shields.io/badge/Astro-6.0-BC52EE?logo=astro&logoColor=white)](https://astro.build)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.2-38B2AC?logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![Node.js](https://img.shields.io/badge/Node-22.12%2B-339933?logo=node.js&logoColor=white)](https://nodejs.org)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-222?logo=github&logoColor=white)](https://pages.github.com)
[![MIT License](https://img.shields.io/badge/Code%20License-MIT-0b7?logo=opensourceinitiative&logoColor=white)](LICENSE)
[![CC BY-NC-ND 4.0](https://img.shields.io/badge/Content%20License-CC%20BY--NC--ND%204.0-03c?logo=creativecommons&logoColor=white)](CONTENT_LICENSE.md)

## 🚀 Tech Stack

- **[Astro](https://astro.build)** - Static site generator for content-focused websites
- **[Tailwind CSS](https://tailwindcss.com)** - Utility-first CSS framework via the Vite plugin
- **[TypeScript](https://www.typescriptlang.org)** - Type-safe JavaScript
- **[Fontsource](https://fontsource.org/)** - Self-hosted web fonts
- **Markdown** - Content authoring

## ✨ Features

- ⚡ Static site generation with Astro
- 🎨 Tailwind CSS 4 for styling with the typography plugin
- 📝 Content authored in Markdown
- 🖼️ Astro asset pipeline for optimized local images
- 🗺️ Automatic sitemap generation for GitHub Pages
- 🔗 Internal link validation
- 📱 Responsive design
- ♿ Accessibility-focused

## 📂 Project Structure

```text
/ 
├── public/          # Static files copied as-is
├── src/
│   ├── assets/      # Optimized local images
│   ├── content/     # Markdown content files
│   └── pages/       # Astro pages and routes
├── scripts/         # Build and utility scripts
└── package.json
```

## 🛠️ Commands

All commands are run from the root of the project:

This project targets Node.js `22.12.0` or newer.

Use `nvm use` if you have `nvm` installed.

| Command               | Action                                      |
| :-------------------- | :------------------------------------------ |
| `npm install`         | Install dependencies                        |
| `npm run dev`         | Start local dev server at `localhost:4321`  |
| `npm run build`       | Build the production site to `./dist/`      |
| `npm run preview`     | Preview the build locally                   |
| `npm run check`       | Run Astro content/type checks               |
| `npm run check:links` | Check internal links in generated HTML      |

## 🚀 Deployment

Deployed via GitHub Pages at https://dosorio79.github.io/portfolio/.

The current released version is `v0.1.0`.

## 📄 License

Code is licensed under the MIT License. Content is licensed under
Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
See `LICENSE` and `CONTENT_LICENSE.md`.
