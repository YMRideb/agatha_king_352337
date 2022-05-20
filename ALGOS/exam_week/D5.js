// console.log("there is no spoon");
/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];

const nums6 = [5, 4, 1, 4, 1, 5];
const expected6 = [];
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
function mode(nums) {
    //initialize an empty array
    let arr = [];
    let object = {};
    if (nums.length <= 1) {
        return nums;
    }
    for (i = 0; i < nums.length; i++) {
        if (object.hasOwnProperty(nums[i])) {
            object[nums[i]] += 1;
        } else {
            object[nums[i]] = 1;
        }
    }
    let new_high_value = 0;
    let count = 1;
    for (key in object) {
        if (object[key] > new_high_value) {
            arr = [];
            new_high_value = object[key];
            arr.push(parseInt(key));
        } else if (object[key] == new_high_value) {
            arr.push(parseInt(key));
        }
    }
    let total_nums = Object.keys(object).length;
    if (total_nums == arr.length) {
        arr = [];
    }
    arr.push();
    return arr;
}
console.log(mode(nums1));
console.log(mode(nums2));
console.log(mode(nums3));
console.log(mode(nums4));
console.log(mode(nums5));


// if (count == object[]);
//check if this index exists, incrememnt the value, if not initialize key in obj = 1
//check highest value in obj, return obj
// if not return arr
//highest value, return as long as it is not the same amount != all have the same value return arr