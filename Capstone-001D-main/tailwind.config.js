module.exports = {
  content: [
    './app/templates/**/*.html',
    './app/static/app/js/**/*.js',
    './app/static/app/css/**/*.css',
  ],
  theme: {
    extend: {
      colors: {
        cyan: {
          500: '#00bfff',
          400: '#33ccff',
          300: '#66d9ff',
          200: '#99e6ff',
          100: '#ccf3ff',
        },
        blue: {
          900: '#0d3b66',
          800: '#1155cc',
          700: '#1976d2',
          600: '#1e90ff',
          500: '#3399ff',
          400: '#66b3ff',
          300: '#99ccff',
          200: '#cce6ff',
          100: '#e6f2ff',
        },
        purple: {
          900: '#28193d',
          700: '#6a1b9a',
          600: '#8e24aa',
          500: '#9c27b0',
          400: '#af52bf',
        },
        pink: {
          500: '#ff4081',
          400: '#ff79b0',
        },
      },
      backgroundImage: {
        'gradient-blue-purple': 'linear-gradient(to right, #1976d2, #6a1b9a, #8e24aa)',
        'gradient-purple-pink': 'linear-gradient(to right, #9c27b0, #ff4081, #ff79b0)',
        'gradient-cyan': 'linear-gradient(to right, #00bfff, #33ccff, #66d9ff)',
      },
    },
  },
  plugins: [],
};