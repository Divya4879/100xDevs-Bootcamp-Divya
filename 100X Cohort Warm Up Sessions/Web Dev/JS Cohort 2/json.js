const users={
            "name":"Divya",
            "age":20,
            "Field":"Tech",
            "Interest":"Dev"
            }

// JSON.parse
// JSON.stringify(json_var)

const testString = JSON.stringify(users);

console.log(testString);  // {"name":"Divya","age":20,"Field":"Tech","Interest":"Dev"}
console.log(typeof(testString))  // string

console.log(testString["name"]) // undefined

console.log(users["name"])      // Divya