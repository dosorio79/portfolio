# Portfolio

Personal portfolio site built with Astro. Static, content-first, and minimal.

## Features

- Static site generation with Astro
- Tailwind for styling
- Content authored in Markdown
- Sitemap generation for GitHub Pages

## Project Structure

```text
/
├── public/
├── src/
│   ├── content/
│   └── pages/
├── scripts/
└── package.json
```

## Commands

All commands are run from the root of the project:

| Command            | Action                                           |
| :----------------- | :----------------------------------------------- |
| `npm install`      | Install dependencies                             |
| `npm run dev`      | Start local dev server at `localhost:4321`       |
| `npm run build`    | Build the production site to `./dist/`           |
| `npm run preview`  | Preview the build locally                        |
| `npm run check`    | Run Astro content/type checks                    |
| `npm run check:links` | Check internal links in generated HTML        |
