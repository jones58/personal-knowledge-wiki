import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  integrations: [starlight({
    title: "My Knowledge Wiki",
    social: {
      github: "https://github.com/withastro/starlight"
    },
    sidebar: [{
      label: "Reference",
      autogenerate: {
        directory: "reference"
      }
    }]
  }), sitemap()]
});