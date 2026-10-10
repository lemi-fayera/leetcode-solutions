/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    
    let count = new Map()
    let total = 0
    let jewelses = new Set()
    for (const jewel of jewels ){
        jewelses.add(jewel)
    }

    for( const stone of stones) {
        count.set(stone, (count.get(stone) || 0) + 1)
    }
    for (let [key, value] of count)  {
        if (jewelses.has(key)) {
            total += value
        }
            
    }
    return total
};