/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr.sort((a,b)=>fn(a)-fn(b))
    //we are using compare function inside sort function which is optional and which will automatically sort the two values

    //for descending order we can use fn(b)-fn(a)
    
};