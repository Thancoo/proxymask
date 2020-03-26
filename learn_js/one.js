function TestOne() {
    /*
    * number
    * undefined/null
    * boolean
    * function
    * object
    * */
    let num = 3.14;
    let num1 = 2;

    let b;

    let boolean = false;
    console.log(num);
    console.log(num1);
    console.log(typeof 3.14);
    console.log(typeof num1);
    console.log(typeof boolean);
    console.log(b);
    ll = 'll';
    document.writeln(typeof testTwo);
    document.write('<br>');
    document.writeln(typeof ll);
    document.writeln(typeof LL);
}

function testTwo() {
    if ('ll') {
        document.write('not null');
    } else {
        document.write("null");
    }
}

let f = function () {
    /*
    *
    * steps
    *
    *
    *
    *
    * */
    return "Hello, java";
};

let ll = {
    name: 'LLL',
    age: 34,
    walk: function () {
        console.log(this.name + 'can walk, and her age is ' + this.age.toString());
    },
    obj: {
        husband: "hgg",
        age: 45,
        university: 'GZDX',
        all: function (age) {
            if (age < 25) {
                console.log("ai");
            } else {
                console.log("not love");
            }

        }
    }

};

function zxOne(girlName, age, work) {
    if (girlName === 'lll') {
        console.log("Can be a gf");
        if (age > 30) {
            console.log("Too old");
        } else {
            if (work === 'teacher') {
                console.log("No way");
            } else {
                console.log("Merry me");
            }
        }
    } else {
        console.log('No way');
    }
}

function TestNaN() {
    let test = 312;
    let test1 = '123';
    let test2 = "Hello, world";

    console.log(Number(test1));
    document.writeln(Number(test2)); // Not a Number

    document.write(isNaN(test1) + "<br />");
    document.write(isNaN(test2));
}

function testParseInt() {
    console.log(parseInt('10000', 10));
}

function iLan(name, age = 18) {
    console.log(`${name} + ${age.toString()}`);
}

iLan('zx', 20);

// zxOne('zx');


function func(a, b, c) {
    let d = b * b - 4 * a * c;
    if (d < 0) {
        return "No root";
    } else if (d === 0) {
        let x = (-b + Math.sqrt(d)) / (2 * a);
        return `x1 = x2 = ${x}`;
    } else {
        let x1 = (-b + Math.sqrt(d)) / (2 * a);
        let x2 = (-b - Math.sqrt(d)) / (2 * a);
        return `x1 = ${x1}, x2 = ${x2}`
    }
}

// 韩信带领 1500 人打仗，死伤四五百人，这时，他让三个三个站在一起剩下2人，
// 五个五个站在一起剩下3人，七个七个站在一起剩下2人，问现在还有士兵多少人？

let checkPerson = function () {
    let i = 1500 - 500;
    while (i < (1500 - 400)) {
        if ((i % 3 === 2) && (i % 5 === 3) && (i % 7 === 2)) {
            console.log(i);
        }
        i++;
    }
};

checkPerson();