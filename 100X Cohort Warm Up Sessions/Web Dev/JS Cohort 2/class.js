class Animal{
    constructor(name, legCount, speaks){
        this.name = name;
        this.legCount = legCount;
        this.speaks = speaks;
    }

    static myType(){      // Not associated with any object, just the class itself- Animal.myType()
        console.log("Animal");
    }

    speak(){
        console.log(`${this.name} makes a noise.`)  // f-string in Python ~ `${var_name}` in JS
    }
}

Dob = new Animal("Dob", 4, "Woof");

console.log(`My dog ${Dob.name} has ${Dob.legCount} legs and greets me with his excited ${Dob.speaks} everyday.`)
// My dog Dob has 4 legs and greets me with his excited Woof everyday.

Dob.speak();   // Dob makes a noise.

Animal.myType();  // Animal
// Dob.myType();   // Throws an error