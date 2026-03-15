import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const projects = defineCollection({
  loader: glob({ base: "./src/content/projects", pattern: "**/*.md" }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      year: z.number(),
      stack: z.array(z.string()),
      context: z.enum(["course", "independent"]).optional(),
      course_name: z.string().optional(),
      course_role: z.enum(["capstone", "homework"]).optional(),
      summary: z.string().optional(),
      tags: z.array(z.string()).optional(),
      snapshot: image().optional(),
      architecture_diagram: image().optional(),
      video_url: z.url().optional(),
      repo: z.url().optional(),
      authors: z.array(z.string()).optional(),
    }),
});

const publications = defineCollection({
  loader: glob({ base: "./src/content/publications", pattern: "**/*.md" }),
  schema: z.object({
    title: z.string(),
    year: z.number(),
    journal: z.string(),
    authors: z.array(z.string()),
    summary: z.string().optional(),
    link: z.url().optional(),
    featured: z.boolean().default(false),
    type: z.enum(["peer-reviewed", "preprint"]),
  }),
});

export const collections = {
  projects,
  publications,
};
