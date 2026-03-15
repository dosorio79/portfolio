const base = import.meta.env.BASE_URL;
const basePath = base.endsWith("/") ? base : `${base}/`;

export const withBase = (path: string) =>
  `${basePath}${path.replace(/^\/+/, "")}`;

export const normalizePath = (path: string) =>
  path.replace(/\/+$/, "") || "/";

export const stripBase = (path: string) =>
  path.startsWith(basePath) ? `/${path.slice(basePath.length)}` : path;

export const withAssetBase = (path: string) =>
  path.startsWith("http") ? path : withBase(path);
