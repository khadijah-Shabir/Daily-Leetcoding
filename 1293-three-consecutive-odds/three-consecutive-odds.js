/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {
    let i=0;
    for(const n of arr){
        if (n%2!=0){
            i++;
            if(i>=3){
            return true;
            }
        }else{
            i=0;
        }
        
    }
    return false;
};