const dateToday = new Date();

console.log(dateToday.getDate());   // 13
console.log(dateToday.getYear());   // 126 - starting from 1900
console.log(dateToday.getMonth());  // 0- 0 index(January rn)
console.log(dateToday.getMinutes()); // 50- it's 00:50 rn
console.log(dateToday.getHours());  // 0
console.log(dateToday.getSeconds()); // 33
console.log(dateToday.getFullYear()); // 2026

dateToday.setFullYear(2026);
console.log(dateToday.toDateString()); // Tue Jan 13 2026

console.log(dateToday.getTime());  // 1768246625882 - All the milliseconds since 1970

// 1st Jan 1970- epoch time

// using this in our code- to find the time it took to execute

function sum(n){
    let counter = 0;
    for(let i = 0; i <=n; i++){
        counter += i;
    }
    return counter;
}

time1 = new Date().getTime();
console.log(time1);

console.log(sum(1000000000));    // It took 12 ms.

time2 = new Date().getTime();
console.log(time2);   

let timeDiff = time2 - time1;

console.log(`The time it took to execute this function:- ${timeDiff} ms.`)