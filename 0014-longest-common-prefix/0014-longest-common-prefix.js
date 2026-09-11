/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
        let pre = strs[0];

    for (let i = 1; i < strs.length; i++) {
        while (!strs[i].startsWith(pre)) {
            pre = pre.slice(0, -1);
        }
    }

    return pre;
};