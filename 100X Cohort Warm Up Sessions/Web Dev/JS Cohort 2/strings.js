// Strings

// str.length

function getLength(str){
    return str.length;
}

console.log(getLength('Divya'));  // 5

// str.indexOf(target)

function findIndexOf(str, target){
    return str.indexOf(target);
}

console.log(findIndexOf("Divya","i"));  // 1

// str.lastIndexOf(target)

console.log(findIndexOf("Divya","vya"));  // 2

console.log("Divya is a good good goodie good human.".lastIndexOf("good"));  // 28

// str.splice(start_index,last_index)

console.log("My Very Excellent Mother Just Served Me Noodles".slice(5,10)); // ry Ex


// str.replace(original_one, new_one)- it won't throw an error if the original_one isn't in the str

console.log("Divya is a girl".replace("girl","techie"));

// str.split(delimeter)

console.log("Divya is a human being.".split(" "))   // [ 'Divya', 'is', 'a', 'human', 'being.' ]

// str.trim() - like strip() in python

console.log("       Hello       peeps!          ".trim());    // Hello       peeps!


//  str.toUpperCase()

console.log("divYa".toUpperCase());  // DIVYA


// str.toLowerCase()

console.log("DIVYa".toLowerCase());    // divya