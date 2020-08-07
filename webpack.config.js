const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
    //web pack reads from file below
  entry: {
    index: './src/main/index.js',
    setup: './src/setup/setup.js',
    dashboard:'./src/dashboard/dashboard.js',
    guest: './src/guest/guest.js'
  },
  mode: 'development',
  devServer: {
    open: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js'
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: './src/main/index.html',
      inject: true,
      chunks: ['index'],
      filename: 'index.html'
    }),
    new HtmlWebpackPlugin({
      template: './src/setup/setup.html',
      inject: true,
      chunks: ['setup'],
      filename: 'setup.html'
    }),
    new HtmlWebpackPlugin({
      template: './src/dashboard/dashboard.html',
      inject: true,
      chunks: ['dashboard'],
      filename: 'dashboard.html'
    }),
    new HtmlWebpackPlugin({
      template: './src/guest/guest.html',
      inject: true,
      chunks: ['guest'],
      filename: 'guest.html'
    })
  ]
};