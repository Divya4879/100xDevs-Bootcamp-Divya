// Object.keys(obj)

// Object.values(obj)

// Object.entries(obj)  - [[Key1,value1],[key2,value2],...]

// Object.hasOwnPoperty("property")  - returns true  or false

// Object.assign({}, obj, {newProperty: "newValue"}); - new object with more entries

const obj1 = {
    key1 : "value1",
    key2 : "value2",
    key3 : "value3"
}



let newObj = Object.assign({}, obj1, {newProperty: "newValue"});
console.log(newObj);

```

{
  key1: 'value1',
  key2: 'value2',
  key3: 'value3',
  newProperty: 'newValue'
}
  
```

console.log(obj1)    // { key1: 'value1', key2: 'value2', key3: 'value3' }