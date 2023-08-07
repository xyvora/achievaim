/* eslint-disable @typescript-eslint/no-var-requires */

module.exports = {
  purge: ['./src/**/*.svelte', './src/**/*.html'],
  darkMode: 'class', // or 'media'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [require('daisyui')],

  daisyui: {
    themes: [
      {
        light: {
          ...require('daisyui/src/theming/themes')['[data-theme=light]'],
          primary: '#198cff',
          'primary-focus': '#0072e5',
          'primary-content': '#f8f8f8',
          secondary: '#f38c24',
          'secondary-focus': '#da720b',
          'secondary-content': '#f8f8f8',
          accent: '#00feff',
          'accent-focus': '#00cbcc',
          'accent-content': '#ffffff',
          neutral: '#666666',
          'neutral-focus': '#4c4c4c',
          'neutral-content': '#ffffff',
          'base-100': '#f7f7f7',
          'base-200': '#ededed',
          'base-300': '#dddddd',
          'base-content': '#16191c',
          info: '#32baff',
          success: '#14b714',
          warning: '#ffdd32',
          error: '#ff3232',
        },
        dark: {
          ...require('daisyui/src/theming/themes')['[data-theme=dark]'],
          primary: '#4ca5fe',
          'primary-focus': '#198cff',
          'primary-content': '#f8f8f8',
          secondary: '#f6a555',
          'secondary-focus': '#f38c24',
          'secondary-content': '#f8f8f8',
          accent: '#4cfefe',
          'accent-focus': '#19feff',
          'accent-content': '#ffffff',
          neutral: '#999999',
          'neutral-focus': '#7f7f7f',
          'neutral-content': '#ffffff',
          'base-100': '#0c0c0c',
          'base-200': '#191919',
          'base-300': '#333333',
          'base-content': '#f2f2f2',
          info: '#65cbff',
          success: '#19e519',
          warning: '#feff65',
          error: '#ff6565',
        },
      },
    ],
  },
};
