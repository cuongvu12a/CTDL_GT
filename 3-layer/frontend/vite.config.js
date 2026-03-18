import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    proxy: {
      "/items": "http://api:3000",
      "/health": "http://api:3000",
    },
  },
});
