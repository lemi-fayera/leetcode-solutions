/**
 * @param {string} s
 * @return {boolean}
 */


function clean(s) {
  return s.toLowerCase().replace(/[^a-z0-9]/g, "");
}

function isPalindrome(s) {
  const cleaned = clean(s);
  const reversed = cleaned.split("").reverse().join("");
  if (cleaned === reversed) {
    return true;
  }
  return false;
}