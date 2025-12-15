📘 ES6 Data Manipulation

Holberton School — Back-end Specialization

This project introduces essential ES6 tools and data structures used to manipulate data efficiently in modern JavaScript.
You will work with arrays, typed arrays, Set, Map, and advanced methods such as filter, map, reduce, DataView, and more.

The goal is to help you write cleaner, more expressive, and more optimized data-handling code.

📂 Project Contents
0. Basic list of objects — 0-get_list_students.js

Creates a function returning an array of student objects containing:
id, firstName, and location.

1. More mapping — 1-get_list_student_ids.js

Returns an array of student ids.

Must use Array.map()

Returns an empty array if the argument is not an array.

2. Filter — 2-get_students_by_loc.js

Returns all students located in a specific city.

Must use Array.filter()

3. Reduce — 3-get_ids_sum.js

Returns the sum of all student ids.

Must use Array.reduce()

4. Update student grades — 4-update_grade_by_city.js

Returns students from a specific city and attaches their updated grade.

Must combine filter() + map()

If a student has no grade → "N/A"

5. Typed Arrays — 5-typed_arrays.js

Creates an ArrayBuffer and uses a DataView to write an Int8 value at a specific position.

Throws "Position outside range" if the index is invalid.

6. Set data structure — 6-set.js

Returns a Set created from an array.
Duplicates are automatically removed.

7. More set data structure — 7-has_array_values.js

Checks whether all elements in an array exist within a Set.

Uses Array.every() combined with set.has().

8. Clean set — 8-clean_set.js

Returns a string of all Set values that start with a given prefix.

The returned string contains the remaining part after the prefix.

Values are joined using -.

Returns an empty string if the prefix is an empty string or not a string.

9. Map data structure — 9-groceries_list.js

Returns a Map representing a grocery list with the following items:

Item	Quantity
Apples	10
Tomatoes	10
Pasta	1
Rice	1
Banana	5
10. More map data structure — 10-update_uniq_items.js

Updates a Map by changing all items with quantity 1 to 100.

Throws "Cannot process" if the argument is not a Map.

🧠 Key ES6 Concepts Covered
✔️ Array manipulation

map()

filter()

reduce()

every()

Spread operator (...)

✔️ Typed Arrays

ArrayBuffer

DataView

Writing values with setInt8()

✔️ Set

Automatic duplicate removal

Fast membership checking (set.has())

✔️ Map

Key/value pairs

Updating values with map.set()

Iteration with for…of

⚙️ Installation & Usage
Install dependencies
npm install

Run a script
npm run dev <file.js>

Run tests (Jest)
npm test

Run ESLint
npm run lint

Full project check (tests + lint)
npm run full-test

🎯 Learning Objectives

By the end of this project, you should be able to:

Handle and transform data using modern ES6 methods

Work effectively with Set, Map, ArrayBuffer, DataView

Chain array methods to write expressive and clean code

Validate input types and handle errors gracefully

Produce code that passes both Jest and ESLint
