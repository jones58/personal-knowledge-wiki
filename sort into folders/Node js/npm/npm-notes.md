---
title: Npm Notes
---

# NPM notes

- Package managers emerged to solve the issue of automating download and upgrade of libraries from central repository. In other words, you can manage dependencies (external code) that project needs to run correctly.
- npm is the most popular package manageers, then yarn (which uses npm underneath anyway) and works in a similar way.
- (pnpm)[https://pnpm.io/] is a good alternative to npm if you want to save disk space.
- modules are basically javascript libraries.
- originally made for node.js (backend server js)
- No longer use vanilla javascript.

## Key commands

- `npm init` and keep clicking enter. and then yes. You can fill in these details if building something want to share.
- to skip this can write `npm init --yes` to instantly initialise without these. Later can edit in package.json file.
- This creates a package.json file.
- Will also create node_modules folder which can be added to git ignore because it gets big and other devs can install these dependencies with `npm install`.
- `npm install <module-name>` where module-name is name of module you want to install and `i` is an alias for install.
- then can install node modules, like `npm i moment`, or
- to get the require modules working in browser, can use a module bundleer called browserify to make a bundle (`browserify main.js -o bundle.js`), and change link in html to bundle.js.
- this can also be done with Webpack which is more popular than Browserify
- can use babel and typescript as transpilers to transform code

## Resources

- [Vanilla js vs modern js] (https://peterxjang.com/blog/modern-javascript-explained-for-dinosaurs.html)
- [FreeCodeCamp NPM tutorial](https://www.youtube.com/watch?v=2V1UUhBJ62Y)
- [Beginner's guide to npm](https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/)
- [npm tricks](https://nodesource.com/blog/eleven-npm-tricks-that-will-knock-your-wombat-socks-off)
