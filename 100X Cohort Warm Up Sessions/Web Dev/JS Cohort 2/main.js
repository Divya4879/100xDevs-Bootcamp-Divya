let a = 1;
a = 2;

console.log(a);
console.log(4)

const b = 1;

// b = 2;  // Assignment to constant variable.


let fname = 'Divya';
let age = 20;
let isMarried = false;

if(isMarried){
    console.log(fname + 'is married.')
}
else{
    console.log(fname +" is not married.")
}


// For loop

let sum = 0;

for(let i=0; i <= 1000; i++){
    sum += i;
}

console.log(sum);

// Questions from the Video

// Ques 1: Greeting a person given their fname  & lname

// let fname = 'Divya';
let lname = 'Singh'

console.log('Hello ' + fname + ' ' + lname + '!');

// Ques 2: Greeting a person based on their age

let gender = 'Female';

if(gender == 'Female'){
    console.log('Hello lady!');
}
else{
    console.log('Hello dude!')
}


// Arrays

let person1 = 'Divya';
let person2 = 'Ria';
let person3 = 'Issabella';

const people = ['Divya', 'Ria', 'Issabella'];
const ages = [20, 19, 14];

console.log(people[0]);
console.log(people[1]);
console.log(people[2]);

// Program that prints all even numbers in an array

const nums = [2,7,4,6,46,75,57,78];

for(let i=0; i<nums.length; i++){
    if(nums[i]%2==0){
        console.log(nums[i]);
    }
}

// WAP to print the biggest no. in an array

let max = 0;
for(let i=0; i<nums.length; i++){
    if(nums[i]>max){
        max = nums[i];
    }
}

console.log(max);

// OBJECTS

const peeps = ['Ram', 'Shyam', 'Rama'];
const genders = ['Male', 'Male', 'Female'];

for(let i=0; i<peeps.length; i++){
    if(genders[i]=='Male'){
        console.log(peeps[i]);
    }
}

// An object to store person details
const peepsObject = [
    {
        firstName : "Ram",
        gender : "Male",
    },
    {
        firstName : 'Shyam',
        gender : 'Male',
    },
    {
        firstName : 'Rama',
        gender : 'Female'
    }
]

for(let i=0; i<peepsObject.length;i++){
    if(peepsObject[i].gender== 'Male'){
        console.log(peepsObject[i]['firstName']);
    }
}

// Functions

// WAP using a function to add 2 nos

function addTwoNumbers(num1, num2, fnToCall){
    let sum = num1 + num2;
    fnToCall(sum);
}

function prettyResult(data){
    console.log("The result is " + data);
}

function displayPassiveResult(data){
    console.log("The sum of the two numbers is " + data);
}

addTwoNumbers(3,8,displayPassiveResult);

// Assignment Ques- 

// Question  1

for(let i = 30; i>=0; i--){
    console.log(i);
}

// Question 2 - Calculate the time between a setTimeout call, and the inner function actually running

function test(a,b){
    console.log("test");
    console.log(a + b);
}

console.log("Test Divya")
console.log(setTimeout(test, 2 * 1000, 4 , 9));  // setTimeout() loses the return value, so just console it.

// Result:- 

// Test Divya
// Timeout {
//   _idleTimeout: 2000,
//   _idlePrev: [TimersList],
//   _idleNext: [TimersList],
//   _idleStart: 54,
//   _onTimeout: [Function: test],
//   _timerArgs: [Array],
//   _repeat: null,
//   _destroyed: false,
//   Symbol(refed): true,
//   Symbol(kHasPrimitive): false,
//   Symbol(asyncId): 6,
//   Symbol(triggerId): 1,
//   Symbol(kAsyncContextFrame): undefined
// }
// test
// test
// 13

// time we set in the setTimeout is the min time after which the function will be called, here idleStart is 54(ms), so the function will
// run 2054 ms after we run this file at minimum. This time may increase in case of throttling, bottlenecks, delay_inflation. but none of that's mentioned here.
// so, ideally this program will run after 2054 ms.

// Terminal Clock- displays the date time every min

function timeNow(){
    let time = new Date().toTimeString();
    console.log(time);
}
timeNow();
setInterval(timeNow, 60 * 1000);