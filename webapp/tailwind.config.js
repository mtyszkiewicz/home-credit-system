/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/{lib,routes}/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      opacity: {
        '40': '0.4'
      }
    },
  },
  plugins: [],
  safelist: [
    {
      pattern: /bg-(red|green|pink|orange)-(100|500|700)/, // You can display all the colors that you need
      variants: ['lg', 'hover', 'focus', 'lg:hover'],      // Optional
    },
  ],
}
