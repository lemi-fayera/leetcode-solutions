/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let one = 1;
    let two = 2;

    if (n === 1) return one;
    if (n === 2) return two;

    for (let i = 3; i <= n; i++) {
        let next = one + two;
        one = two;
        two = next;
    }

    return two;
};