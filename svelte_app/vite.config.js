import {defineConfig} from 'vite'
import {svelte} from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [svelte({
        // compilerOptions: {
        //     cssOutputFilename: 'spa.css'
        // },
    })],
    // assetsInclude: ["**/static/spa/*"],
    base: "/static/spa",
    build: {
        outDir: "../static/spa",
        assetsDir: './assets',
        // makeAbsoluteExternalsRelative: true,
        rollupOptions: {
            output: {
                entryFileNames: '[name].js',
                assetFileNames: '[name].[ext]',
            },
        },
    }
})
