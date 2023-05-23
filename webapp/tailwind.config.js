/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/{lib,routes}/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      opacity: {
        '35': '0.35'
      }
    },
  },
  plugins: [],
  safelist: [
    {
      pattern: /bg-(red|green|pink|orange)-(100|500|700)/,
      variants: ['lg', 'hover', 'focus', 'lg:hover'],
    },
    {
      pattern: /accent-(red|green|pink|orange)-(100|500|700)/,
      variants: ['lg', 'hover', 'focus', 'lg:hover'],
    },
  ],
}
