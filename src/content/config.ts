import { defineCollection, z } from "astro:content";

const projects = defineCollection({
  schema: z.object({
    title: z.string(),
    year: z.number(),
    stack: z.array(z.string()),
    impact: z.string().optional(),
  }),
});

const publications = defineCollection({
  schema: z.object({
    title: z.string(),
    year: z.number(),
    journal: z.string(),
    authors: z.array(z.string()),
    link: z.string().url().optional(),
    featured: z.boolean().default(false),
    type: z.enum(["peer-reviewed", "preprint"]),
  }),
});

export const collections = {
  projects,
  publications,
};
