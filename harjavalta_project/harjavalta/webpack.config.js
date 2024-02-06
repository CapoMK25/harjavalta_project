const path = require("path");

module.exports = {
  mode: 'development',
  entry: path.resolve(__dirname, "./src/index.js"),
  output: {
    path: path.resolve(__dirname, "src/harjavalta"),
    filename: "bundle.js",
  },
  resolve: {
    modules: [path.resolve(__dirname, "harjavalta/src"), "node_modules"],
    extensions: [".js", ".json", ".jsx"],
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
};
