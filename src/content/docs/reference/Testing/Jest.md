---
title: Jest
---

Jest is one of most popular testing frameworks for its ease of use.

The best way to run tests in VSCode is with the [extension](https://github.com/jest-community/vscode-jest).

Write ` jest --coverage` into package.json next to `test`. The --coverage flag makes Jest generate coverage data for tests automatically. This is useful to see which parts of your codebase lack testing. It writes this data into a coverage folder.

Add /coverage/ to your .gitignore

`expect("values") ... matcher`

There are lots of matchers, like toBe(), toEqual(), toContain(), etc.

.toBe()

- Checks primitive values like numbers and booleans.

.toEqual()

- Checks values of objects and arrays

.toBeFalsy()

- Checks if value is falsy, ie false, 0, '', undefined etc.

.toBeTruthy()

- Checks if value is truthy, ie not false, 0, '', undefined etc.

.toThrow()

- Checks if an error is thrown. Ie. invalid input etc.

## Testing async code

- Callbacks
  - The done parameter is passed to the callback.
- Promises
  - use resolves and rejects
- Async
  - use async and await
  - Cleaner testing

## Mock Functions and Spies

Mocking isolates the unit of code which is being tested. Replace slow or unavailable functions.
Use jest.fn to write a mock function.

```js
test("mock implementation of a function", () => {
  const mock = jest.fn((x) => 42 + x);
  expect(mock(1)).toBe(43);
  expect(mock).toHaveBeenCalledWith(1);
});
```

Use toHaveBeenCalledWith to check if a function was called with certain arguments.

Use spy to see if a function was called. Spy.mockRestore() to restore the original function.

## Resources

[Jest Crash Course](https://www.youtube.com/watch?v=IPiUDhwnZxA)
[Practise Unit Tests](https://github.com/breatheco-de/exercise-unit-test-with-jest)
[Jest Sample Tests](https://github.com/Lemoncode/jest-testing-by-sample)
[Jest with React](https://auth0.com/blog/testing-react-applications-with-jest/)
[Jest Docs](https://jestjs.io/)
[Jest and Puppeteer](https://github.com/argos-ci/jest-puppeteer)
[Jest Cheat Sheet](https://github.com/sapegin/jest-cheat-sheet)
[Jest GUI: Majestic](https://github.com/Raathigesh/majestic)
[Jest Preview](https://www.jest-preview.com/)
[Awesome Jest Reources](https://github.com/jest-community/awesome-jest)

```

```
