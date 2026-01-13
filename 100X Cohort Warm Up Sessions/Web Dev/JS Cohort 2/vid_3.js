let sum = 0;

for(let i=0; i<=100; i++){
    sum += i;
}

console.log(sum)     // 5050

// Callback Functions

function sum1(a,b,c){
    return a+b+c;
}

function mult(a,b,c){
    return a*b*c;
}

function result(a,b,c,func){
    return func(a,b,c);
}

console.log(result(5,8,4,sum1));   // 17
console.log(result(4,8,6,mult));   // 192

// Anonymous Functions

function sumOfSomething(a,b,c,func){
    console.log(func);    // [Function (anonymous)]
    let a1 = func(a,b,c);
    let b1 = func(a,b,c);
    let c1 = func(a,b,c);
    return a1 + b1+ c1;
}

const answer = sumOfSomething(3,6,4, function (a,b,c){
    return a*b*c;
});
console.log(answer)  // mult function removed, and used directly like this and anonymously, without a function name

// anymous func- these functions like this can't be called elsewhere in the code.


