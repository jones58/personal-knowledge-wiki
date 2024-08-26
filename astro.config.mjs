import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import sitemap from "@astrojs/sitemap";
import starlightThemeRapide from "starlight-theme-rapide";

// https://astro.build/config
export default defineConfig({
  site: "https://knowledgewiki.jackkershaw.net",
  description:
    "This is my personal wiki, with all the links and notes that I find useful.",
  integrations: [
    starlight({
      plugins: [starlightThemeRapide()],
      logo: {
        src: "/public/favicon.svg",
      },
      title: "My Knowledge Wiki",
      social: {
        github: "https://github.com/jones58/personal-knowledge-wiki",
      },
      editLink: {
        baseUrl:
          "https://github.com/jones58/personal-knowledge-wiki/edit/main/",
      },
      sidebar: [
        {
          label: "Reference",
          autogenerate: {
            directory: "reference",
          },
        },
      ],
    }),
    sitemap(),
  ],
});
