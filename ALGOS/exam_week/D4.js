console.log("There is no spoon");
/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
    let tempObj = {};
    while (cents > 0) {
        if (cents >= 25) {
            console.log(cents);
            if (!tempObj["quarter"]) {
                tempObj["quarter"] = 1;
            } else {
                tempObj["quarter"]++;
            }
            cents -= 25;
        } else if (cents >= 10) {
            console.log(cents);
            if (!tempObj["dime"]) {
                tempObj["dime"] = 1;
            } else {
                tempObj["dime"]++;
            }
            cents -= 10;
        } else if (cents >= 5) {
            console.log(cents);
            if (!tempObj["nickel"]) {
                tempObj["nickel"] = 1;
            } else {
                tempObj["nickel"]++;
            }
            cents -= 5;
        } else if (cents >= 1) {
            console.log(cents);
            if (!tempObj["penny"]) {
                tempObj["penny"] = 1;
            } else {
                tempObj["penny"]++;
            }
            cents -= 1;
        }
    }
    return tempObj;
}

console.log(fewestCoinChange(cents1));
console.log(fewestCoinChange(cents2));
console.log(fewestCoinChange(cents3));
console.log(fewestCoinChange(cents4));

//    temp obj
//if checks, 
//more than 25? add a quarter
//quarter += 1
//if 10 then dime
// if five then nickel
//else penny
// at the end of the if check, you subtract quarter, dime, nickel, etc from cents
//if 0 return dictionary