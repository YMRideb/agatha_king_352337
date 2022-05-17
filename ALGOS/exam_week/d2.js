console.log("there is no spoon");
/* 
  Given two arrays, interleave them into one new array.
  The arrays may be different lengths. The extra items should be added to the
  back of the new array.
*/

const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
const expected2 = [1, 2, 3, 4, 6, 8];

const arrA5 = [1, 3, [1, 3, 5]];
const arrB5 = [2, 4, 6, 8];
const expected5 = [1, 2, 3, 4, [1, 3, 5], 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 4];
const expected3 = [1, 2, 3, 4, 5, 7];

const arrA4 = [];
const arrB4 = [42, 0, 6];
const expected4 = [42, 0, 6];


function interleaveArrays(arr1, arr2) {
    let arr = [];
    temp = arr1.length;
    if (arr2.length > temp) {
        temp = arr2.length;
    }
    for (i = 0; i < temp; i++) {
        if (arr1[i] != undefined) {
            arr.push(arr1[i]);
        }
        if (arr2[i] != undefined) {
            arr.push(arr2[i]);
        }
    }
    return arr;
}
console.log(interleaveArrays(arrA1, arrB1));
console.log(interleaveArrays(arrA2, arrB2));
console.log(interleaveArrays(arrA3, arrB3));
console.log(interleaveArrays(arrA4, arrB4));
console.log(interleaveArrays(arrA5, arrB5));



//pseudocode
//for loop can use
//initailize a new array
//use arr.shift() to remove the first index of the passed in array
//use push() to insert in to the new array
// ******************************************************************************
/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const two_nums1 = [1, 3, 5, 6];
const two_searchNum1 = 4;
const two_expected1 = false;

const two_nums2 = [4, 5, 6, 8, 12];
const two_searchNum2 = 5;
const two_expected2 = true;

const two_nums3 = [3, 4, 6, 8, 12];
const two_searchNum3 = 3;
const two_expected3 = true;

// bonus, how many times does the search num appear?
const two_nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const two_searchNum4 = 2;
const two_expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
function binarySearch(sortedNums, searchNum) {

}
//figure out the first and last number finding the midpoint
//arr.length / 2, position [2]
// Math.floor
// > = <
//go down the array
//arr[i] - 1
const two_nums2 = [4, 5, 6, 8, 12];
//position [1] == searchNum?
//return that position[i]