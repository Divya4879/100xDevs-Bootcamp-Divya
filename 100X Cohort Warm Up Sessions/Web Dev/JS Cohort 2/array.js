// array.push(item)

let exampleArray = [2,4,6];
exampleArray.push(5);        

console.log(exampleArray);           // [ 2, 4, 6, 5 ]

// array.pop()

console.log(exampleArray.pop());     // 5

console.log(exampleArray);           // [ 2, 4, 6 ]

// array.shift() - removes 1st item from the array

console.log(exampleArray.shift())    // 2

// array.unshift(item)  - adds the item to the 1st idx of array, and returns the length of the new array

console.log(exampleArray.unshift("Divya"));   // 3

console.log(exampleArray);            // [ 'Divya', 4, 6 ]

// arr1.concat(arr2)

console.log(["Divya","Ria","Issabella"].concat(["Coffee","Tea","Water"]));
 // [ 'Divya', 'Ria', 'Issabella', 'Coffee', 'Tea', 'Water' ]

// array.forEach(function) - this function is executed for each element of the array
// forEach is for side effects, not transformations.

let testArray = [4,7,65,46];

function doubleItem(z){
    console.log(z*2);
    // return z*2;   // this will be ignored, will return undefined
}

testArray.forEach(doubleItem);

```

Output:- 

8
14
130
92

```