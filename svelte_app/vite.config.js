import {defineConfig} from 'vite'
import {svelte} from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [svelte()],
    // параметр base определят директорию прямой ссылки на статические файлы (используется при разыменовывании относительных ссылок в скриптах)
    base: "/static/spa",
    build: {
        //сюда будем выкладывать артефакты
        outDir: "../static/spa",
        //сюда картинки и прочее midia
        assetsDir: './assets',

        rollupOptions: {
            output: {
                //название главного файла javascript
                entryFileNames: '[name].js',
                //название остальных файлов. Если не прописать, то к имени будет дописывать случайный id
                assetFileNames: '[name].[ext]',
            },
        },
    }
})
