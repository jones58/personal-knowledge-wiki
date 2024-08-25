let sales = 123456789;
let course = "TypeScript";
let is_published = true;
let level;
level = 1;
level = "a";

const enum Size {
  Small = 1,
  Medium,
  Large,
}
let mySize: Size = Size.Large;
console.log(mySize);

function printName(name: string | null) {
  if (name) {
    console.log("Your name is: " + name);
  } else {
    console.log("No name was provided!");
  }
}

printName(null);
