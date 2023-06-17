/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('autoprefixer'),
    require('flowbite/plugin'),
    require('postcss-nesting'),
    require('tailwindcss-debug-screens'),
  ],
}

