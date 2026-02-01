import { defineCollection, z } from "astro:content";

const projects = defineCollection({
  schema: z.object({
    title: z.string(),
    year: z.number(),
    stack: z.array(z.string()),
    context: z.enum(["course", "independent"]).optional(),
    course_name: z.string().optional(),
    summary: z.string().optional(),
    repo: z.string().url().optional(),
    authors: z.array(z.string()).optional(),
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
